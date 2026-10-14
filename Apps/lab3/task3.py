import sys
from PyQt5.QtWidgets import QApplication, QWidget, QFileDialog
from PyQt5.QtGui import QPixmap, QImage, QTransform
from ftask3 import Ui_Form


class Task3(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.image = None
        self.btnOpen.clicked.connect(self.open_file)
        self.btnLeft.clicked.connect(lambda: self.rotate(-90))
        self.btnRight.clicked.connect(lambda: self.rotate(90))
        self.comboChannel.currentIndexChanged.connect(self.update_view)

    def open_file(self):
        path, _ = QFileDialog.getOpenFileName(self, "Открыть", "", "Images (*.png *.jpg *.bmp)")
        if not path:
            return
        img = QImage(path)
        if img.isNull():
            return
        size = min(img.width(), img.height())
        img = img.copy(0, 0, size, size)
        self.image = img.convertToFormat(QImage.Format_ARGB32)
        self.update_view()

    def update_view(self):
        if self.image is None:
            return
        img = QImage(self.image)
        mode = self.comboChannel.currentText()
        if mode in ("R", "G", "B"):
            channel = {"R": 0, "G": 1, "B": 2}[mode]
            for y in range(img.height()):
                for x in range(img.width()):
                    px = img.pixel(x, y)
                    r = (px >> 16) & 0xFF
                    g = (px >> 8) & 0xFF
                    b = px & 0xFF
                    keep = [r, g, b][channel]
                    img.setPixel(x, y, (0xFF << 24) | (keep << 16) | (keep << 8) | keep)
        self.lblImage.setPixmap(QPixmap.fromImage(img))

    def rotate(self, angle):
        if self.image is None:
            return
        self.image = self.image.transformed(QTransform().rotate(angle))
        self.update_view()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = Task3()
    w.show()
    sys.exit(app.exec_())