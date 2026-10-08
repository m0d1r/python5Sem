import sys
from PyQt6.QtWidgets import *

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("task1")

        self.button = QPushButton("=>")
        self.button.clicked.connect(self.button_clicked)
        self.input1 = QLineEdit()
        self.input2 = QLineEdit()

        self.button_state = True

        layout = QHBoxLayout()
        layout.addWidget(self.input1)
        layout.addWidget(self.button)
        layout.addWidget(self.input2)

        container = QWidget()
        container.setLayout(layout)

        self.setCentralWidget(container)

    def button_clicked(self):
        if self.button_state:
            self.input2.setText(self.input1.text())
            self.input1.setText("")
            self.button.setText("<=")
        else:
            self.input1.setText(self.input2.text())
            self.input2.setText("")
            self.button.setText("=>")
        self.button_state = not self.button_state
            




app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()