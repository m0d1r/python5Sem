# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(650, 700)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.canvas = QtWidgets.QWidget(Form)
        self.canvas.setMinimumSize(QtCore.QSize(600, 600))
        self.canvas.setObjectName("canvas")
        self.verticalLayout.addWidget(self.canvas)
        self.lblInfo = QtWidgets.QLabel(Form)
        self.lblInfo.setObjectName("lblInfo")
        self.verticalLayout.addWidget(self.lblInfo)
        self.btnOpen = QtWidgets.QPushButton(Form)
        self.btnOpen.setObjectName("btnOpen")
        self.verticalLayout.addWidget(self.btnOpen)
        self.sliderStep = QtWidgets.QSlider(Form)
        self.sliderStep.setOrientation(QtCore.Qt.Horizontal)
        self.sliderStep.setMinimum(0)
        self.sliderStep.setMaximum(0)
        self.sliderStep.setObjectName("sliderStep")
        self.verticalLayout.addWidget(self.sliderStep)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "L-система"))
        self.lblInfo.setText(_translate("Form", "Файл не загружен"))
        self.btnOpen.setText(_translate("Form", "Открыть"))