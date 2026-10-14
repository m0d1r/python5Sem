# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(450, 500)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.canvas = QtWidgets.QWidget(Form)
        self.canvas.setMinimumSize(QtCore.QSize(400, 400))
        self.canvas.setObjectName("canvas")
        self.verticalLayout.addWidget(self.canvas)
        self.btnColor = QtWidgets.QPushButton(Form)
        self.btnColor.setObjectName("btnColor")
        self.verticalLayout.addWidget(self.btnColor)
        self.sliderScale = QtWidgets.QSlider(Form)
        self.sliderScale.setOrientation(QtCore.Qt.Horizontal)
        self.sliderScale.setMinimum(50); self.sliderScale.setMaximum(300)
        self.sliderScale.setValue(100)
        self.sliderScale.setObjectName("sliderScale")
        self.verticalLayout.addWidget(self.sliderScale)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Смайлик"))
        self.btnColor.setText(_translate("Form", "Цвет"))