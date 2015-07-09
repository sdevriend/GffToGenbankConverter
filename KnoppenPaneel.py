"""
Sebastiaan de Vriend 8-7-15 Knoppen paneel opmaken

De class maakt een knoppen paneel voor 3 knoppen. Minder knoppen
kunnen ook gemaakt worden.
"""

import wx
import sys
from SubPaneel import SubPaneel


class KnoppenPaneel(wx.Panel):

    def __init__(self, parent, id=wx.ID_ANY, size=wx.DefaultSize):
        self.KnopPaneel = wx.Panel.__init__(self, parent, id, size=size)
        self.HBox = wx.BoxSizer(wx.HORIZONTAL)
        self.GoKnop = wx.Button(self, id=-1, label="Volgende")
        self.HelpKnop = wx.Button(self, id=-1, label="Help")
        self.StopKnop = wx.Button(self, id=-1, label="Stop")
        self.HBox.Add(self.TussenPan(), 1, wx.ALL | wx.EXPAND)
        self.HBox.Add(self.StopKnop, 1, wx.ALL |wx.ALIGN_CENTER)
        self.HBox.Add(self.TussenPan(), 1, wx.ALL | wx.EXPAND)
        self.HBox.Add(self.HelpKnop, 1, wx.ALL |wx.ALIGN_CENTER)
        self.HBox.Add(self.TussenPan(), 1, wx.ALL | wx.EXPAND)
        self.HBox.Add(self.GoKnop, 1, wx.ALL |wx.ALIGN_CENTER )
        self.HBox.Add(self.TussenPan(), 1, wx.ALL | wx.EXPAND)
        self.SetSizer(self.HBox)
        self.StopKnop.Bind(wx.EVT_BUTTON, self.Stoppen)


    def Stoppen(self, Event):
        sys.exit()


    def TussenPan(self):
        return SubPaneel(self)
        
        
        
