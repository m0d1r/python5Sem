from PyQt5 import QtCore, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 500)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.schoolLabel = QtWidgets.QLabel(self.centralwidget)
        self.horizontalLayout.addWidget(self.schoolLabel)
        self.schoolBox = QtWidgets.QComboBox(self.centralwidget)
        self.horizontalLayout.addWidget(self.schoolBox)
        self.classLabel = QtWidgets.QLabel(self.centralwidget)
        self.horizontalLayout.addWidget(self.classLabel)
        self.classBox = QtWidgets.QComboBox(self.centralwidget)
        self.horizontalLayout.addWidget(self.classBox)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget.setColumnCount(3)
        self.verticalLayout.addWidget(self.tableWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Результаты олимпиады"))
        self.schoolLabel.setText(_translate("MainWindow", "Школа"))
        self.classLabel.setText(_translate("MainWindow", "Класс"))
        for index, title in enumerate(("Логин", "ФИО", "Суммарный балл")):
            self.tableWidget.setHorizontalHeaderItem(
                index, QtWidgets.QTableWidgetItem(_translate("MainWindow", title))
            )
