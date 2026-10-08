import sys
from PyQt6.QtWidgets import *

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("task2")

        self.button = QPushButton("Вычислить")
        self.button.clicked.connect(self.button_clicked)
        self.input1 = QLineEdit()
        self.input2 = QLineEdit()

        layout = QHBoxLayout()
        layout.addWidget(self.input1)
        layout.addWidget(self.button)
        layout.addWidget(self.input2)

        container = QWidget()
        container.setLayout(layout)

        self.setCentralWidget(container)

    def button_clicked(self):
        self.input2.setText(str(eval(self.input1.text())))
            
app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()