# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 220)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btnLoad = QtWidgets.QPushButton(Form)
        self.btnLoad.setObjectName("btnLoad")
        self.horizontalLayout.addWidget(self.btnLoad)
        self.btnSave = QtWidgets.QPushButton(Form)
        self.btnSave.setObjectName("btnSave")
        self.horizontalLayout.addWidget(self.btnSave)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.lblMax = QtWidgets.QLabel(Form)
        self.lblMax.setObjectName("lblMax")
        self.verticalLayout.addWidget(self.lblMax)
        self.lblMin = QtWidgets.QLabel(Form)
        self.lblMin.setObjectName("lblMin")
        self.verticalLayout.addWidget(self.lblMin)
        self.lblAvg = QtWidgets.QLabel(Form)
        self.lblAvg.setObjectName("lblAvg")
        self.verticalLayout.addWidget(self.lblAvg)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Числа из файла"))
        self.btnLoad.setText(_translate("Form", "Загрузить"))
        self.btnSave.setText(_translate("Form", "Сохранить"))
        self.lblMax.setText(_translate("Form", "Максимум: —"))
        self.lblMin.setText(_translate("Form", "Минимум: —"))
        self.lblAvg.setText(_translate("Form", "Среднее: —"))