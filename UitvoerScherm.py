"""
Sebastiaan 28-7-15 maken van uitvoer schermpje.
Sebastiaan 29-7-15 Documentatie.

De class zorgt voor een klein schermpje met een label en een knopje.
"""

import wx


class UitvoerScherm(wx.Frame):
    """
    De class maakt het schermpje als de conversie script uitgevoerd
    wordt. Daarnaast bevat de class een methode om de stop knop
    id op te halen.
    """
    def __init__(self, parent, id=wx.ID_ANY,
                 title='', pos=wx.DefaultPosition, size=(300, 300),
                 style=wx.DEFAULT_FRAME_STYLE & ~(wx.RESIZE_BORDER |
                                                  wx.CLOSE_BOX |
                                                  wx.SYSTEM_MENU),
                 name=''):
        """
        De init maakt een frame, en zet daarop een tekst met font en een
        stop knop. Deze worden in een boxsizer gezet en in het midden
        geplaatst.
        Daarnaast wordt de achtergrond op grijs gezet voor een windows
        achtige look.
        """
        super(UitvoerScherm, self).__init__(parent, id, title, pos, size,
                                           style, name)
        PanLabel = wx.StaticText(self, id=-1, label="Script is in uitvoering!")
        font = wx.Font(12, wx.DEFAULT, wx.NORMAL, wx.BOLD)
        PanLabel.SetFont(font)
        self.stopknop = wx.Button(self, -1, label="Stop")
        vbox = wx.BoxSizer(wx.VERTICAL)
        vbox.Add(PanLabel, 0,  wx.ALIGN_CENTER)
        vbox.Add(self.stopknop, 0, wx.ALIGN_CENTER)
        self.SetSizer(vbox)
        self.SetBackgroundColour("LTGRAY")
        self.Show()

    def getStopUitvoer(self):
        """Geeft de id van de stopknop terug aan de interface controller."""
        return self.stopknop.GetId()
