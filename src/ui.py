# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created: Tue Jan 20 11:32:47 2015
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(460, 280)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.textEdit1 = QtGui.QTextEdit(self.centralwidget)
        self.textEdit1.setGeometry(QtCore.QRect(10, 110, 441, 141))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.textEdit1.setFont(font)
        self.textEdit1.setObjectName(_fromUtf8("textEdit1"))
        self.textEdit2 = QtGui.QTextEdit(self.centralwidget)
        self.textEdit2.setGeometry(QtCore.QRect(140, 10, 311, 31))
        self.textEdit2.setObjectName(_fromUtf8("textEdit2"))
        self.newlineB = QtGui.QPushButton(self.centralwidget)
        self.newlineB.setGeometry(QtCore.QRect(10, 30, 61, 23))
        self.newlineB.setObjectName(_fromUtf8("newlineB"))
        self.itemB = QtGui.QPushButton(self.centralwidget)
        self.itemB.setGeometry(QtCore.QRect(70, 30, 61, 23))
        self.itemB.setObjectName(_fromUtf8("itemB"))
        self.newFrameB = QtGui.QPushButton(self.centralwidget)
        self.newFrameB.setGeometry(QtCore.QRect(10, 0, 61, 23))
        self.newFrameB.setObjectName(_fromUtf8("newFrameB"))
        self.newPicB = QtGui.QPushButton(self.centralwidget)
        self.newPicB.setGeometry(QtCore.QRect(70, 0, 61, 23))
        self.newPicB.setObjectName(_fromUtf8("newPicB"))
        self.blockB = QtGui.QPushButton(self.centralwidget)
        self.blockB.setGeometry(QtCore.QRect(10, 60, 61, 23))
        self.blockB.setObjectName(_fromUtf8("blockB"))
        self.textEdit3 = QtGui.QTextEdit(self.centralwidget)
        self.textEdit3.setGeometry(QtCore.QRect(140, 50, 311, 31))
        self.textEdit3.setObjectName(_fromUtf8("textEdit3"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 460, 17))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuTEX_helper = QtGui.QMenu(self.menubar)
        self.menuTEX_helper.setObjectName(_fromUtf8("menuTEX_helper"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuTEX_helper.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.newlineB.setText(_translate("MainWindow", "newline", None))
        self.itemB.setText(_translate("MainWindow", "item", None))
        self.newFrameB.setText(_translate("MainWindow", "newFrame", None))
        self.newPicB.setText(_translate("MainWindow", "newPic", None))
        self.blockB.setText(_translate("MainWindow", "block", None))
        self.menuTEX_helper.setTitle(_translate("MainWindow", "TEX_helper", None))

