from Writefile import write_file
class Merger:
    def __init__(self, filename):
        self.filename = filename
        self.fasta = ""
        self.posdict = {}
        self.mergedict()
    def read_generator(self):
        fastaFile = open(self.filename ,'r')
        for line in fastaFile.readlines():
            if ">" not in line:
                yield [0,line]
            else:
                yield [1,line]

        

    def mergedict(self):
        generator = self.read_generator()    
        for x in range(500000):   
            try:
                line = generator.next()
                if line[0] == 0:
                    self.fasta += line[1]
                elif line[0] == 1:
                    self.posdict[self.headerdict(len(self.fasta),line[1])] = len(self.fasta)
            except StopIteration:
                break

    def headerdict(self, startpos, line):
        line = line.strip(">")
        return line.strip("\n")
                             

    def getfasta(self):
        return self.fasta.upper()
    
    def getdict(self):
        return self.posdict


