from PyQt5 import QtCore, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        self.vbox = QtWidgets.QVBoxLayout(Form)
        self.nameEdit = QtWidgets.QLineEdit(Form)
        self.vbox.addWidget(self.nameEdit)
        self.phoneEdit = QtWidgets.QLineEdit(Form)
        self.vbox.addWidget(self.phoneEdit)
        self.btn = QtWidgets.QPushButton("Добавить", Form)
        self.vbox.addWidget(self.btn)
        self.listWidget = QtWidgets.QListWidget(Form)
        self.vbox.addWidget(self.listWidget)