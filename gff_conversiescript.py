from datetime import datetime

SUPERSTRING = ''
import csv
from Statistiek import Statistiek
##import origin
from Refference import check
from Refference import refference
from Merger import Merger
from Writefile import write_file
from Writefile import write_list
from Writefile import make_gbk_file
from Fastagenerator import generate_fasta



def gff_conversie(gff_name, fasta_name, annot_file, gbk_name):
    #Functie hernoemd van main naar gff_conversie
    """
    De functie roept de andere functies aan:
    het openen van de file, het maken van een multidimensionale lijst,
    het filteren van de attributen, het maken van de genbank file en
    het schrijven van de afsluitende tag //
    """
    print "Merger maken"
    merger = Merger(fasta_name)
    refference(annot_file)
    print "Merger klaar"

    stopwatch = Statistiek()
    make_gbk_file(gbk_name)
    write_file('LOCUS PLACEHOLDER\n', gbk_name)
    write_file('FEATURES\t\tLocation/Qualifiers\n', gbk_name)
    write_file("PLACEHOLDER\n", gbk_name)
    print "GFF bestand openen"
    contigdict = merger.getdict()
    dataBalancer(contigdict, gff_name, gbk_name)
    print "Na verdeel"
    print "Bestand genereren"
    print "DO FASTA"

    # print merger.get_fasta()
    print "DONE FASTA"

    highest_stop = 10
    lowest_start = 1

    insert_values(highest_stop, lowest_start, 2, gbk_name)
    insert_values(highest_stop, "unspecified", 0, gbk_name)
    print "Sequentie schrijven"
    generate_fasta(fasta_name, gbk_name)
    ##write_file()
    sluiter = "//"
    
    write_file(sluiter, gbk_name)
    print "Klaar!"
    stopwatch.stop()


def insert_values(maxpar, extrapar, type, gbk_name):
    readfile = open(gbk_name, 'r')
    lines = readfile.readlines()
    readfile.close()
    if type == 2:
        insertstring = "\t source\t\t\t\t\t" + "1" + ".." + str(maxpar) + "\n"

    if type == 0:
        insertstring = "LOCUS\t\t%s\t%s" % (str(extrapar), str(maxpar) + " bp \t DNA \n")
    lines[type] = insertstring
    writefile = open(gbk_name, 'w')
    for line in lines:
        writefile.write(line)
    writefile.close()





def open_gff(gff_name):
    """
    Het gff bestand wordt geopend, de rijen in het bestand
    worden terug gegeven als de generator wordt aangeroepen. Als
    het bestand leeg is, dan wordt None terug gegeven.
    """
    # Hier heb ik een aantal aanpassingen gemaakt. Ik heb als eerste
    # de open_gff omgezet naar een generator. Deze yield een rij en
    # None als de file leeg is. Daarnaast wordt de filename bepaald
    # door gff_name. Deze wordt meegegven door de interface, maar kan ook
    # aangepast worden in de main.
    gff_file = open(gff_name, 'rb', buffering=1)
    reader = csv.reader(gff_file, delimiter="\t")
    
    for row in reader:
        if "#" not in row[0]:
            yield row
    while True:
        yield None



def dataBalancer(contigdict, gff_name, gbk_name):
    """
    Input: 3
        contigdict, contig dictionary van merger.
        gff_name: bestandsnaam
        gbk_name: bestandsnaam

    De functie heeft eerst gebruik gemaakt van multi process, maar
    blijkt bij monitoring het toch niet nodig te hebben.

    De functie maakt een generator aan met de naam data. Vervolgens
    worden de loop variabelen data en stop gemaakt.

    In rij komt elke yield van data te staan. En stop is de boolean om
    de loop te stoppen als rij een None yield.

    De functie loopt op een while met als conditie dat de loop stopt
    als er geen regels meer in het bestand zitten.

    In de while loop wordt de resultaat lijst aangemaakt en de draden
    lijst. De draden lijst is voor de eerste for loop.
        In de eerste for loop wordt er 8 keer geloopt. Dit was voor de
        8 cores, maar werkt serial ook erg goed. In de 8 for loop wordt
        er 100 duizend keer geloopt om data punten te yielden en toe te
        voegen aan de lijst draadlijst, tenzij er een None wordt geyield,
        dan wordt de loop afgesloten.
    De 8 multi dementionale lijsten worden na de vul loops 1 voor 1
    doorgegven aan de functie lijst_gb_invoer, het resultaat daarvan
    wordt in de resultaat lijst gezet en wordt doorgegeven aan
    write_list zodat er 800k lines geschreven worden.
    """
    print "start verdeel"
    print gff_name
    verdeelstat = Statistiek()
    data = open_gff(gff_name)
    rij = "" #declaratie voor while loop
    stop = False
    while rij != None:
        resultaat = []
        draden = []
        for x in range(8):
            draadlijst = []
            for x in range(100000):
                rij = data.next()
                
                if rij == None:
                    stop = True
                    break
                else:
                   draadlijst.append(rij)
            draden.append(draadlijst)      
            if stop:
                break
        for draad in draden:
            resultaat.append(lijst_gb_invoer(draad,contigdict))
        write_list(resultaat, gbk_name)
                   

    
    verdeelstat.stop()    
    print "einde verdeelstation"


def lijst_gb_invoer(lgi_lijst, contigdict):
    gb_lijst = []
    for item in lgi_lijst:
        gb_lijst += make_gb(item, contigdict)
    return gb_lijst
    
