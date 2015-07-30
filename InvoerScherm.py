"""
Sebastiaan 8-7-15 Maken van invoerscherm.
Sebastiaan 28-7-15 documenteren en netjes maken.

De class maakt het invoerscherm waar de gebruiker een gff bestand,
raw(fasta) en annotation bestand kunnen invoeren. Daarnaast kan
de gebruiker aangeven waar het bestand opgeslagen kan worden.
"""

import wx

from Bestandspaneel import Bestandspaneel
from KnoppenPaneel import KnoppenPaneel


class InvoerScherm(wx.Frame):
    """
    De class roept de methode middenstuk aan, waar een global boxsizer
    wordt gemaakt. Deze wordt toegevoegd aan een vertical boxsizer met
    de verhouding 17 en de knoppenpaneel met verhouding 3.
    In het knoppenpaneel staat een stop knop, help knop en go knop.
    Als laatste wordt de kleur aangepast en het scherm wordt getoont.
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
        #Hier kunnen extensions veranderd worden en panelen toegevoegd
        #en verwijderd worden.
        """
        De functie roept 4x een bestandspaneel aan. Aan bestandspaneel
        wordt elke keer een wildcard, label en bij de save wordt een
        boolean meegegeven.

        De panelen worden toegevoegd aan de global boxsizer met
        een ruimte van 10 pixels tussen elke paneel.
        """
        self.gff = Bestandspaneel(self,"""Gff(*.gff)|*.gff""",
                                        label="GFF file")
        self.raw = Bestandspaneel(self,"""Fasta(*.fasta, *.fsa, *.fa)
                                          |*.fasta;*.fsa;*.fa""",
                                        label="RAW file")
        self.annot = Bestandspaneel(self, """Annotation(*.*)|*.*""",
                                    label="Annotation \nfile")
                                           
        self.save = Bestandspaneel(self, """Genbank(*.gbk)|*.gbk""",
                                    label="Aangepaste\ngbk locatie", save=True)
        self.VMidBox = wx.BoxSizer(wx.VERTICAL)
        self.VMidBox.Add(self.gff ,0,wx.ALL, 10 )
        self.VMidBox.Add(self.raw , 0, wx.ALL, 10 )
        self.VMidBox.Add(self.annot, 0, wx.ALL, 10 )
        self.VMidBox.Add(self.save, 0, wx.ALL, 10 )

    def getGoKnop(self):
        """
        Functie geeft de id van de go knop uit het knoppen paneel
        terug.
        """
        return self.Knoppen.getGoKnopId()

    def GetNamen(self):
        #Als er een extra bestandspaneel komt of wordt verwijderd,
        #verwijder of voeg dan een naam toe.
        """
        De functie haalt alle bestandspaden op van de bestandspanelen.
        Als er in de save geen path zit, dan wordt de path van
        de gff genomen en wordt gff op het einde eraf gehaald en gbk
        erin gezet.
        """
        naam1 = self.gff.getFilePath()
        naam2 = self.raw.getFilePath()
        naam3 = self.annot.getFilePath()
        naam4 = self.save.getFilePath()
        if len(naam4) == 0:
            naam4 = naam1[:-3] + "gbk"
        return [naam1, naam2, naam3, naam4]

    def getHelpKnopId(self):
        """ Functie geeft de id van de helpknop door aan de controller. """
        return self.Knoppen.getHelpKnopId()


    
        
