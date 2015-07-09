"""
Sebastiaan 8-7-15 Maken van invoerscherm.

De class maakt het invoerscherm waar de gebruiker een gff file kan
invoeren.
"""

import wx
import os

from SubPaneel import SubPaneel
from KnoppenPaneel import KnoppenPaneel

class InvoerScherm(wx.Frame):

    def __init__(self, parent, id=wx.ID_ANY,
                 title='', pos=wx.DefaultPosition, size=(0, 0),
                 style=wx.DEFAULT_FRAME_STYLE & ~(wx.RESIZE_BORDER |
                                                  wx.CLOSE_BOX |
                                                  wx.SYSTEM_MENU),
                 name=''):
        super(InvoerScherm, self).__init__(parent, id, title, pos, size,
                                           style, name)
        self.Mainpaneel = SubPaneel(self)
        self.middenstuk()
        self.Vbox = wx.BoxSizer(wx.VERTICAL)
        self.Vbox.Add(self.Hbox, 17, wx.ALL | wx.EXPAND)
        self.Knoppen = KnoppenPaneel(self)
        self.Vbox.Add(self.Knoppen, 3, wx.ALL | wx.EXPAND)
        self.SetSizer(self.Vbox)
        self.Knoppen.SetBackgroundColour((0, 255, 0))
        self.Show()

    def middenstuk(self):
        
        
        PanRechts = SubPaneel(self)
        PanRechts.SetBackgroundColour((0, 0, 255))
        self.Hbox = wx.BoxSizer(wx.HORIZONTAL)
        self.Hbox.Add(self.maakLinks(), 1, wx.ALL | wx.EXPAND)
        self.Hbox.Add(PanRechts, 1, wx.ALL | wx.EXPAND)


    def maakLinks(self):
        PanLinks = SubPaneel(self)
        PanLinks.SetBackgroundColour((255, 0, 0 ))
        vbox = wx.BoxSizer(wx.VERTICAL)
        self.bladerknop = wx.Button(PanLinks, -1, label="bladeren")
        self.bladerknop.Bind(wx.EVT_BUTTON, self.browsegff)
        vbox.Add(self.bladerknop, 0)
        PanLinks.SetSizer(vbox)
        return PanLinks

    def browsegff(self, event):
        print "blader naar file"
        wildcard = """gff(*.gff)|*.gff"""
        self.blad = wx.FileDialog(self, "Bladeren", os.getcwd(), "",
                                  wildcard, wx.OPEN)
        if self.blad.ShowModal() == wx.ID_OK:
            bestandsnaam = self.blad.GetPath()
            print bestandsnaam