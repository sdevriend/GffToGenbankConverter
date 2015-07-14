
from Merger import Merger

def origin():
    merger = Merger()
    seq = merger.get_fasta()
    lijst = [seq[x:x + 10] for x in range(0, len(seq), 10)]
    out = "ORIGIN\n"
    for x in range(0, len(lijst), 6):
        parts = 6
        if x + 6 > len(lijst):
            parts = len(lijst) - x
        out += ((("        %s" % str(x * 10 + 1))[-9:]) +
                ((" %s " * parts) % tuple(lijst[x:x + parts])) + "\n")
    return out


#print origin()
