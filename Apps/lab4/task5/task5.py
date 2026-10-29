import sys
from pathlib import Path

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QWidget

from ftask5 import Ui_Form


class MainWindow(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setMinimumSize(self.ufoLabel.size())
        image_path = Path(getattr(sys, '_MEIPASS', Path(__file__).parent)) / 'ufo.png'
        self.ufoLabel.setPixmap(QPixmap(str(image_path)))

    def keyPressEvent(self, event):
        step = 20
        dx, dy = {
            Qt.Key_Left: (-step, 0), Qt.Key_Right: (step, 0),
            Qt.Key_Up: (0, -step), Qt.Key_Down: (0, step)
        }.get(event.key(), (0, 0))
        if not (dx or dy):
            return
        x = self.ufoLabel.x() + dx
        y = self.ufoLabel.y() + dy
        max_x = self.width() - self.ufoLabel.width()
        max_y = self.height() - self.ufoLabel.height()
        x = max_x if x < 0 else 0 if x > max_x else x
        y = max_y if y < 0 else 0 if y > max_y else y
        self.ufoLabel.move(x, y)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
