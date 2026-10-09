from PyQt5 import QtCore, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        self.vbox = QtWidgets.QVBoxLayout(Form)
        self.calendar = QtWidgets.QCalendarWidget(Form)
        self.vbox.addWidget(self.calendar)
        self.timeEdit = QtWidgets.QTimeEdit(Form)
        self.vbox.addWidget(self.timeEdit)
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.vbox.addWidget(self.lineEdit)
        self.btn = QtWidgets.QPushButton("Добавить", Form)
        self.vbox.addWidget(self.btn)
        self.listWidget = QtWidgets.QListWidget(Form)
        self.vbox.addWidget(self.listWidget)