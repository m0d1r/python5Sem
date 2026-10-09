from PyQt5 import QtCore, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        self.vbox = QtWidgets.QVBoxLayout(Form)
        self.lbl_stones = QtWidgets.QLabel("Камней: 0", Form)
        self.vbox.addWidget(self.lbl_stones)
        self.spinBox = QtWidgets.QSpinBox(Form)
        self.spinBox.setMinimum(1)
        self.spinBox.setMaximum(100)
        self.vbox.addWidget(self.spinBox)
        self.btn_start = QtWidgets.QPushButton("Начать игру", Form)
        self.vbox.addWidget(self.btn_start)
        self.takeSpinBox = QtWidgets.QSpinBox(Form)
        self.takeSpinBox.setMinimum(1)
        self.takeSpinBox.setMaximum(3)
        self.vbox.addWidget(self.takeSpinBox)
        self.btn_take = QtWidgets.QPushButton("Взять", Form)
        self.btn_take.setEnabled(False)
        self.vbox.addWidget(self.btn_take)
        self.lbl_status = QtWidgets.QLabel(Form)
        self.vbox.addWidget(self.lbl_status)