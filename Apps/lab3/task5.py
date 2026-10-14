import sys
import random
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog
from PyQt5.QtGui import QPixmap, QPainter, QColor
from ftask5 import Ui_Form


class Task5(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.btnMake.clicked.connect(self.make_flag)

    def make_flag(self):
        n, ok = QInputDialog.getInt(self, "Цвета", "Число цветов:", 5, 2, 20)
        if not ok:
            return
        w, h = 400, 300
        pix = QPixmap(w, h)
        painter = QPainter(pix)
        stripe_h = h / n
        for i in range(n):
            color = QColor(random.randint(0, 255),
                           random.randint(0, 255),
                           random.randint(0, 255))
            painter.fillRect(0, int(i * stripe_h), w, int(stripe_h) + 1, color)
        painter.end()
        self.lblFlag.setPixmap(pix)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = Task5()
    w.show()
    sys.exit(app.exec_())