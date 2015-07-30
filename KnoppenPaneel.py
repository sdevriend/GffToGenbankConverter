"""
Sebastiaan de Vriend 8-7-15 Knoppen paneel opmaken.
Sebastiaan de Vriend 28-7-15 Documentatie nalopen.

De class maakt een knoppen paneel voor 3 knoppen. Minder knoppen
kunnen ook gemaakt worden.
"""

import sys
import wx

from SubPaneel import SubPaneel


class KnoppenPaneel(wx.Panel):
    """
    Het idee is om een knoppen paneel te maken. Hierop komen drie knoppen
        GoKnop: Voor volgende, nog niks mee gedaan.
        HelpKnop: Voor een popup voor het helpscherm, niks mee gedaan.
        StopKnop: Knop met een event om de interface te sluiten.

    De class zet drie knoppen met subpaneeltjes op een rij netjes.

    pan-knop-pan-knop-pan-knop-pan

    en alles wordt netjes in een horizontal boxsizer geplaatst.
    """
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
        """Exit systeem."""
        sys.exit()


    def TussenPan(self):
        """
        De functie geeft een subpaneeltje terug voor de vijf panelen.
        """
        return SubPaneel(self)
        
        
        
    def getGoKnopId(self):
        """Geeft de id van de Go Knop terug aan hogere lvl interface."""
	return self.GoKnop.GetId()

    def getHelpKnopId(self):
        """Geeft de id van de help Knop terug aan hogere lvl interface."""
	return self.HelpKnop.GetId()
