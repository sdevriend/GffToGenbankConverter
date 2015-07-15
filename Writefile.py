def write_file(wfgenbank):
    """
    De functie opent het genbank bestand
    en voegt de parameter toe aan het bestand.
    """

    openfile = open('test_def2.gbk', 'a')
    openfile.write(str(wfgenbank))
    openfile.close()