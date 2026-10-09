import sys
from PyQt5.QtWidgets import QApplication, QWidget
from ftask1 import Ui_Form

class Task1(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.btn.clicked.connect(self.draw)

    def draw(self):
        c1 = "Красный" if self.r11.isChecked() else "Зелёный" if self.r12.isChecked() else "Белый"
        c2 = "Красный" if self.r21.isChecked() else "Зелёный" if self.r22.isChecked() else "Белый"
        c3 = "Красный" if self.r31.isChecked() else "Зелёный" if self.r32.isChecked() else "Белый"
        self.lbl.setText(f"{c1}, {c2}, {c3}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = Task1()
    w.show()
    sys.exit(app.exec_())