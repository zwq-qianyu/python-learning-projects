#导入wxpython模块
import wx

def opens(event):
	'''打开文件'''
	file = open(filename.GetValue(),'r')
	content.SetValue(file.read())
	file.close()

def save(event):
	'''保存文件'''
	file = open(filename.GetValue(),'w')
	file.write(content.GetValue())
	file.close()

#创建应用程序
app = wx.App()
#创建窗口
win = wx.Frame(None,title="个人记事本",size=(600,400))
#创建组件
opensBtu = wx.Button(win,label="Open",pos=(400,5),size=(90,30))
saveBtu = wx.Button(win,label="Save",pos=(500,5),size=(90,30))
filename = wx.TextCtrl(win,pos=(5,5),size=(380,30))
content = wx.TextCtrl(win,pos=(5,40),size=(590,340),style=wx.TE_MULTILINE|wx.HSCROLL)
#为按钮组件绑定事件
opensBtu.Bind(wx.EVT_BUTTON,opens)
saveBtu.Bind(wx.EVT_BUTTON,save)
#设置可见
win.Show()
#进入应用程序事件主循环
app.MainLoop()