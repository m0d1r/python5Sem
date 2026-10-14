# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(500, 400)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.btnNew = QtWidgets.QPushButton(Form)
        self.btnNew.setObjectName("btnNew")
        self.horizontalLayout.addWidget(self.btnNew)
        self.btnOpen = QtWidgets.QPushButton(Form)
        self.btnOpen.setObjectName("btnOpen")
        self.horizontalLayout.addWidget(self.btnOpen)
        self.btnSave = QtWidgets.QPushButton(Form)
        self.btnSave.setObjectName("btnSave")
        self.horizontalLayout.addWidget(self.btnSave)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.browser = QtWidgets.QTextBrowser(Form)
        self.browser.setObjectName("browser")
        self.verticalLayout.addWidget(self.browser)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Редактор"))
        self.btnNew.setText(_translate("Form", "Новый"))
        self.btnOpen.setText(_translate("Form", "Открыть"))
        self.btnSave.setText(_translate("Form", "Сохранить"))