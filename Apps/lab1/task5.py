import sys
from PyQt6.QtWidgets import *

MENU = {
    'Пицца': 500,
    'Суши': 350,
    'Чай': 100,
}

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("task5")

        self.checks = {}
        self.spins = {}

        grid = QGridLayout()

        for i, name in enumerate(MENU):
            cb = QCheckBox(name)
            sp = QSpinBox()
            sp.setValue(1)
            self.checks[name] = cb
            self.spins[name] = sp
            grid.addWidget(cb, i, 0)
            grid.addWidget(sp, i, 1)

        self.button = QPushButton("Заказать")
        self.button.clicked.connect(self.make_order)

        self.output = QPlainTextEdit()

        layout = QVBoxLayout()
        layout.addLayout(grid)
        layout.addWidget(self.button)
        layout.addWidget(self.output)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def make_order(self):
        text = ""
        total = 0
        for name, price in MENU.items():
            if self.checks[name].isChecked():
                qty = self.spins[name].value()
                cost = price * qty
                total += cost
                text += f"{name} | {qty} шт. | {cost} руб.\n"
        text += f"\nИтого: {total} руб."
        self.output.setPlainText(text)


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()