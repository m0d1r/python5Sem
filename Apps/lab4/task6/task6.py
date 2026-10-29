import hashlib
import hmac
import os
import shutil
import sqlite3
import sys
import uuid
from datetime import date
from pathlib import Path

from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QIcon, QPainter, QPixmap
from PyQt5.QtWidgets import QApplication, QFileDialog, QMessageBox, QTableWidgetItem, QWidget

from ftask6 import Ui_Form

DIRECTORY = Path(__file__).parent


class MainWindow(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.db = sqlite3.connect(DIRECTORY / 'library.sqlite')
        self.db.execute('CREATE TABLE IF NOT EXISTS users (login TEXT PRIMARY KEY, salt BLOB, password_hash BLOB)')
        self.db.execute('''CREATE TABLE IF NOT EXISTS books (
            id INTEGER PRIMARY KEY, title TEXT, author TEXT, year INTEGER,
            genre TEXT, image_path TEXT)''')
        self.db.commit()
        self.selected_book_id = None
        self.image_path = ''
        self.pages.setCurrentWidget(self.loginPage)
        self.loginButton.clicked.connect(self.login)
        self.goRegisterButton.clicked.connect(lambda: self.pages.setCurrentWidget(self.registerPage))
        self.backToLoginButton.clicked.connect(lambda: self.pages.setCurrentWidget(self.loginPage))
        self.registerButton.clicked.connect(self.register)
        self.searchTitleEdit.textChanged.connect(self.show_books)
        self.searchAuthorEdit.textChanged.connect(self.show_books)
        self.addBookButton.clicked.connect(self.add_book)
        self.editBookButton.clicked.connect(self.edit_book)
        self.deleteBookButton.clicked.connect(self.delete_book)
        self.chooseImageButton.clicked.connect(self.choose_image)
        self.saveBookButton.clicked.connect(self.save_book)
        self.cancelBookButton.clicked.connect(lambda: self.pages.setCurrentWidget(self.catalogPage))
        self.booksTable.setColumnCount(5)
        self.booksTable.setHorizontalHeaderLabels(['Название', 'Автор', 'Год', 'Жанр', 'Обложка'])
        self.booksTable.setEditTriggers(self.booksTable.NoEditTriggers)
        self.booksTable.setSelectionBehavior(self.booksTable.SelectRows)
        self.booksTable.setSelectionMode(self.booksTable.SingleSelection)
        self.booksTable.setIconSize(QSize(45, 58))
        self.booksTable.itemSelectionChanged.connect(self.show_cover)
        self.coverLabel.setAlignment(Qt.AlignCenter)

    def register(self):
        login = self.regLoginEdit.text().strip()
        password = self.regPasswordEdit.text()
        if not login or not password:
            QMessageBox.warning(self, 'Ошибка', 'Укажите логин и пароль.')
            return
        salt = os.urandom(16)
        password_hash = hashlib.pbkdf2_hmac('sha256', password.encode(), salt, 200000)
        try:
            self.db.execute('INSERT INTO users VALUES (?, ?, ?)', (login, salt, password_hash))
            self.db.commit()
        except sqlite3.IntegrityError:
            QMessageBox.warning(self, 'Ошибка', 'Такой логин уже существует.')
            return
        self.loginEdit.setText(login)
        self.passwordEdit.clear()
        self.pages.setCurrentWidget(self.loginPage)

    def login(self):
        user = self.db.execute('SELECT salt, password_hash FROM users WHERE login=?',
                               (self.loginEdit.text().strip(),)).fetchone()
        if not user or not hmac.compare_digest(
                hashlib.pbkdf2_hmac('sha256', self.passwordEdit.text().encode(), user[0], 200000), user[1]):
            QMessageBox.warning(self, 'Ошибка', 'Неверный логин или пароль.')
            return
        self.pages.setCurrentWidget(self.catalogPage)
        self.show_books()

    def placeholder(self):
        image = QPixmap(135, 185)
        image.fill(Qt.lightGray)
        painter = QPainter(image)
        painter.drawText(image.rect(), Qt.AlignCenter, 'Нет обложки')
        painter.end()
        return image

    def cover(self, path):
        image = QPixmap(str(DIRECTORY / path)) if path else QPixmap()
        return image if not image.isNull() else self.placeholder()

    def show_books(self):
        title = '%' + self.searchTitleEdit.text().strip() + '%'
        author = '%' + self.searchAuthorEdit.text().strip() + '%'
        self.books = self.db.execute('''SELECT id, title, author, year, genre, image_path
            FROM books WHERE title LIKE ? AND author LIKE ? ORDER BY title''', (title, author)).fetchall()
        self.booksTable.setRowCount(len(self.books))
        for i, book in enumerate(self.books):
            for j, value in enumerate(book[1:5]):
                self.booksTable.setItem(i, j, QTableWidgetItem(str(value)))
            item = QTableWidgetItem()
            item.setIcon(QIcon(self.cover(book[5])))
            self.booksTable.setItem(i, 4, item)
            self.booksTable.setRowHeight(i, 65)
        self.booksTable.resizeColumnsToContents()
        self.show_cover()

    def show_cover(self):
        row = self.booksTable.currentRow()
        image = self.cover(self.books[row][5]) if 0 <= row < len(self.books) else self.placeholder()
        self.coverLabel.setPixmap(image.scaled(self.coverLabel.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation))

    def selected_book(self):
        row = self.booksTable.currentRow()
        if row < 0 or not self.booksTable.selectedItems():
            QMessageBox.warning(self, 'Ошибка', 'Выберите книгу.')
            return None
        return self.books[row]

    def add_book(self):
        self.selected_book_id = None
        for field in (self.bookTitleEdit, self.bookAuthorEdit, self.bookYearEdit,
                      self.bookGenreEdit, self.bookImageEdit):
            field.clear()
        self.image_path = ''
        self.pages.setCurrentWidget(self.bookFormPage)

    def edit_book(self):
        book = self.selected_book()
        if book is None:
            return
        self.selected_book_id = book[0]
        for field, value in zip((self.bookTitleEdit, self.bookAuthorEdit,
                                 self.bookYearEdit, self.bookGenreEdit, self.bookImageEdit), book[1:]):
            field.setText(str(value or ''))
        self.image_path = book[5] or ''
        self.pages.setCurrentWidget(self.bookFormPage)

    def choose_image(self):
        path, _ = QFileDialog.getOpenFileName(self, 'Выберите обложку', '', 'Изображения (*.png *.jpg *.jpeg *.bmp)')
        if path:
            self.image_path = path
            self.bookImageEdit.setText(path)

    def save_book(self):
        title = self.bookTitleEdit.text().strip()
        author = self.bookAuthorEdit.text().strip()
        genre = self.bookGenreEdit.text().strip()
        try:
            year = int(self.bookYearEdit.text())
        except ValueError:
            year = 0
        if not title or not author or not genre or not 1 <= year <= date.today().year:
            QMessageBox.warning(self, 'Ошибка', 'Заполните название, автора, жанр и корректный год.')
            return
        path = self.image_path
        if path and Path(path).is_absolute():
            (DIRECTORY / 'covers').mkdir(exist_ok=True)
            target = Path('covers') / (uuid.uuid4().hex + Path(path).suffix.lower())
            shutil.copy2(path, DIRECTORY / target)
            path = str(target)
        values = (title, author, year, genre, path)
        if self.selected_book_id is None:
            self.db.execute('INSERT INTO books(title, author, year, genre, image_path) VALUES (?, ?, ?, ?, ?)', values)
        else:
            self.db.execute('UPDATE books SET title=?, author=?, year=?, genre=?, image_path=? WHERE id=?',
                            (*values, self.selected_book_id))
        self.db.commit()
        self.pages.setCurrentWidget(self.catalogPage)
        self.show_books()

    def delete_book(self):
        book = self.selected_book()
        if book is None:
            return
        self.db.execute('DELETE FROM books WHERE id=?', (book[0],))
        self.db.commit()
        self.show_books()

    def closeEvent(self, event):
        self.db.close()
        super().closeEvent(event)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
