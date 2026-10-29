import random
import sys

from PyQt5.QtCore import QPoint, Qt
from PyQt5.QtGui import QColor, QCursor, QPainter, QPolygon
from PyQt5.QtWidgets import QApplication, QWidget

from ftask3 import Ui_Form


class MainWindow(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.figures = []

    def add_figure(self, kind, point):
        self.figures.append((kind, point, random.randint(25, 80),
                             QColor(random.randint(0, 255), random.randint(0, 255),
                                    random.randint(0, 255))))
        self.update()

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.add_figure('circle', event.pos())
        elif event.button() == Qt.RightButton:
            self.add_figure('square', event.pos())

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Space:
            self.add_figure('triangle', self.mapFromGlobal(QCursor.pos()))

    def paintEvent(self, event):
        painter = QPainter(self)
        for kind, point, size, color in self.figures:
            painter.setBrush(color)
            if kind == 'circle':
                painter.drawEllipse(point, size // 2, size // 2)
            elif kind == 'square':
                painter.drawRect(point.x() - size // 2, point.y() - size // 2, size, size)
            else:
                painter.drawPolygon(QPolygon([
                    QPoint(point.x(), point.y() - size // 2),
                    QPoint(point.x() - size // 2, point.y() + size // 2),
                    QPoint(point.x() + size // 2, point.y() + size // 2)
                ]))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
