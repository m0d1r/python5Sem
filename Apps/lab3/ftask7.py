# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(500, 250)
        self.horizontalLayout = QtWidgets.QHBoxLayout(Form)
        for name, text in [("btnC", "C"), ("btnD", "D"), ("btnE", "E"),
                           ("btnF", "F"), ("btnG", "G"), ("btnA", "A"), ("btnB", "B")]:
            btn = QtWidgets.QPushButton(Form)
            btn.setMinimumSize(QtCore.QSize(60, 200))
            btn.setObjectName(name)
            self.horizontalLayout.addWidget(btn)
            setattr(self, name, btn)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Фортепиано"))
        for name, text in [("btnC", "C"), ("btnD", "D"), ("btnE", "E"),
                           ("btnF", "F"), ("btnG", "G"), ("btnA", "A"), ("btnB", "B")]:
            getattr(self, name).setText(_translate("Form", text))