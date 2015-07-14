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
        self.gff = Bestandspaneel(self,"""gff(*.gff)|*.gff""",
                                        label="GFF file")
        self.raw = Bestandspaneel(self,"""fasta(*.fasta)|*.fasta""",
                                        label="RAW file")
        self.annot = Bestandspaneel(self, """*(*.*)|*.*""",
                                    label="Annotation \nfile")
                                           
        self.save = Bestandspaneel(self, """gb(*.gb)|*.gb""",
                                    label="Opslaan \nlocatie", save=True)
        
        
        
        
        
        #PanMid = SubPaneel(self, style=wx.SUNKEN_BORDER)## Mac interface
        #PanMid.SetBackgroundColour((0, 0, 255))
        #PanRechts = SubPaneel(self, style=wx.SUNKEN_BORDER)
        #PanRechts.SetBackgroundColour((125, 0, 250))## Mac interface
        self.VMidBox = wx.BoxSizer(wx.VERTICAL)
        
        self.VMidBox.Add(self.gff ,0,wx.ALL, 10 )
        #self.VMidBox.Add(SubPaneel(self),0, wx.ALL, 20)
        self.VMidBox.Add(self.raw , 0, wx.ALL, 10 )
        #self.VMidBox.Add(SubPaneel(self),0, wx.ALL, 20)
        self.VMidBox.Add(self.annot, 0, wx.ALL, 10 )
        self.VMidBox.Add(self.save, 0, wx.ALL, 10 )


    def getGoKnop(self):
        return self.Knoppen.getGoKnopId()


    def GetNamen(self):
        naam1 = self.gff.getFilePath()
        naam2 = self.raw.getFilePath()
        naam3 = self.annot.getFilePath()
        naam4 = self.save.getFilePath()
        if len(naam4) == 0:
            naam4 = naam1[:-3] + "gb"
        return [naam1, naam2, naam3, naam4]

    def getHelpKnopId(self):
        return self.Knoppen.getHelpKnopId()


    
        
