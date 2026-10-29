import sqlite3
import sys
from datetime import date
from pathlib import Path

from PyQt5.QtWidgets import QApplication, QDialog, QMessageBox, QTableWidgetItem, QWidget

from ftask2 import Ui_Form

DB = Path(__file__).with_name('films_db.sqlite')


class FilmForm(QDialog, Ui_Form):
    def __init__(self, connection, film=None):
        super().__init__()
        self.setupUi(self)
        self.listArea.hide()
        self.formArea.move(0, 0)
        self.resize(450, 270)
        self.connection = connection
        self.film = film
        self.setWindowTitle('Изменить фильм' if film else 'Добавить фильм')
        for genre_id, title in connection.execute('SELECT id, title FROM genres ORDER BY title'):
            self.genreBox.addItem(title, genre_id)
        if film:
            self.idEdit.setText(str(film[0]))
            self.titleEdit.setText(film[1] or '')
            self.yearEdit.setText(str(film[2] or ''))
            self.genreBox.setCurrentIndex(self.genreBox.findData(film[3]))
            self.durationEdit.setText(str(film[4] or ''))
        self.saveButton.clicked.connect(self.save)
        self.cancelButton.clicked.connect(self.reject)

    def save(self):
        title = self.titleEdit.text().strip()
        try:
            year = int(self.yearEdit.text())
            duration = int(self.durationEdit.text())
        except ValueError:
            QMessageBox.warning(self, 'Ошибка', 'Год и длительность должны быть числами.')
            return
        if not title or not 1 <= year <= date.today().year or duration <= 0 or self.genreBox.currentIndex() < 0:
            QMessageBox.warning(self, 'Ошибка', 'Проверьте название, год, жанр и длительность.')
            return
        values = (title, year, self.genreBox.currentData(), duration)
        if self.film:
            self.connection.execute('UPDATE films SET title=?, year=?, genre=?, duration=? WHERE id=?',
                                    (*values, self.film[0]))
        else:
            self.connection.execute('INSERT INTO films(title, year, genre, duration) VALUES (?, ?, ?, ?)', values)
        self.connection.commit()
        self.accept()


class MainWindow(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.formArea.hide()
        self.resize(860, 590)
        self.connection = sqlite3.connect(DB)
        self.addButton.clicked.connect(self.add_film)
        self.editButton.clicked.connect(self.edit_film)
        self.deleteButton.clicked.connect(self.delete_film)
        self.tableFilms.setEditTriggers(self.tableFilms.NoEditTriggers)
        self.tableFilms.setSelectionBehavior(self.tableFilms.SelectRows)
        self.tableFilms.setSelectionMode(self.tableFilms.SingleSelection)
        self.refresh()

    def refresh(self):
        cursor = self.connection.execute('''SELECT films.id, films.title, films.year,
                        genres.title AS genre, films.duration
                        FROM films LEFT JOIN genres ON films.genre = genres.id''')
        rows = cursor.fetchall()
        self.tableFilms.clear()
        self.tableFilms.setColumnCount(len(cursor.description))
        self.tableFilms.setHorizontalHeaderLabels([column[0] for column in cursor.description])
        self.tableFilms.setRowCount(len(rows))
        for i, row in enumerate(rows):
            for j, value in enumerate(row):
                self.tableFilms.setItem(i, j, QTableWidgetItem(str(value) if value is not None else ''))
        self.tableFilms.resizeColumnsToContents()

    def selected_id(self):
        row = self.tableFilms.currentRow()
        if row < 0 or not self.tableFilms.selectedItems():
            QMessageBox.warning(self, 'Ошибка', 'Выберите фильм в таблице.')
            return None
        return int(self.tableFilms.item(row, 0).text())

    def add_film(self):
        if FilmForm(self.connection).exec_():
            self.refresh()

    def edit_film(self):
        film_id = self.selected_id()
        if film_id is None:
            return
        film = self.connection.execute('SELECT * FROM films WHERE id=?', (film_id,)).fetchone()
        if FilmForm(self.connection, film).exec_():
            self.refresh()

    def delete_film(self):
        film_id = self.selected_id()
        if film_id is None:
            return
        self.connection.execute('DELETE FROM films WHERE id=?', (film_id,))
        self.connection.commit()
        self.refresh()

    def closeEvent(self, event):
        self.connection.close()
        super().closeEvent(event)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
