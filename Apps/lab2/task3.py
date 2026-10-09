import sys
from PyQt5.QtWidgets import QApplication, QWidget
from ftask3 import Ui_Form

class Task3(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.btn.clicked.connect(self.add_contact)

    def add_contact(self):
        name = self.nameEdit.text()
        phone = self.phoneEdit.text()
        if name and phone:
            self.listWidget.addItem(f"{name}: {phone}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = Task3()
    w.show()
    sys.exit(app.exec_())