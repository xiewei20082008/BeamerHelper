#coding=utf8
import sys
from PyQt4 import QtCore, QtGui
from ui import Ui_MainWindow
import os.path
import win32clipboard as w  
import win32con 


def setClip(aString):  
    w.OpenClipboard()  
    w.EmptyClipboard()  
    w.SetClipboardData(win32con.CF_UNICODETEXT, aString)  
    w.CloseClipboard()
def getClip():
    w.OpenClipboard()
    d = w.GetClipboardData(win32con.CF_TEXT)
    w.CloseClipboard()
    return d

class MyForm(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)  
        #value
        self.editor1 = self.ui.textEdit1
        self.editor2 = self.ui.textEdit2
        self.editor3 = self.ui.textEdit3
        #slot
        self.connect(self.ui.newlineB,QtCore.SIGNAL('clicked()'),self.newline_clicked)
        self.connect(self.ui.itemB,QtCore.SIGNAL('clicked()'),self.item_clicked)
        self.connect(self.ui.newFrameB,QtCore.SIGNAL('clicked()'),self.newFrameB_clicked)
        self.connect(self.ui.newPicB,QtCore.SIGNAL('clicked()'),self.newPicB_clicked)
        self.connect(self.ui.blockB,QtCore.SIGNAL('clicked()'),self.blockB_clicked)
        #
    def blockB_clicked(self):
        res = u'\\begin{block}{'
        res+= self.editor3.toPlainText();
        res+= u'}\n\n';
        res+= u'\\end{block}\n'
        setClip(res)
    def newPicB_clicked(self):
        res = u'\\begin{center}\n'
        res+= u'\t\\includegraphics[height=6cm]{1.jpg}\n'
        res+= u'\end{center}'
        setClip(res)
    def newline_clicked(self):
        setClip(u'\\newline\\newline')
    def newFrameB_clicked(self):
        res = '\\begin{frame}\n'
        res+='\\frametitle{'
        res+=self.editor2.toPlainText()
        res+='}\n'
        res+='\end{frame}\n'
        setClip(res)
    def item_clicked(self):
        str = self.editor1.toPlainText()
        res = '\\begin{itemize}\n'
        s = str.split('\n')
        for i in s:
            res+='\t\\item '+i+'\n'
        res+= '\\end{itemize}\n'
        #print res
        setClip(res)
        
app = QtGui.QApplication(sys.argv)
myapp = MyForm()
myapp.show()
sys.exit(app.exec_())
