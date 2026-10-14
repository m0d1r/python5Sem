import sys
from PyQt5.QtWidgets import QApplication, QWidget, QFileDialog
from PyQt5.QtGui import QPixmap, QImage
from ftask4 import Ui_Form


class Task4(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.image = None
        self.btnOpen.clicked.connect(self.open_file)
        self.sliderAlpha.valueChanged.connect(self.update_alpha)

    def open_file(self):
        path, _ = QFileDialog.getOpenFileName(self, "Открыть", "", "Images (*.png *.jpg *.bmp)")
        if not path:
            return
        img = QImage(path)
        if img.isNull():
            return
        self.image = img.convertToFormat(QImage.Format_ARGB32)
        self.update_alpha()

    def update_alpha(self):
        if self.image is None:
            return
        alpha = int(255 * self.sliderAlpha.value() / 100)
        img = QImage(self.image)
        for y in range(img.height()):
            for x in range(img.width()):
                px = img.pixel(x, y)
                img.setPixel(x, y, (alpha << 24) | (px & 0x00FFFFFF))
        self.lblImage.setPixmap(QPixmap.fromImage(img))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = Task4()
    w.show()
    sys.exit(app.exec_())