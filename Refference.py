annotationdict = {}
def refference():
    reffile = open("annotest.csv", 'r')
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
    for key in annotationdict.keys():
        # print key
        if key == paramkey:
            return str(annotationdict[key][0])
refference()
print (check("cypCar_00000001-RA"))
