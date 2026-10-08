import sys
from PyQt6.QtWidgets import *

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("task6")

        self.result = 0
        self.op = None
        self.buffer = ""

        self.display = QLineEdit()
        self.display.setReadOnly(True)

        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+',
            'C',
        ]

        grid = QGridLayout()
        for i, text in enumerate(buttons):
            btn = QPushButton(text)
            btn.clicked.connect(lambda checked=False, t=text: self.press(t))
            grid.addWidget(btn, i // 4, i % 4)

        layout = QVBoxLayout()
        layout.addWidget(self.display)
        layout.addLayout(grid)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def press(self, t):
        if t.isdigit() or t == '.':
            self.buffer += t
            self.display.setText(self.buffer)
        elif t == 'C':
            self.result = 0
            self.op = None
            self.buffer = ""
            self.display.setText("")
        elif t == '=':
            if self.calc():
                self.op = None
                self.buffer = ""
                self.display.setText(str(self.result))
        else:
            if self.calc():
                self.op = t
                self.buffer = ""
                self.display.setText(str(self.result))

    def calc(self):
        if self.buffer == "":
            return True
        x = float(self.buffer)
        if self.op == '+':
            self.result += x
        elif self.op == '-':
            self.result -= x
        elif self.op == '*':
            self.result *= x
        elif self.op == '/':
            if x == 0:
                self.display.setText("Деление на 0")
                self.result = 0
                self.op = None
                self.buffer = ""
                return False
            self.result /= x
        else:
            self.result = x
        return True


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()