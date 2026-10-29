import sys

from PyQt5.QtCore import QEvent, QPoint, Qt
from PyQt5.QtGui import QCursor
from PyQt5.QtWidgets import QApplication, QWidget

from ftask4 import Ui_Form


class MainWindow(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setMinimumSize(self.runButton.size())
        self.setMouseTracking(True)
        self.runButton.setMouseTracking(True)
        self.runButton.installEventFilter(self)

    def move_button(self):
        mouse = self.mapFromGlobal(QCursor.pos())
        button = self.runButton
        if (button.geometry().adjusted(-70, -70, 70, 70).contains(mouse)):
            x_limit = max(0, self.width() - button.width())
            y_limit = max(0, self.height() - button.height())
            corners = (QPoint(0, 0), QPoint(x_limit, 0),
                       QPoint(0, y_limit), QPoint(x_limit, y_limit))
            button.move(max(corners, key=lambda p: (p - mouse).manhattanLength()))

    def mouseMoveEvent(self, event):
        self.move_button()

    def eventFilter(self, obj, event):
        if obj == self.runButton and event.type() in (QEvent.Enter, QEvent.MouseMove, QEvent.MouseButtonPress):
            self.move_button()
            if event.type() == QEvent.MouseButtonPress:
                return True
        return super().eventFilter(obj, event)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
