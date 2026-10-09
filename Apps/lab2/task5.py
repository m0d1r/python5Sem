import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from ftask5 import Ui_MainWindow

class Task5(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.btn.clicked.connect(self.check)

    def check(self):
        t1 = [x.strip() for x in self.text1.toPlainText().split('\n') if x.strip()]
        t2 = [x.strip() for x in self.text2.toPlainText().split('\n') if x.strip()]
        if not t1:
            return
        common = sum(1 for line in t1 if line in t2)
        percent = (common / len(t1)) * 100
        threshold = self.spinBox.value()
        if percent >= threshold:
            self.statusbar.setStyleSheet("color: red;")
            self.statusbar.showMessage(f"Плагиат! Совпадение: {percent:.2f}%")
        else:
            self.statusbar.setStyleSheet("color: green;")
            self.statusbar.showMessage(f"Оригинал. Совпадение: {percent:.2f}%")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = Task5()
    w.show()
    sys.exit(app.exec_())