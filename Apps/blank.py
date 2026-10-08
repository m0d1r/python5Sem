import sys
from PyQt6.QtWidgets import *

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("blank")
            
app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()