def make_gb(mgb_rijen, contigdict):
    """
    Een standaard header wordt aangemaakt.
    De source regel wordt opgesteld door te kijken naar de laagste
    beginpositie en de hoogste eindpositie.
    Deze string wordt aan het bestand toegevoegd.
    Iedere feature in de lijst wordt genomen en voor iedere instantie wordt de
    dictionary met attributen gemaakt.
    Een lege string wordt gemaakt waarin de data uiteindelijk komt.
    Eerst wordt de feature toegevoegd. Dit wordt gedaan met de bijbehorende
    positie. Als er aangegeven wordt dat de data complementair is, wordt dit
    toegevoegd aan de string.
    Daarna wordt het gene attribuut toegevoegd. Deze neemt het ID van
    de instantie uit de dictionary en voegt deze toe aan de string.
    Daarna wordt een eventuele notitie toegevoegd. Als deze None is, wordt
    deze niet toegevoegd. Ditzelfde wordt gedaan met het db_xref attribuut
    Iedere instantie wordt dan appart meegegeven aan de functie writeFile.
    """

    ##print "aantal rijen: ",len(mgb_rijen)
    ##print "aantal attrij: ", len(mgb_attrijen)
    
    featurelist = []

    mgb_attdict = filters(mgb_rijen)
    finalstring = ''
    # print "Merger samenvoegen maken"

    # print "samenvoegen gemaakt"
    # print "Dictionary maken"

    # print "Dictionary gemaakt"
    
    testvar = mgb_attdict.get('id').lower()

    if "contig" in testvar:
        # print mgb_attdict.get('id').lower()
        if ":" in testvar:
            contig = testvar.split(':')[0]
            
        elif ":" not in testvar:
            contig = testvar
        else:
            contig = "AAAA"
    
        try:
            start = contigdict[contig]
            print start
        except KeyError:
            print "Can't find this contig in the raw file"
            pass


    # Eerste: feature

    if not "complement" in mgb_rijen[8]:
        feature = str("\t %-20s \t %s..%s\n" % (mgb_rijen[2],
                                                mgb_rijen[3], mgb_rijen[4]))
    else:
        feature = str("\t %-6s \t complement(%s..%s)\n" %
                      (mgb_rijen[2],
                       mgb_rijen[3], mgb_rijen[4]))
    finalstring += feature
    # Tweede: gene
    gene = str("\t\t\t\t /gene=\"%s\"\n") % mgb_attdict.get('id')
    if "cypCar" in gene:
        # print check(gene.split("-")[0].split("\"")[1])
        geneid = str(check(gene.split("-")[0].split("\"")[1]))
        finalstring += str("\t\t\t\t /gene=\"%s\"\n") % geneid
    else:
        finalstring += gene
    # Derde: note
    note = mgb_attdict.get('note')

    if note is not None:
        finalstring += "\t\t\t\t /note=\"%s\"\n" % note
    # Vierde: db_xref
    db_xref = mgb_attdict.get('db_xref')
    if db_xref is not None:
        finalstring += "\t\t\t\t /note=\"%s\"\n" % db_xref

    featurelist.append(finalstring)
    # features.append(featurelist)
    ##print featurelist
    """for i in range(len(featurelist)):
        genbank = featurelist[i]
        write_file(genbank)
    """
    ## wat doet deze?
    
    return featurelist


def filters(rijen, versie=3):
    """
    De functie maakt een dictionary van de attributenkolom en geeft deze terug
    """
    splitter = {2: " ", 3: ";"}

    current = rijen[8].split(splitter[versie])
    
    if versie == 2:
        att = {"id": None, "name": None, "alias": None, "parent": None,
               "target": None, "gap": None, "derives_from": None,
               "note": None, "dbxref": None, "ontology_term": None,
               "gene": None, "EC_number": None, "codon_start": None,
               "product": None, "db_xref": None, "translation": None,
               "organism": None, "strain": None, "mol_type": None,
               "allele": None, "gene_synonym": None, "map": None,
               "operon": None, "phenotype": None, "standard_name": None,
               "function": None, "transcript": None}
    else:
        att = {"id": None, "name": None,
               "note": None, "dbxref": None}
    for waarde in current:
        current2 = waarde.split("=")
        if current2[0].lower() in att:

            try:
                att[current2[0].lower()] = current2[1]
            except KeyError:
                print "onbekend attribuut"
            except IndexError:
                print "missende data"
    # print [att]                

    return att

def run_gff_conversie(gff_name, fasta_name, annot_file, gbk_name, queue):
    try:
        gff_conversie(gff_name, fasta_name, annot_file, gbk_name)
        queue.put("Goed")
    except Exception as e:
        print e.args
        if e.args == ():
            queue.put(e.args)
        else:
            queue.put(e[0])

'''
referentie
in multirij:
0 : seqname
1 : source
2 : feature
3 : start position
4 : stop position
5 : score
6 : strand
7 : frame
8 : group
'''
if __name__ == '__main__':
    """
    Functie roept de hernoemde main aan, gff conversie.
    Aan gff_conversie worden 4 data punten meegegeven. Deze kunnnen
    aangepast worden naar eigen bestandspaden voor test doeleindes.
    """
    #mp.freeze_support() # oude line
    gffname = "D:\\ncbi_data\\software\\Converter\\testfile_500klines.gff"
    fastaname = "D:\\ncbi_data\\software\\Converter\\carp_pbjelly.fa"
    gbk_name = "D:\\ncbi_data\\software\\Converter\\carp_pbjelly.gbk"
    annot_file = "bla"
    gff_conversie(gffname, fastaname, gbk_name, annot_file)

