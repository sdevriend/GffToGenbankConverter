from origin import origin
def generate_fasta(fasta_name, gbk_name):

    #openfile = open('D:\\ncbi_data\\software\\Converter\\carp_pbjelly.fa','r')
    openfile = open(fasta_name, 'r')
    lines = openfile.readlines()
    openfile.close()
    gen = generator_test(lines)
    #openfile = open('test_def2.gbk', 'a')
    openfile = open(gbk_name, 'a')
    for x in range(len(lines)):
        next_gen = next(gen)
        openfile.write( origin(next_gen[0], next_gen[1]))
    openfile.close()


def generator_test(lines):
    for line in lines:
        if ">" not in line:
            ##print line[0:60]
            ##print line[60:120]
            for x in xrange(0,len(line),60):
                yield [line[x:x+60],str(x+1)]

def writetofile(sequence, gbk_name):
    #openfile = open('test_def2.gbk', 'a')
    openfile = open(gbk_name, 'a')
    openfile.write(sequence)
    openfile.close()
