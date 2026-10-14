import sys
import os
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox
from PyQt5.QtMultimedia import QSound
from ftask7 import Ui_Form


NOTES = ["C", "D", "E", "F", "G", "A", "B"]


class Task7(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        for note in NOTES:
            btn = QPushButton(note)
            btn.setMinimumSize(60, 200)
            btn.clicked.connect(lambda _, n=note: self.play(n))
            self.horizontalLayout.addWidget(btn)

    def play(self, note):
        path = os.path.join("sounds", f"{note}.wav")
        if not os.path.exists(path):
            QMessageBox.warning(self, "Нет файла", f"Не найден {path}")
            return
        QSound.play(path)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = Task7()
    w.show()
    sys.exit(app.exec_())