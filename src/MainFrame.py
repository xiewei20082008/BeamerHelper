#coding=utf8
import sys
from PyQt4 import QtCore, QtGui
from ui import Ui_MainWindow
import downloader
import thread

def mystr(string):
    return string.decode('u8')

class MyForm(QtGui.QMainWindow):
    def showMessage(self,string):
        self.ui.messageTextbox.setText(string)
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)     
        #here start
        downloader.fileLabel = self.ui.fileLabel
        downloader.nowSizeLabel = self.ui.nowSizeLabel
        downloader.totalSizeLabel = self.ui.totalSizeLabel
        downloader.messageTextbox = self.ui.messageTextbox
        #pass para
        self.connect(self.ui.aButton,QtCore.SIGNAL('clicked()'),self.aButton_clicked)
        self.connect(self.ui.bButton,QtCore.SIGNAL('clicked()'),self.bButton_clicked)
        self.connect(self.ui.aAfternoonButton,QtCore.SIGNAL('clicked()'),self.aAfternoonButton_clicked)
        self.connect(self.ui.bAfternoonButton,QtCore.SIGNAL('clicked()'),self.bAfternoonButton_clicked)
        self.connect(self.ui.downloadPercentButton,QtCore.SIGNAL('clicked()'),self.downloadPercentButton_clicked)
        self.connect(self.ui.nextButton,QtCore.SIGNAL('clicked()'),self.nextButton_clicked)
        #event
    def aButton_clicked(self):
        thread.start_new_thread(downloader.main,(1,True))
    def bButton_clicked(self):
        thread.start_new_thread(downloader.main,(0,True))
    def aAfternoonButton_clicked(self):
        thread.start_new_thread(downloader.main,(1,False))
    def bAfternoonButton_clicked(self):
        thread.start_new_thread(downloader.main,(0,False))
    def nextButton_clicked(self):
        downloader.goNext = True
    def downloadPercentButton_clicked(self):
        downloader.refreshPercent()

app = QtGui.QApplication(sys.argv)
myapp = MyForm()
myapp.show()
sys.exit(app.exec_())

