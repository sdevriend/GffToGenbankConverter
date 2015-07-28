

import wx


import sys

from SubPaneel import SubPaneel


class UitvoerScherm(wx.Frame):
    def __init__(self, parent, id=wx.ID_ANY,
                 title='', pos=wx.DefaultPosition, size=(300, 300),
                 style=wx.DEFAULT_FRAME_STYLE & ~(wx.RESIZE_BORDER |
                                                  wx.CLOSE_BOX |
                                                  wx.SYSTEM_MENU),
                 name=''):
        super(UitvoerScherm, self).__init__(parent, id, title, pos, size,
                                           style, name)

        self.threads = []
        PanLabel = wx.StaticText(self, id=-1, label="Script is in uitvoering!")
        font = wx.Font(12, wx.DEFAULT, wx.NORMAL, wx.BOLD)
        PanLabel.SetFont(font)
        self.stopknop = wx.Button(self, -1, label="Stop")
        self.stopknop.Bind(wx.EVT_BUTTON, self.stopbeheer)
        
        vbox = wx.BoxSizer(wx.VERTICAL)
        vbox.Add(PanLabel)
        vbox.Add(self.stopknop)
        
        self.SetSizer(vbox)
        self.SetBackgroundColour("LTGRAY")
        self.Show()
        

        
    def addThread(self, draad):
        self.threads.append(draad)


    def stopbeheer(self, event):
        """for t in self.threads:
            t.terminate()
        alive = True
        while alive:
            if self.threads[0].is_alive():
                if self.threads[1].is_alive():
                    alive = False
            print "I'm still alive!"
        """
        sys.exit()
