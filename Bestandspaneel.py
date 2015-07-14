"""
Sebastiaan 14-7-15 Bestandpaneeltje schrijven. Kan handig zijn.
"""

import wx
import os
from SubPaneel import SubPaneel

class Bestandspaneel(wx.Panel):
    def __init__(self, parent, wildcard, id=wx.ID_ANY, size=wx.DefaultSize,
                 label=""):
        self.BestandPaneel = wx.Panel.__init__(self, parent, id, size=size)
        self.wildcard = wildcard
        LinkstextPanl = SubPaneel(self)
        
        self.bladerknop = wx.Button(LinkstextPanl, -1, label="bladeren")
        self.bladerknop.Bind(wx.EVT_BUTTON, self.browsefile)

        
        LHbox = wx.BoxSizer(wx.HORIZONTAL)

        PanLabel = wx.StaticText(LinkstextPanl, id=-1, label=label)
        font = wx.Font(12, wx.DEFAULT, wx.NORMAL, wx.BOLD)
        PanLabel.SetFont(font)

        vboxnambro = wx.BoxSizer(wx.VERTICAL)
        vboxnambro.Add(PanLabel)
        vboxnambro.Add(self.bladerknop)
        LinkstextPanl.SetSizer(vboxnambro)

        BestHbox = wx.BoxSizer(wx.HORIZONTAL)
        BestHbox.Add(LinkstextPanl, 3,  wx.EXPAND )
        BestHbox.Add(self.maakTextPan(), 17, wx.ALIGN_BOTTOM , 10)
        self.SetSizer(BestHbox)
        
    def maakTextPan(self):
        TextPan = SubPaneel(self, style=wx.SUNKEN_BORDER)
        self.BestandText = wx.StaticText(TextPan, id=-1, label="Geen bestand" +
                                     " geselecteerd ")

        hbox = wx.BoxSizer(wx.HORIZONTAL)
        hbox.Add(self.BestandText, 3, wx.EXPAND, wx.ALL)
        TextPan.SetSizer(hbox)
        return TextPan


    def browsefile(self, event):
        """
        De methode kan bladeren naar een bestand en het bestandsnaam
        daarvan opslaan in een variable.
        """
        
        blad = wx.FileDialog(self, "Bladeren", os.getcwd(), "",
                                  self.wildcard, wx.OPEN)
        if blad.ShowModal() == wx.ID_OK:
            self.bestandsnaam = blad.GetPath()
            self.setBestandsNaam()


    def setBestandsNaam(self):
        naam = self.bestandsnaam.split("\\")
        self.BestandText.SetLabel(label=naam[len(naam)-1])
        
