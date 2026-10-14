# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(500, 500)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.lblImage = QtWidgets.QLabel(Form)
        self.lblImage.setAlignment(QtCore.Qt.AlignCenter)
        self.lblImage.setObjectName("lblImage")
        self.verticalLayout.addWidget(self.lblImage)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.btnOpen = QtWidgets.QPushButton(Form); self.btnOpen.setObjectName("btnOpen")
        self.horizontalLayout.addWidget(self.btnOpen)
        self.btnLeft = QtWidgets.QPushButton(Form); self.btnLeft.setObjectName("btnLeft")
        self.horizontalLayout.addWidget(self.btnLeft)
        self.btnRight = QtWidgets.QPushButton(Form); self.btnRight.setObjectName("btnRight")
        self.horizontalLayout.addWidget(self.btnRight)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.comboChannel = QtWidgets.QComboBox(Form)
        self.comboChannel.setObjectName("comboChannel")
        self.comboChannel.addItem("")
        self.comboChannel.addItem("")
        self.comboChannel.addItem("")
        self.comboChannel.addItem("")
        self.verticalLayout.addWidget(self.comboChannel)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Картинка"))
        self.lblImage.setText(_translate("Form", "Картинка не загружена"))
        self.btnOpen.setText(_translate("Form", "Открыть"))
        self.btnLeft.setText(_translate("Form", "Влево"))
        self.btnRight.setText(_translate("Form", "Вправо"))
        self.comboChannel.setItemText(0, _translate("Form", "Все каналы"))
        self.comboChannel.setItemText(1, _translate("Form", "R"))
        self.comboChannel.setItemText(2, _translate("Form", "G"))
        self.comboChannel.setItemText(3, _translate("Form", "B"))