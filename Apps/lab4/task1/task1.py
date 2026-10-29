import csv
import sys
from pathlib import Path

from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem

from ftask1 import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        with open(Path(__file__).with_name('rez(1).csv'), encoding='utf-8-sig', newline='') as file:
            self.results = list(csv.DictReader(file))

        self.schoolBox.addItem('Все')
        self.classBox.addItem('Все')
        self.schoolBox.addItems(sorted({row['login'].split('-')[-3] for row in self.results}))
        self.classBox.addItems(sorted({row['login'].split('-')[-2] for row in self.results}))

        self.schoolBox.currentIndexChanged.connect(self.update_table)
        self.classBox.currentIndexChanged.connect(self.update_table)
        self.update_table()

    def update_table(self):
        school = self.schoolBox.currentText()
        grade = self.classBox.currentText()
        rows = [row for row in self.results
                if (school == 'Все' or row['login'].split('-')[-3] == school)
                and (grade == 'Все' or row['login'].split('-')[-2] == grade)]
        scores = sorted({int(row['Score']) for row in rows}, reverse=True)
        colors = [QColor('#FFD700'), QColor('#C0C0C0'), QColor('#CD7F32')]

        self.tableWidget.setRowCount(len(rows))
        for i, row in enumerate(rows):
            values = [row['login'], row['user_name'].split(maxsplit=3)[-1], row['Score']]
            for j, value in enumerate(values):
                item = QTableWidgetItem(value)
                rank = scores.index(int(row['Score']))
                if rank < 3:
                    item.setBackground(colors[rank])
                self.tableWidget.setItem(i, j, item)
        self.tableWidget.resizeColumnsToContents()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
