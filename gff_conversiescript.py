SUPERSTRING = ''
import csv
from Statistiek import Statistiek
from origin import origin


def main():
    """
    De functie roept de andere functies aan:
    het openen van de file, het maken van een multidimensionale lijst,
    het filteren van de attributen, het maken van de genbank file en
    het schrijven van de afsluitende tag //
    """
    highest_stop = 0
    lowest_start = 2 ** 32
    stopwatch = Statistiek()
    print "GFF bestand openen"
    write_file('FEATURES\t\tLocation/Qualifiers\n')
    write_file("PLACEHOLDER\n")
    highest_stop, lowest_start = open_gff(highest_stop, lowest_start)
    insert_source(highest_stop, lowest_start)
    print "Origin schrijven"
    write_file(origin())
    sluiter = "//"
    write_file(sluiter)

    stopwatch.stop()

    print "Klaar!"
    print highest_stop, lowest_start


def insert_source(highest, lowest):
    readfile = open('extratest.gbk', 'r')
    lines = readfile.readlines()
    sourcestring = "\t source\t\t\t\t\t" + str(highest) + ".." + str(lowest) + "\n"
    lines[1] = sourcestring
    readfile.close()
    writefile = open('extratest.gbk', 'w')
    for line in lines:
        writefile.write(line)


def write_file(wfgenbank):
    """
    De functie opent het genbank bestand
    en voegt de parameter toe aan het bestand.
    """

    openfile = open('extratest.gbk', 'a')
    openfile.write(str(wfgenbank))
    openfile.close()


def open_gff(highest_stop, lowest_start):
    """
    Het gff bestand wordt geopend, de rijen in het bestand
    worden toegevoegd aan een nieuwe lijst. Deze wordt
    teruggegeven.
    """

    gff_file = open('test_def.gff', 'rb', buffering=1)
    reader = csv.reader(gff_file, delimiter="\t")
    print str(lowest_start)
    for row in reader:
        if "#" not in row[0]:
            if int(row[3]) > highest_stop:
                highest_stop = int(row[3])
            if int(row[4]) < lowest_start:
                lowest_start = int(row[4])
            make_gb(row, filters(row))

    return lowest_start, highest_stop


def make_gb(mgb_rijen, mgb_attrijen):
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

    featurelist = []

    mgb_attdict = mgb_attrijen
    finalstring = ''

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
    for i in range(len(featurelist)):
        genbank = featurelist[i]
        write_file(genbank)

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
main()

