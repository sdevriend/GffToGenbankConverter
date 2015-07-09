import csv


def main():
	'''
	De functie roept de andere functies aan:
	het openen van de file, het maken van een multidimensionale lijst,
	het filteren van de attributen, het maken van de genbank file en 
	het schrijven van de afsluitende tag //
	'''
    readlist = open_gff()
    rows = make_list(readlist)

    att_rows = filters(readlist)

    #print att_rows[30]
    make_gb(rows, att_rows)
    sluiter = "//"
    writeFile(sluiter)
def writeFile(wfGenBank):
	'''
	De functie opent het genbank bestand
	en voegt de parameter toe aan het bestand.
	'''
    openFile = open('test_def.gbk','a')
    openFile.write(str(wfGenBank))
    openFile.close()

def open_gff():
	'''Het gff bestand wordt geopend, de rijen in het bestand
	worden toegevoegd aan een nieuwe lijst. Deze wordt
	teruggegeven.
	'''	
    with open('test_def.gff', 'rb') as gff_file:
        reader = csv.reader(gff_file, delimiter="\t")
        readlijst = []
        for row in reader:

            if "#" not in row[0]:

                readlijst.append(row)

    return readlijst
def make_list(ml_readlijst):
	''' 
	Een lijst met daarin 8 lijsten wordt gemaakt.
	De comments met een # worden gefilterd en de attributen
	worden toegevoegd aan de lijst.
	'''
    rijen = [[] for x in range(9)]


    for row in ml_readlijst:
        if "#" not in row[0]:

            for column in range(len(row)):

                value = row[column]
                x = ml_readlijst.index(row)
                y = column
                rijen[y].append(value)

    return rijen


def make_gb(mgb_rijen, mgb_attRijen):
	'''
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
	'''
    gb_string = 'FEATURES\t\tLocation/Qualifiers\n'
    
    source_1 = "\t %5s \t" %'source' +min(mgb_rijen[3])+".."+max(mgb_rijen[4])+"\n"
    gb_string += source_1
    writeFile(gb_string)
    features = []

    for instance in range(len(mgb_rijen[2])):

        featurelist = []

        mgb_attDict = mgb_attRijen[instance]
        finalString = ''

        #Eerste: feature

        if not "complement" in mgb_rijen[8][instance]:
            feature = str("\t %-20s \t %s..%s\n"%(mgb_rijen[2][instance],
                            mgb_rijen[3][instance],mgb_rijen[4][instance]))
        else:
            feature = str("\t %-6s \t complement(%s..%s)\n"%
                        (mgb_rijen[2][instance],
                        mgb_rijen[3][instance],mgb_rijen[4][instance]))
        finalString+=feature
        #Tweede: gene
        gene = str("\t\t\t\t /gene=\"%s\"\n")%mgb_attDict.get('id')

        finalString += gene
        #Derde: note
        note = mgb_attDict.get('note')

        if note != None:

            finalString+= "\t\t\t\t /note=\"%s\"\n"%note
        #Vierde: db_xref
        db_xref = mgb_attDict.get('db_xref')
        if db_xref != None:
            finalString += "\t\t\t\t /note=\"%s\"\n"%db_xref
        
        featurelist.append(finalString)
        #features.append(featurelist)
        for i in range(len(featurelist)):
            genBank =  featurelist[i]
            writeFile(genBank)


    return featurelist
def filters(rijen, versie=3):
	'''
	De functie maakt een dictionary van de attributenkolom en geeft deze terug
	'''
    splitter = {2: " ", 3:";"}
    out = []


    for rij in rijen:
    
        if "#" not in rij[0]:
            current = rij[8].split(splitter[versie])

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
                att = {"id": None, "name": None, "alias": None, "parent": None,
                        "target": None, "gap": None, "derives_from": None,
                        "note": None, "dbxref": None, "ontology_term": None}
            for waarde in current:
                current2 = waarde.split("=")
                if current2[0].lower() in att:

                    try:
                        att[current2[0].lower()] = current2[1]
                    except KeyError:
                        print "onbekend attribuut"
                    except IndexError:
                        print "missende data"
            out +=[att]

    return out

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
