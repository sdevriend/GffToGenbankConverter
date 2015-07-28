def write_file(wfgenbank, gbk_save):
    # aanpassing: gbk_invoer die hieronder aangepast kan worden of
    # in de main van gff script.
    """
    De functie opent het genbank bestand
    en voegt de parameter toe aan het bestand.
    """
    #openfile = open('test_def2.gbk', 'a')
    openfile = open(gbk_save, 'a')
    openfile.write(str(wfgenbank))
    openfile.close()

def write_list(lijst, gbk_save):
    #gbk_file = open('test_def2.gbk', 'a')
    gbk_file = open(gbk_save, 'a')
    for itemlijst in lijst:
        for item in itemlijst:
            gbk_file.write(str(item))

    gbk_file.close()


def make_gbk_file(gbk_save):
    """
    De functie maakt de gbk file aan. Het overschrijft als de file
    bestaat. De gebruiker is hiervoor gewaarschuwd in de interface.

    Input:
    gbk_save: Invoer naam van genbank bestandsnaam.
    """
    mgf_openfile = open(gbk_save, "w")
    mgf_openfile.close()
