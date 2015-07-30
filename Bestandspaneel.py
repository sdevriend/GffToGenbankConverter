"""
Sebastiaan 14-7-15 Bestandpaneeltje schrijven.
Sebastiaan 28-7-15 Documentatie toevoegen, netjes maken.
"""

import wx
import os

from SubPaneel import SubPaneel

class Bestandspaneel(wx.Panel):
    """De class maakt een bestandspaneeltje aan. Hierin kan je browsen naar
        een file, Ook wordt er getoont welk bestand er geselecteerd is.
        Als er gebrowsed is, dan wordt er geen event gemaakt.
    """
    def __init__(self, parent, wildcard, id=wx.ID_ANY, size=wx.DefaultSize,
                 label="", save=False):
        """
        Input
            Wilcard: string met bestandstypes
            label: Tekst voor paneel.
            save: Boolean, True voor opslag, False voor search.
        De init maakt het scherm aan en de daarbij behorende paneeltjes...
        """
        self.BestandPaneel = wx.Panel.__init__(self, parent, id, size=size)
        self.wildcard = wildcard
        BladerPan = self.maakBladerKnop(label, save)
        LHbox = wx.BoxSizer(wx.HORIZONTAL)
        BestHbox = wx.BoxSizer(wx.HORIZONTAL)
        BestHbox.Add(BladerPan, 3,  wx.EXPAND )
        BestHbox.Add(self.maakTextPan(), 17, wx.ALIGN_BOTTOM , 10)
        self.SetSizer(BestHbox)

    def maakBladerKnop(self, label, save):
        """
        Input: 2
            Label: Tekst voor bestandspaneel.
            save: boolean, bij true wordt dit de save knop, anders de
                  browse.

        De methode maakt een paneeltje met daarop een static text en knop.
        Deze wordt gebind op basis van save.
        De onderdelen worden toegevoegd aan een sizer en het paneel daarvan
        wordt terug gegeven.
        """
        LinkstextPanl = SubPaneel(self)
        self.bestandsnaam = "" 
        self.bladerknop = wx.Button(LinkstextPanl, -1, label="bladeren")
        if save:
            self.bladerknop.Bind(wx.EVT_BUTTON, self.savefile)
        else:
            self.bladerknop.Bind(wx.EVT_BUTTON, self.browsefile)
        PanLabel = wx.StaticText(LinkstextPanl, id=-1, label=label)
        font = wx.Font(12, wx.DEFAULT, wx.NORMAL, wx.BOLD)
        PanLabel.SetFont(font)
        vboxnambro = wx.BoxSizer(wx.VERTICAL)
        vboxnambro.Add(PanLabel)
        vboxnambro.Add(self.bladerknop)
        LinkstextPanl.SetSizer(vboxnambro)
        return LinkstextPanl

    def maakTextPan(self):
        """
        De methode maakt een global static text en zet deze in een panel
        die in een boxsizer gezet wordt.
        """
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
        daarvan opslaan in een variable. Wildcard is een string met
        daarin bestandtypes.
        """
        blad = wx.FileDialog(self, "Bladeren", os.getcwd(), "",
                                  self.wildcard, wx.OPEN)
        if blad.ShowModal() == wx.ID_OK:
            self.bestandsnaam = blad.GetPath()
            self.setBestandsNaam()

    def savefile(self, event):
        """
        Savefile werkt hetzelfde als browsefile, maar heeft alleen
        een save dialog met overrride.
        """
        blad = wx.FileDialog(self, "Bladeren", os.getcwd(), "",
                                  self.wildcard, wx.SAVE | wx.OVERWRITE_PROMPT)
        if blad.ShowModal() == wx.ID_OK:
            self.bestandsnaam = blad.GetPath()
            self.setBestandsNaam()

    def setBestandsNaam(self):
        """De methode splits de bestandsnaam op \\ en zet het laatste
           gedeelte in de static text. Zo kan bestandsnaam gezien worden
           zonder het hele path.
        """
        naam = self.bestandsnaam.split("\\")
        self.BestandText.SetLabel(label=naam[len(naam)-1])

    def getFilePath(self):
        """De functie geeft de path van het gekozen bestand terug. """
        return self.bestandsnaam
