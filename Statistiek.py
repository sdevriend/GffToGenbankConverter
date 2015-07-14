from datetime import datetime


class Statistiek():
    def __init__(self):
        self.timer = datetime.now()


    def stop(self):
        self.stop = datetime.now()
        self.verschil = self.stop - self.timer
        print "Gestart op: " + str(self.timer).split(" ")[1].split(".")[0]
        print "Klaar op: " + str(self.stop).split(" ")[1].split(".")[0]
        tijd = str(self.verschil).split(":")
        print "Statistiek:"
        print "Uur:", tijd[0]
        print "Minuten:", tijd[1]
        print "Secondes:", tijd[2].split(".")[0]
