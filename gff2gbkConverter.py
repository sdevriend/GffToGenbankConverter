"""
Sebastiaan 8-7-15 begin maken interface

De Interface controller beheert de schermflow voor de gebruiker
en stuurt de gegevens door naar de converter.

Q: Ik wil de bestandstypes veranderen die gevraagd worden in het
   browse scherm
A: Dit kan in Invoerscherm. Pas in de functie middenstuk bij het
   juiste paneeltje de wildcard string aan naar
   BESTANDSTYPENAAM(*.TYPE1, *.TYPE2)|*.TYPE1; *.TYPE2

Q: Ik wil foutmeldingen toevoegen die de gebruiker kan zien.
A: Verander in het conversie script de except statement en geef een
   nieuwe waarde terug. Pas dan vervolgens in beheer_conversie
   de if statement aan en vang deze op met een bericht.
   Vergeet dan niet om de foutmelding te tonen.
"""

import threading
import time
import sys
import Queue
import wx

from EindScherm import EindScherm
from gff_conversiescript import run_gff_conversie
from InvoerScherm import InvoerScherm
from UitvoerScherm import UitvoerScherm


class ConvertInterface(wx.App):
    """
    De class beheerd de flow van de applicatie.
    """
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
        """
        De functie kijkt wat het schermNr is en zet de schermnaam en
        formaat voor elk schermpje.
        Bij het uitvoerschermpje wordt een global boolean aangemaakt
        zodat de class weet of er een melding gegeven is.
        """
        if self.SchermNr == 0:
            strNaam = "GFF Converter - Invoer"
            schermFormaat = (700, 400)
            self.files = []
        elif self.SchermNr == 1:
            
            strNaam = "GFF Converter - Bezig..."
            schermFormaat = (200, 100)
        elif self.SchermNr == 2:
            strNaam = "GFF Converter - Klaar"
            schermFormaat = (300, 200)
        self.frame = self.SchermLijst[self.SchermNr](None, title=strNaam,
                                                     size=schermFormaat)
        if self.SchermNr == 1: # Aanroep voor
            self.uitvoeropen = False
            
    def beheer_conversie(self):
        """
        De methode start het conversie scipt op.
        Als eerste worden de filenames omgezet in de varaible f om het kort
        te houden. Daarna wordt de import queue aangeroepen en
        wordt een draad aangemaakt die naar de conversie script gaat
        met als arguments de filenames en de queue.

        Daarna wordt draad als deamon ingesteld zodat deze ook stopt zodra
        het de main thread stopt.

        Daarna wordt de draad gestart en daarna gejoined zodat het script
        verder loopt zodra de thread klaar is.

        Uit de queue wordt het resultaat gehaald. Dit kan Goed zijn
        of een error. Als het result '28' is, dan is er te weinig ruimte
        op de schijf(python standaard melding). () is out of memmory, maar
        kan je merken omdat je computer bijna crashed. En als laatste wordt
        gekeken of fout aanstaat. Dan wordt er een bericht getoont en het
        schermnummer verlaagd zodat deze op 0 komt en het eerste scherm toont.

        Als laatste wordt wx.CallAfter(self.synchUitvoer) uitgevoerd.
        Met deze functie wordt de thread afgesloten en het script naar
        een sync methode gestuurd. Dit kan omdat deze functie ook
        gestart is op een apparte thread.
        """
        f = self.files  
        queue = Queue.Queue()
        draad = threading.Thread(target=run_gff_conversie,
                                args=(f[0], f[1], f[2], f[3], queue))
        draad.setDaemon(True)
        draad.start()
        draad.join() 
        result = queue.get()
        fout = False
        if result == "Goed":
            pass
        elif result == 28:
            bericht = "Onvoldoende ruimte om gbk op te slaan."
            fout = True
        else:
            # Mogelijk is dit memmory error. Pc crasht dan best hard
            bericht = ("Er is iets fout gegaan bij het converteren" +
                        " probeer het eens met een ander bestand.")
            fout = True           
        if fout:    
            wx.MessageBox(bericht, "Fout bij het converteren",
                           wx.OK | wx.ICON_ERROR)
            self.SchermNr = -1
        wx.CallAfter(self.synchUitvoer)

    def synchUitvoer(self):
        """
        De functie wordt aangeroepen nadat de conversie klaar is.
        Er wordt gekeken of het stop dialoog openstaat , als dit zo
        is dan wordt er via een thread de syncDraad functie opgeroepen
        met deamon optie.

        Als dit niet zo is, dan wordt sluitscherm opgeroepen.
        """
        if self.uitvoeropen:
            draad = threading.Thread(target=self.syncDraad)
            draad.setDaemon(True)
            draad.start()
        else:
            self.SluitScherm()
        
    def syncDraad(self):
        """
        De functie loopt op een thread.
        Er wordt gekeken in een while loop of self.uitvoeropen op true staat.
        Als dit zo is, dan wordt de loop stilgezet voor 2 seconden. Als
        de gebruiker het schermpje gesloten heeft, dan wordt
        CallAffter sluit scherm aangeroepen zodat de thread
        gesloten wordt.
        """
        while self.uitvoeropen:
            time.sleep(2)
        wx.CallAfter(self.SluitScherm)
        
    def KnopBeheer(self, event):
        """
        De functie vangt de knoppen op die ingedrukt worden van
        doorgaan en help over alle schermen.
        De knop wordt opgevraagt aan de hand van het schermpje dat open
        staat. Dit wordt gedaan via self.SchermNr.

        Bij het invoer scherm wordt de doorgaan knop en helpknop
        opgevraagt. Als de doorgaan knop is ingedrukt, dan
        wordt er gekeken of alle files zijn oppgegeven. Als dit niet zo is,
        dan krijgt de gebruiker een foutmelding te zien. Als de gebruiker
        wel alles heeft ingevuld, dan wordt sluitscherm aangeroepen en
        daarna wordt de conversie functie gestart op een nieuwe thread die
        op een deamon gezet wordt zodat deze netjes afgesloten wordt.
        Als de helpknop ingedrukt wordt, dan krijgt de gebruiker een infoscherm
        te zien.

        Bij het uitvoer scherm wordt de stopscherm getoont en
        wordt een global boolean op true gezet. Hierdoor blijft het scherm
        open en krijg je geen dubbele schermen als het script klaar is.

        Bij het laatste scherm wordt het schermnummer op -1 gezet zodat
        het invoerscherm weer naar boven komt.
        """
        if self.SchermNr == 0: # Invoer frame
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
                    draad.start()

            elif event.GetId() == Help:
                wx.MessageBox("Hier kunt u de files inladen die nodig zijn" +
                              " die nodig zijn voor de conversie. \n" +
                              "\tU heeft nodig:\n\n" +
                              "\t\t-Een gff bestand\n" +
                              "\t\t-Een raw bestand met een sequentie daarin\n"
                              "\t\t-Een annotation bestand", "Info", wx.OK)
        elif self.SchermNr == 1: # Uitvoer frame
            Stop = self.frame.getStopUitvoer()
            if event.GetId() == Stop:
                UVStat = wx.MessageDialog(self.frame, "Weet u zeker dat u wilt " +
                                  "annuleren? Het bestand is niet af.",
                                  "Bevestiging", wx.STAY_ON_TOP  | wx.CANCEL)
                UVStat.SetOKCancelLabels("Stoppen", "Doorgaan")
                self.uitvoeropen = True
                res = UVStat.ShowModal()
                if res == wx.ID_OK:
                    sys.exit()
                self.uitvoeropen = False
        elif self.SchermNr == 2: # eindscherm
            Door = self.frame.getDoor()
            if event.GetId() == Door:
                self.SchermNr = -1
                self.SluitScherm()
                

    def SluitScherm(self):
        """
        De functie sluit self.frame, telt 1 bij de schermteller en
        start de functie SchermBeheer op.
        """
        self.frame.Destroy()
        self.SchermNr += 1
        self.SchermController()
            
app = ConvertInterface(False)
app.MainLoop()
