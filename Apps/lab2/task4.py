import sys
from PyQt5.QtWidgets import QApplication, QWidget
from ftask4 import Ui_Form

class Task4(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.btn_start.clicked.connect(self.start_game)
        self.btn_take.clicked.connect(self.player_move)
        self.stones = 0

    def start_game(self):
        self.stones = self.spinBox.value()
        self.lbl_stones.setText(f"Камней: {self.stones}")
        self.btn_take.setEnabled(True)
        self.lbl_status.setText("Ваш ход")

    def player_move(self):
        take = self.takeSpinBox.value()
        if take > self.stones:
            self.lbl_status.setText("Ошибка: столько камней нет")
            return
        self.stones -= take
        self.lbl_stones.setText(f"Камней: {self.stones}")
        if self.stones == 0:
            self.lbl_status.setText("Вы победили!")
            self.btn_take.setEnabled(False)
            return
        self.ai_move()

    def ai_move(self):
        take = self.stones % 4
        if take == 0:
            take = 1
        if take > self.stones:
            take = self.stones
        self.stones -= take
        self.lbl_stones.setText(f"Камней: {self.stones}")
        if self.stones == 0:
            self.lbl_status.setText("ИИ победил!")
            self.btn_take.setEnabled(False)
        else:
            self.lbl_status.setText(f"ИИ взял {take}. Ваш ход")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = Task4()
    w.show()
    sys.exit(app.exec_())