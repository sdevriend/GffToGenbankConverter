annotationdict = {}
def refference(annot_file):

    ##reffile = open("annotest.csv", 'r')
    ##reffile = open('D:\\ncbi_data\\software\\Converter\\annotest.csv', 'r')
    reffile = open(annot_file, 'r')
    lines = reffile.readlines()
    annotations = []
    for line in lines:
        annotations.append(line.split(';'))
        # print line
    # print annotations
    global annotationdict
    for annotation in annotations:
        annotationdict.update({annotation[0]: [annotation[1], annotation[2]]})
    # print annotationdict
    return annotationdict





def check(paramkey):
    paramkey += "-RA"
    for key in annotationdict.keys():
        # print key
        if key == paramkey:
            return str(annotationdict[key][0])
#refference()
#print (check("cypCar_00000001-RA", "bla"))
