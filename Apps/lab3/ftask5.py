# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(450, 350)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.lblFlag = QtWidgets.QLabel(Form)
        self.lblFlag.setAlignment(QtCore.Qt.AlignCenter)
        self.lblFlag.setObjectName("lblFlag")
        self.verticalLayout.addWidget(self.lblFlag)
        self.btnMake = QtWidgets.QPushButton(Form)
        self.btnMake.setObjectName("btnMake")
        self.verticalLayout.addWidget(self.btnMake)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Флаг"))
        self.btnMake.setText(_translate("Form", "Создать флаг"))