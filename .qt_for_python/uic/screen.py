# Form implementation generated from reading ui file 'c:\Users\ct67ca\Desktop\Abe\virf\menu\screen.ui'
#
# Created by: PyQt6 UI code generator 6.3.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(700, 541)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.hangGame = QtWidgets.QPushButton(self.centralwidget)
        self.hangGame.setGeometry(QtCore.QRect(10, 20, 200, 200))
        self.hangGame.setStyleSheet("background-image: url(:/menu/hanggame.jpg);")
        self.hangGame.setText("")
        self.hangGame.setObjectName("hangGame")
        self.ticTacToe = QtWidgets.QPushButton(self.centralwidget)
        self.ticTacToe.setGeometry(QtCore.QRect(220, 20, 200, 200))
        self.ticTacToe.setStyleSheet("background-image: url(:/menu/tictactoe.jpg);")
        self.ticTacToe.setText("")
        self.ticTacToe.setObjectName("ticTacToe")
        self.joKenPo = QtWidgets.QPushButton(self.centralwidget)
        self.joKenPo.setGeometry(QtCore.QRect(10, 230, 200, 200))
        self.joKenPo.setStyleSheet("background-image: url(:/menu/jokenpo.jpg);")
        self.joKenPo.setText("")
        self.joKenPo.setObjectName("joKenPo")
        self.github = QtWidgets.QPushButton(self.centralwidget)
        self.github.setGeometry(QtCore.QRect(220, 230, 200, 200))
        self.github.setStyleSheet("background-image: url(:/menu/github.jpg);")
        self.github.setText("")
        self.github.setObjectName("github")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(450, 20, 191, 201))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/menu/virf-logo.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))