import sys
from PyQt5.QtWidgets import QApplication, QWidget, QColorDialog
from PyQt5.QtGui import QPainter, QColor, QPen
from PyQt5.QtCore import Qt
from ftask6 import Ui_Form


class SmileWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.color = QColor(255, 220, 0)
        self.scale = 1.0
        self.setMinimumSize(400, 400)

    def paintEvent(self, event):
        p = QPainter(self)
        p.setRenderHint(QPainter.Antialiasing)
        p.translate(self.width() / 2, self.height() / 2)
        p.scale(self.scale, self.scale)

        p.setBrush(self.color)
        p.setPen(QPen(Qt.black, 3))
        p.drawEllipse(-100, -100, 200, 200)

        p.setBrush(Qt.black)
        p.drawEllipse(-45, -40, 20, 20)
        p.drawEllipse(25, -40, 20, 20)

        p.setPen(QPen(Qt.black, 4))
        p.setBrush(Qt.NoBrush)
        p.drawArc(-60, 10, 120, 70, 0, -180)


class Task6(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.smile = SmileWidget(self)
        self.verticalLayout.replaceWidget(self.canvas, self.smile)
        self.canvas.deleteLater()

        self.btnColor.clicked.connect(self.pick_color)
        self.sliderScale.valueChanged.connect(self.change_scale)

    def pick_color(self):
        c = QColorDialog.getColor(self.smile.color, self, "Цвет смайлика")
        if c.isValid():
            self.smile.color = c
            self.smile.update()

    def change_scale(self, v):
        self.smile.scale = v / 100.0
        self.smile.update()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = Task6()
    w.show()
    sys.exit(app.exec_())