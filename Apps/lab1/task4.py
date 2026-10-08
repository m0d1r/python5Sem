import sys
from PyQt6.QtWidgets import *

MORSE = {
    'A': '.-',   'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.',  'H': '....', 'I': '..',   'J': '.---', 'K': '-.-',  'L': '.-..', 'M': '--',   'N': '-.',   
    'O': '---',  'P': '.--.', 'Q': '--.-', 'R': '.-.',  'S': '...',  'T': '-', 'U': '..-',  'V': '...-', 'W': '.--',  'X': '-..-', 'Y': '-.--', 'Z': '--..'
}

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("task4")

        self.input = QLineEdit()

        grid = QGridLayout()
        letters = list(MORSE.keys())

        for i, letter in enumerate(letters):
            btn = QPushButton(letter)
            btn.clicked.connect(
                lambda checked=False, l=letter: self.add_morse(l)
            )
            row = i // 7
            col = i % 7
            grid.addWidget(btn, row, col)

        layout = QVBoxLayout()
        layout.addWidget(self.input)
        layout.addLayout(grid)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def add_morse(self, letter):
        self.input.setText(self.input.text() + MORSE[letter] + ' ')


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()