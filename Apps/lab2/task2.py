import sys
from PyQt5.QtWidgets import QApplication, QWidget
from ftask2 import Ui_Form

class Task2(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.btn.clicked.connect(self.add_event)
        self.events = []

    def add_event(self):
        dt = self.calendar.selectedDate().toString("yyyy-MM-dd")
        tm = self.timeEdit.time().toString("HH:mm")
        txt = self.lineEdit.text()
        if txt:
            self.events.append(f"{dt} {tm} - {txt}")
            self.events.sort()
            self.listWidget.clear()
            self.listWidget.addItems(self.events)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = Task2()
    w.show()
    sys.exit(app.exec_())