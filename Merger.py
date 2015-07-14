class Merger():
    """
    De klasse voegt meerdere fastafiles samen tot een lange sequentie
    ook voegt het de namen in een dictionary met de start en stop posities
    in de lange sequenties.
    """
    def __init__(self):
        """
        De fastabestanden worden uitgelezen. Er wordt door deze lijst geloopd
        Als het de header betreft (>) wordt de naam als key in de dictionary
        geplaatst. De lengte wordt aangepast aan de lengte van de sequentie
        en de start en stoppositie worden opgeslagen als values in de dictionary
        Als het de sequentie betreft, wordt deze aan de lange string van sequentie toegevoegd.
        :return:
        """
        self.length = 1
        self.contigs = []
        self.dict = {}
        self.fastanames = []
        self.lines = self.setlines()
        self.fasta = ''

        #print self.get_dict()

    def do_dict(self):
        lines = self.get_lines()
        for line in range(len(lines)):
            if ">" in lines[line]:
                self.fastanames.append(lines[line])
                startpos = self.length
                self.length += len(lines[line+1])
                #print len(lines[line+1])
                stoppos = self.length
                self.dict[lines[line].strip('\n')] = [startpos, stoppos]


    def do_fasta(self):
        lines = self.get_lines()
        for line in range(len(lines)):
            if ">" not in lines[line]:
                self.fasta += lines[line]
    def setlines(self):
        """
        Het fasta bestand wordt uitgelezen
        :return: de regels in het bestand
        """
        fastafile = open("test.fa")
        fastaseqs = fastafile.readlines()
        fastafile.close()
        return fastaseqs


    def get_lines(self):
        return self.lines
    def get_dict(self):
        """
        Geeft de dictionary terug
        :return: Dictionary
        """
        return self.dict
    def get_fasta(self):
        """
        De fasta string wordt teruggegeven
        :return: fasta string
        """
        return self.fasta
    def get_start(self, key):
        """
        De methode kijkt of de meegegeven key in de dictionary zit. Is dit het geval,
        wordt de value hiervan teruggegeven.
        :param key: Key value voor de dictionary
        :return: startpositie
        """
        if key.lower() in self.dict:
            print "SUCCES BYATCH"
            return self.dict[key][0]
    def get_stop(self,key):
        """
        De methode kijkt of de meegegeven key in de dictionary zit. Is dit het geval,
        wordt de value hiervan teruggegeven
        :param key: key voor de dictionary
        :return: stoppositie
        """
        print key.lower()
        if key.lower() in self.dict:

            return self.dict[key][1]
        else:
            print "nope"

