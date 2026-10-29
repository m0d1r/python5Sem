from PyQt5 import QtCore, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(750, 520)
        self.ufoLabel = QtWidgets.QLabel(Form)
        self.ufoLabel.setObjectName('ufoLabel')
        self.ufoLabel.setGeometry(QtCore.QRect(330, 220, 72, 48))
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", 'Управление НЛО'))
        self.ufoLabel.setText(_translate("Form", ''))
