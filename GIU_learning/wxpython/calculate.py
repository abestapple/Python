#__*__ encoding:utf-8 __*__
import wx
from math import *
class Myframe(wx.Frame):
    def __init__(self,parent,title,size):
        wx.Frame.__init__(self,parent,title=title,size=size)
        panel=wx.Panel(self)
        panel.SetBackgroundColour("blue")
        self.result=wx.TextCtrl(panel)
        self.buttondata="7 8 9 DEL AC 4 5 6 * / 1 2 3 + - 0 % pi e sqrt ^ sin cos tan log ln ( ) . =".split()
        self.vbox=wx.BoxSizer(wx.VERTICAL)
        gridbox=wx.GridSizer(6,5,5,5)
        self.eqal=""
        N=len(self.buttondata)
        for i in range(N):
            label=self.buttondata[i]
            button_item=wx.Button(panel,i,label=label,size=(63,55))
            self.creathand(button_item,label)
            gridbox.Add(button_item,0,0)
        self.vbox.Add(self.result, 1,wx.EXPAND)
        self.vbox.Add(gridbox,5, wx.EXPAND)
        panel.SetSizer(self.vbox)
        self.Show()
    def creathand(self,button,label):
        items="DEL AC ="
        if label not in items:
            self.Bind(wx.EVT_BUTTON,self.Nomal,button)
        elif label=="DEL":
            self.Bind(wx.EVT_BUTTON,self.dell,button)
        elif label=="AC":
            self.Bind(wx.EVT_BUTTON,self.AC,button)
        else:
            self.Bind(wx.EVT_BUTTON,self.sqal,button)
    def Nomal(self,event):
        but_event=event.GetEventObject()
        label=but_event.GetLabel()
        self.eqal+=label
        self.result.SetValue(self.eqal)
    def dell(self,event):
        self.eqal=self.eqal[:-1]
        self.result.SetValue(self.eqal)
    def AC(self,event):
        #self.result.SetValue(" ")
        self.result.Clear()
        self.eqal=""
    def sqal(self,event):
        str = self.result.GetValue()
        if "^" in str:
            str=str.replace("^","**")
        try:
            result=eval(str)
            p_str=self.eqal+"="+"%s"%result
        except:
            diag=wx.MessageDialog(self,"请正确输入！","错误",wx.OK)
            diag.ShowModal()
            diag.Destroy()
        else:
            self.result.SetValue(p_str)
app=wx.App()
frame=Myframe(None,"计算器",(350,480))
app.MainLoop()