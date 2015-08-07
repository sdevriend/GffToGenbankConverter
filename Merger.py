from Writefile import write_file
class Merger:
    '''
    De klasse maakt een grote fastafile
    //TODO fastafile doorsturen naar Origin maker
    Maakt een dictionary waar de naam van de sequentie
    en de startpositie in het grote bestand in worden opgeslagen.
    '''
    def __init__(self, filename):
        '''
        Bij het maken van een object wordt de filenaam opgeslagen
        Een dictionary wordt aangemaakt en de methode die de fasta en
        dictionary maakt wordt aangeroepen.
        '''
        self.filename = filename
        self.fasta = ""
        self.posdict = {}
        self.mergedict()
        
    def read_generator(self):
        '''
        Generator die de fastafile opent en iedere regel
        yield, samen met een index, afhankelijk van de > in
        de header van een fasta bestand.
        '''
        fastaFile = open(self.filename ,'r')
        for line in fastaFile.readlines():
            if ">" not in line:
                yield [0,line]
            else:
                yield [1,line]

        

    def mergedict(self):
        '''
        De generator wordt aangeroepen en opgeslagen.
        In een loop wordt iedere regel in de generator aangeroepen.
        Als dit een header betreft, wordt deze in een dictionary gestopt
        samen met de postitie.
        Als het een sequentie betreft wordt deze opgeslagen in de fasta string.
        Als de regels op zijn, stopt de loop.
        '''
        generator = self.read_generator()    
        while True:
            try:
                line = generator.next()
                if line[0] == 0:
                    self.fasta += line[1]
                elif line[0] == 1:
                    line = line[1].strip(">")
                    line = line.strip("\n")
                    self.posdict[line.lower()] = len(self.fasta)
            except StopIteration:
                break
                             

    def getfasta(self):
        '''
        Geeft de sequentie terug in hoofdletters.
        '''
        return self.fasta.upper()
    
    def getdict(self):
        '''
        Geeft de dictionary terug
        '''
        return self.posdict


