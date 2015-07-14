"""
Sebastiaan 8-7-15 Maken van invoerscherm.

De class maakt het invoerscherm waar de gebruiker een gff file kan
invoeren.
"""

import wx
#import wx.lib.stattext as ST

import os

from SubPaneel import SubPaneel
from KnoppenPaneel import KnoppenPaneel
from Bestandspaneel import Bestandspaneel

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
        self.Vbox.Add(self.VMidBox, 17, wx.ALL | wx.EXPAND)
        self.Knoppen = KnoppenPaneel(self)
        self.Vbox.Add(self.Knoppen, 3, wx.ALL | wx.EXPAND)        
        self.SetSizer(self.Vbox)
        self.SetBackgroundColour(None)
        self.Show()

    def middenstuk(self):
        
        
        
        
        
        
        PanMid = SubPaneel(self, style=wx.SUNKEN_BORDER)## Mac interface
        PanMid.SetBackgroundColour((0, 0, 255))
        PanRechts = SubPaneel(self, style=wx.SUNKEN_BORDER)
        PanRechts.SetBackgroundColour((125, 0, 250))## Mac interface
        self.VMidBox = wx.BoxSizer(wx.VERTICAL)
        
        #self.VMidBox.Add(self.maakGFFDeel(),-1, wx.ALL, 10 )
        self.VMidBox.Add(Bestandspaneel(self,"""gff(*.gff)|*.gff""",
                                        label="blablabla"),-1, wx.ALL, 10 )
        self.VMidBox.Add(PanMid, 1, wx.ALL | wx.EXPAND, 10)
        self.VMidBox.Add(PanRechts, 1, wx.ALL | wx.EXPAND, 10)


    def maakGFFDeel(self):
        LinkerPan = SubPaneel(self)
        self.PanLinks = SubPaneel(self, style=wx.SUNKEN_BORDER)
        self.gffnaam = wx.StaticText(self.PanLinks, id=-1, label="Geen bestand" +
                                     " geselecteerd ")
        hbox = wx.BoxSizer(wx.HORIZONTAL)
        self.bladerknop = wx.Button(LinkerPan, -1, label="bladeren")
        self.bladerknop.Bind(wx.EVT_BUTTON, self.browsegff)
        hbox.Add(self.gffnaam, 3, wx.EXPAND, wx.ALL)
        self.PanLinks.SetSizer(hbox)
        
        self.LHbox = wx.BoxSizer(wx.HORIZONTAL)
        linkstext = wx.StaticText(LinkerPan, id=-1, label="GFF bestand")
        font = wx.Font(12, wx.DEFAULT, wx.NORMAL, wx.BOLD)
        linkstext.SetFont(font)
        vboxnambro = wx.BoxSizer(wx.VERTICAL)
        vboxnambro.Add(linkstext )
        vboxnambro.Add(self.bladerknop)
        LinkerPan.SetSizer(vboxnambro)
        self.LHbox.Add(LinkerPan, 3,  wx.EXPAND )
        self.LHbox.Add(self.PanLinks, 17, wx.ALIGN_BOTTOM , 10)
        return self.LHbox

    def browsegff(self, event):
        """
        De methode kan bladeren naar een bestand en het bestandsnaam
        daarvan opslaan in een variable.
        """
        wildcard = """gff(*.gff)|*.gff"""
        self.blad = wx.FileDialog(self, "Bladeren", os.getcwd(), "",
                                  wildcard, wx.OPEN)
        if self.blad.ShowModal() == wx.ID_OK:
            self.bestandsnaam = self.blad.GetPath()
            self.setgffnaam()
            
    def setgffnaam(self):
        naam = self.bestandsnaam.split("\\")
        self.gffnaam.SetLabel(label=naam[len(naam)-1])
        
        
        
