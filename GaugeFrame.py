import wx

class GaugeFrame(wx.MiniFrame):
    def __init__(self, parent, title, maximum):
        wx.MiniFrame.__init__(self, parent, title=title, size=(200, 60) )

        #self.bar = wx.Gauge(self, range=maximum)
        self.buCancel = wx.Button(self, label="Cancel")
        self.SetBackgroundColour("LTGRAY")

        siMainV = wx.BoxSizer(wx.VERTICAL)
        #siMainV.Add(self.bar)
        siMainV.Add(self.buCancel, flag=wx.CENTER)
        self.SetSizer(siMainV)
        self.Fit()

        self.Bind(wx.EVT_BUTTON, self.onCancel, self.buCancel)

    #def updateGauge(self, value, message=""):
        #self.bar.SetValue(value)
        #if message!="":
           # self.SetTitle(message)

    def onCancel(self, e):
        self.SetTitle("Cancelling...")
