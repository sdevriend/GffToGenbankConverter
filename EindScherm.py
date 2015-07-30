"""
Sebastiaan 29-7-15 Eindscherm maken en documenteren.
"""
import sys
import wx

class EindScherm(wx.Frame):
    """Class maakt een eindschermpje met daarop 2 knopjes en een stuk
        tekst"""
    def __init__(self, parent, id=wx.ID_ANY,
                 title='', pos=wx.DefaultPosition, size=(0, 0),
                 style=wx.DEFAULT_FRAME_STYLE & ~(wx.RESIZE_BORDER |
                                                  wx.CLOSE_BOX |
                                                  wx.SYSTEM_MENU),
                 name=''):
        super(EindScherm, self).__init__(parent, id, title, pos, size,
                                           style, name)
        PanLabel = wx.StaticText(self, id=-1, label="Conversie is klaar\n"
                                 "Nog een file converteren?")
        font = wx.Font(12, wx.DEFAULT, wx.NORMAL, wx.BOLD)
        PanLabel.SetFont(font)
        buttonhbox = wx.BoxSizer(wx.HORIZONTAL)
        self.Stop = wx.Button(self, -1, label="Nee")
        self.Stop.Bind(wx.EVT_BUTTON, self.Stoppen)
        self.Door = wx.Button(self, -1, label="Ja")
        buttonhbox.Add(self.Stop, 0, wx.ALIGN_CENTER)
        buttonhbox.Add(self.Door, 0, wx.ALIGN_CENTER)
        Vbox = wx.BoxSizer(wx.VERTICAL)
        Vbox.Add(PanLabel, 0, wx.ALIGN_CENTER_HORIZONTAL)
        Vbox.Add(buttonhbox, 0, wx.ALIGN_CENTER_HORIZONTAL)
        self.SetSizer(Vbox)
        self.SetBackgroundColour("LTGRAY")
        self.Show()
        wx.MessageBox("Conversie is klaar!", "Statusmelding",
                              wx.OK | wx.ICON_INFORMATION)

    def Stoppen(self, event):
        sys.exit()

    def getDoor(self):
        """Functie geeft id van doorgaanknop door aan  hogerop."""
        return self.Door.GetId()
        
