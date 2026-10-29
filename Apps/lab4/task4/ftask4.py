from PyQt5 import QtCore, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(750, 520)
        self.runButton = QtWidgets.QPushButton(Form)
        self.runButton.setObjectName('runButton')
        self.runButton.setGeometry(QtCore.QRect(330, 230, 110, 40))
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", 'Убегающая кнопка'))
        self.runButton.setText(_translate("Form", 'Кнопка'))
