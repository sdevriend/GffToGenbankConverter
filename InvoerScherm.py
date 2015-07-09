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
    """
    De class is niet helemaal af!

    De class toont 3 panelen voor bladeren naar een bestand.
    Dit zit in middenstuk
    in links wordt het bladeren correct toegevoegt.
    """
    def __init__(self, parent, id=wx.ID_ANY,
                 title='', pos=wx.DefaultPosition, size=(0, 0),
                 style=wx.DEFAULT_FRAME_STYLE & ~(wx.RESIZE_BORDER |
                                                  wx.CLOSE_BOX |
                                                  wx.SYSTEM_MENU),
                 name=''):
        super(InvoerScherm, self).__init__(parent, id, title, pos, size,
                                           style, name)
        self.bestandsnaam = ""
        self.middenstuk()
        self.Vbox = wx.BoxSizer(wx.VERTICAL)
        self.Vbox.Add(self.Hbox, 17, wx.ALL | wx.EXPAND)
        self.Knoppen = KnoppenPaneel(self)
        self.Vbox.Add(self.Knoppen, 3, wx.ALL | wx.EXPAND)
        
        self.Knoppen.SetBackgroundColour((0, 255, 0))
        
        self.SetSizer(self.Vbox)
        self.SetBackgroundColour(None)
        self.Show()

    def middenstuk(self):
        
        
        PanMid = SubPaneel(self, style=wx.SUNKEN_BORDER)
        PanMid.SetBackgroundColour((0, 0, 255))
        PanRechts = SubPaneel(self, style=wx.SUNKEN_BORDER)
        PanRechts.SetBackgroundColour((125, 0, 250))
        self.Hbox = wx.BoxSizer(wx.HORIZONTAL)
        self.Hbox.Add(self.maakLinks(), 1, wx.ALL | wx.EXPAND, 10)
        self.Hbox.Add(PanMid, 1, wx.ALL | wx.EXPAND, 10, 0)
        self.Hbox.Add(PanRechts, 1, wx.ALL | wx.EXPAND, 10)


    def maakLinks(self):
        PanLinks = SubPaneel(self, style=wx.SUNKEN_BORDER)
        PanLinks.SetBackgroundColour((255, 0, 0 ))
        self.gffnaam = wx.StaticText(PanLinks, id=-1, label="Geen bestand" +
                                     "geselecteerd")
        vbox = wx.BoxSizer(wx.VERTICAL)
        self.bladerknop = wx.Button(PanLinks, -1, label="bladeren")
        self.bladerknop.Bind(wx.EVT_BUTTON, self.browsegff)
        vbox.Add(self.bladerknop, 0)
        vbox.Add(self.gffnaam, 0)
        PanLinks.SetSizer(vbox)
        return PanLinks

    def browsegff(self, event):
        """
        De methode kan bladeren naar een bestand en het bestandsnaam
        daarvan opslaan in een variable.
        """
        print "blader naar file"
        wildcard = """gff(*.gff)|*.gff"""
        self.blad = wx.FileDialog(self, "Bladeren", os.getcwd(), "",
                                  wildcard, wx.OPEN)
        if self.blad.ShowModal() == wx.ID_OK:
            self.bestandsnaam = self.blad.GetPath()
            self.setgffnaam()
            
    def setgffnaam(self):
        naam = self.bestandsnaam.split("\\")
        self.gffnaam.SetLabel("Geselecteerd bestand: \n" + naam[len(naam)-1])
