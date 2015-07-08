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
        return True


    def SchermController(self):
        strNaam = "GFF Converter"
        schermFormaat = (700, 400)
        self.frame = self.SchermLijst[self.SchermNr](None, title=strNaam,
                                                     size=schermFormaat)



app = ConvertInterface(False)
app.MainLoop()
