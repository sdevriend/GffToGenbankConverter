from origin import origin
def generate_fasta():

    openfile = open('carp_pbjelly.fa','r')
    lines = openfile.readlines()
    gen = generator_test(lines)
    for x in range(len(lines)):
        next_gen = next(gen)
        writetofile( origin(next_gen[0], next_gen[1]))


def generator_test(lines):
    for line in lines:
        if ">" not in line:
            print line[0:60]
            print line[60:120]
            for x in xrange(0,len(line),60):
                yield [line[x:x+60],str(x+1)]
def writetofile(sequence):
    openfile = open('test_def2.gbk', 'a')
    openfile.write(sequence)
