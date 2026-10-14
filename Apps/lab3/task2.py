import sys
from PyQt5.QtWidgets import QApplication, QWidget, QFileDialog, QMessageBox
from ftask2 import Ui_Form


class Task2(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.browser.setReadOnly(False)
        self.path = None
        self.btnNew.clicked.connect(self.new_file)
        self.btnOpen.clicked.connect(self.open_file)
        self.btnSave.clicked.connect(self.save_file)

    def new_file(self):
        self.browser.clear()
        self.path = None

    def open_file(self):
        path, _ = QFileDialog.getOpenFileName(self, "Открыть", "", "Text (*.txt);;Все (*)")
        if not path:
            return
        try:
            with open(path, "r", encoding="utf-8") as f:
                self.browser.setPlainText(f.read())
            self.path = path
        except OSError as e:
            QMessageBox.critical(self, "Ошибка", str(e))

    def save_file(self):
        if self.path is None:
            path, _ = QFileDialog.getSaveFileName(self, "Сохранить", "", "Text (*.txt)")
            if not path:
                return
        else:
            path = self.path
        with open(path, "w", encoding="utf-8") as f:
            f.write(self.browser.toPlainText())
        self.path = path


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = Task2()
    w.show()
    sys.exit(app.exec_())