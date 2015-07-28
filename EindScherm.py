
import wx

class EindScherm(wx.Frame):
    def __init__(self, parent, id=wx.ID_ANY,
                 title='', pos=wx.DefaultPosition, size=(0, 0),
                 style=wx.DEFAULT_FRAME_STYLE & ~(wx.RESIZE_BORDER |
                                                  wx.CLOSE_BOX |
                                                  wx.SYSTEM_MENU),
                 name=''):
        super(EindScherm, self).__init__(parent, id, title, pos, size,
                                           style, name)
        PanLabel = wx.StaticText(self, id=-1, label="Conversie is klaar")
        font = wx.Font(12, wx.DEFAULT, wx.NORMAL, wx.BOLD)
        PanLabel.SetFont(font)
        

        self.SetBackgroundColour("LTGRAY")
        self.Show()
