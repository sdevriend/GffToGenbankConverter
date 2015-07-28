"""
Sebastiaan 8-7-15 begin maken interface

De Interface controller beheert de schermflow voor de gebruiker
en stuurt de gegevens door naar de converter.
"""

import wx

from InvoerScherm import InvoerScherm
from gff_conversiescript import gff_conversie
from UitvoerScherm import UitvoerScherm
from EindScherm import EindScherm
from GaugeFrame import GaugeFrame # kan weg ?
import threading

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
        self.SchermLijst = [InvoerScherm, UitvoerScherm, EindScherm]
        self.SchermController()
        self.Bind(wx.EVT_BUTTON, self.KnopBeheer)
        return True


    def SchermController(self):
        strNaam = "GFF Converter"
        schermFormaat = (700, 400)
        self.frame = self.SchermLijst[self.SchermNr](None, title=strNaam,
                                                     size=schermFormaat)
    def beheer_conversie(self):
        
        try:
            #status = wx.MessageDialog(self.frame, "dingetje is bezig", "ding bezig",
                          #wx.STAY_ON_TOP  | wx.CANCEL)
            #status.SetOKLabel("stop")
            
            f = self.files
            #self.gFr = GaugeFrame(self.frame, "Omzetten", 60)
            #self.gFr.Show()
            #gff_conversie(f[0], f[1], f[2], f[3])
            draad = threading.Thread(target=gff_conversie,
                                    args=(f[0], f[1], f[2], f[3]))
            draad.setDaemon(True)
            
            
            draad.start()
            self.frame.addThread(draad)
            
            #status.ShowModal()
            draad.join()
            #status.EndModal()
            #self.gFr.Hide()
            print "draadje"
            #raise ValueError
            return 5
            #pass # script hier
            
        except Exception as e:
            print e.args
            print "error"
            wx.MessageBox("Er is iets fout gegaan bij het converteren" +
                          " probeer het eens met een ander bestand.",
                          "Fout bij het converteren",
                           wx.OK | wx.ICON_ERROR)
            pass ## start script.
        


    def KnopBeheer(self, event):
        Doorgaan = self.frame.getGoKnop()
        Help = self.frame.getHelpKnopId()
        if event.GetId() == Doorgaan:
            self.files = self.frame.GetNamen()
            if "" in self.files:
                wx.MessageBox("Niet alles is ingevuld!", "Foutmelding",
                              wx.OK | wx.ICON_ERROR)
            else:
                self.SluitScherm()
                draad = threading.Thread(target=self.beheer_conversie)
                draad.setDaemon(True)
                self.frame.addThread(draad)
                draad.start()
                
                
                            
        elif event.GetId() == Help:
            wx.MessageBox("Hier kunt u de files inladen die nodig zijn" +
                          " die nodig zijn voor de conversie. \n" +
                          "\tU heeft nodig:\n\n" +
                          "\t\t-Een gff bestand\n" +
                          "\t\t-Een raw bestand met een sequentie daarin\n"
                          "\t\t-Een annotation bestand", "Info", wx.OK)
                          

    def SluitScherm(self):
        """
        De functie sluit self.frame, telt 1 bij de schermteller en
        start de functie SchermBeheer op.
        """
        print "sluiot"
        self.frame.Destroy()
        self.SchermNr += 1
        self.SchermController()
            
app = ConvertInterface(False)
app.MainLoop()
