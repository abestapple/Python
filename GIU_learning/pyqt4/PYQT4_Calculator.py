#__*__ encoding:utf-8 __*__
import sys
from PyQt4 import QtGui,QtCore
from math import *
class Myframe(QtGui.QWidget):
    def __init__(self,parent=None):
        QtGui.QWidget.__init__(self,parent)
        self.setGeometry(200,200,400,400)
        self.setWindowTitle("计算器")
        self.setWindowIcon(QtGui.QIcon('ji.jpg'))
        self.eqal=""
        self.Init()
    def Init(self):
        names="7 8 9 DEL AC 4 5 6 * / 1 2 3 + - 0 % pi e sqrt ^ sin cos tan log ln ( ) . =".split()
        pos = []
        for i in range(1, 7):
            for j in range(5):
                b = (i, j)
                pos.append(b)
        gridbox=QtGui.QGridLayout()
        self.text=QtGui.QLineEdit()
        gridbox.addWidget(self.text,0,0,1,5)
        for i in range(len(names)):
            label=names[i]
            button=QtGui.QPushButton(label,self)
            self.Hand(button,label)
            gridbox.addWidget(button,pos[i][0],pos[i][1])
        self.setLayout(gridbox)
    def Hand(self,button,label):
        items=" DEL AC ="
        if label not in items:
            self.connect(button,QtCore.SIGNAL('clicked()'),self.nomal)
        elif label=="DEL":
            self.connect(button, QtCore.SIGNAL('clicked()'), self.DEL)
        elif label=="AC":
            self.connect(button, QtCore.SIGNAL('clicked()'), self.AC)
        elif label=="=":
            self.connect(button, QtCore.SIGNAL('clicked()'), self.Result)
    def nomal(self):
        source=self.sender()
        label=source.text()
        self.eqal+=label
        self.text.setText(self.eqal)
    def AC(self):
        self.text.clear()
        self.eqal=""
    def DEL(self):
        self.eqal=self.eqal[:-1]
        self.text.setText(self.eqal)
    def Result(self):
        str=self.text.text()
        if '^' in str:
            str=str.replace('^',"**")
        try:
            result=eval(str)
            result=self.eqal+"=%s"%result
            self.text.setText(result)
        except:
            QtGui.QMessageBox.information(self,"警告","检查输入是否有错误!")
app=QtGui.QApplication(sys.argv)
frame=Myframe()
frame.show()
sys.exit(app.exec_())