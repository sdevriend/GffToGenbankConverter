"""
Sebastiaan 8-7-15 begin maken interface

De Interface controller beheert de schermflow voor de gebruiker
en stuurt de gegevens door naar de converter.
"""

import wx

from InvoerScherm import InvoerScherm

class ConvertInterface(wx.App):

    def OnInit(self):
        """
        De OnInit wordt aangeroepen als de applicatie wordt gestart.
        Er wordt een schermnummer opgezet met 0 voor de eerste scherm.
        Er wordt een lijst gemaakt met alle beschikbare schermen.
        En als laatste wordt de SchermController aangeroepen.
        De return True statement is om de app te laten runnen door wx.
        """
        self.SchermNr = 0
        self.SchermLijst = [InvoerScherm]
        self.SchermController()
        self.Bind(wx.EVT_BUTTON, self.KnopBeheer)
        return True


    def SchermController(self):
        strNaam = "GFF Converter"
        schermFormaat = (700, 400)
        self.frame = self.SchermLijst[self.SchermNr](None, title=strNaam,
                                                     size=schermFormaat)


    def KnopBeheer(self, event):
        Doorgaan = self.frame.getGoKnop()
        Help = self.frame.getHelpKnopId()
        if event.GetId() == Doorgaan:
            self.files = self.frame.GetNamen()
            if "" in self.files:
                wx.MessageBox("Niet alles is ingevuld!", "Foutmelding",
                              wx.OK | wx.ICON_ERROR)
            else:
                try:
                    print self.files
                    raise ValueError
                    pass # script hier
                except:
                    wx.MessageBox("Er is iets fout gegaan bij het converteren" +
                                  " probeer het eens met een ander bestand.",
                                  "Fout bij het converteren",
                                  wx.OK | wx.ICON_ERROR)
                pass ## start script.
            
        elif event.GetId() == Help:
            wx.MessageBox("Hier kunt u de files inladen die nodig zijn" +
                          " die nodig zijn voor de conversie. \n" +
                          "\tU heeft nodig:\n\n" +
                          "\t\t-Een gff bestand\n" +
                          "\t\t-Een raw bestand met een sequentie daarin\n"
                          "\t\t-Een annotation bestand", "Info", wx.OK)
                          


            
app = ConvertInterface(False)
app.MainLoop()
