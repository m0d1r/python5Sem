import sys
from PyQt6.QtWidgets import *

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("task3")

        self.label = QLabel("label")
        self.cb_label = QCheckBox("label")
        self.cb_label.setChecked(True)
        self.cb_label.toggled.connect(self.cb_toggled)

        self.input = QLineEdit("input")
        self.cb_input = QCheckBox("input")
        self.cb_input.setChecked(True)
        self.cb_input.toggled.connect(self.cb_toggled)

        self.button = QPushButton("button")
        self.cb_button = QCheckBox("button")
        self.cb_button.setChecked(True)
        self.cb_button.toggled.connect(self.cb_toggled)

        container = QWidget()
        main_layout = QVBoxLayout()

        row1 = QHBoxLayout()
        row1.addWidget(self.cb_label)
        row1.addWidget(self.label)

        row2 = QHBoxLayout()
        row2.addWidget(self.cb_input)
        row2.addWidget(self.input)

        row3 = QHBoxLayout()
        row3.addWidget(self.cb_button)
        row3.addWidget(self.button)

        self.pairs = {
            self.cb_label:  self.label,
            self.cb_input:  self.input,
            self.cb_button: self.button,
        }

        main_layout.addLayout(row1)
        main_layout.addLayout(row2)
        main_layout.addLayout(row3)

        container.setLayout(main_layout)
        self.setCentralWidget(container)

    def cb_toggled(self, checked: bool):
        cb = self.sender()
        widget = self.pairs.get(cb)
        widget.setVisible(checked)





app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()