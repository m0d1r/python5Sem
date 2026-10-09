from PyQt5 import QtCore, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.vbox = QtWidgets.QVBoxLayout(self.centralwidget)
        self.spinBox = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.spinBox.setMaximum(100.0)
        self.spinBox.setValue(80.0)
        self.vbox.addWidget(self.spinBox)
        self.text1 = QtWidgets.QTextEdit(self.centralwidget)
        self.vbox.addWidget(self.text1)
        self.text2 = QtWidgets.QTextEdit(self.centralwidget)
        self.vbox.addWidget(self.text2)
        self.btn = QtWidgets.QPushButton("Проверить", self.centralwidget)
        self.vbox.addWidget(self.btn)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        MainWindow.setStatusBar(self.statusbar)