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
        self.btnOpen = QtWidgets.QPushButton(Form); self.btnOpen.setObjectName("btnOpen")
        self.verticalLayout.addWidget(self.btnOpen)
        self.sliderAlpha = QtWidgets.QSlider(Form)
        self.sliderAlpha.setOrientation(QtCore.Qt.Horizontal)
        self.sliderAlpha.setMinimum(0); self.sliderAlpha.setMaximum(100)
        self.sliderAlpha.setValue(100)
        self.sliderAlpha.setObjectName("sliderAlpha")
        self.verticalLayout.addWidget(self.sliderAlpha)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Прозрачность"))
        self.lblImage.setText(_translate("Form", "Картинка не загружена"))
        self.btnOpen.setText(_translate("Form", "Открыть"))