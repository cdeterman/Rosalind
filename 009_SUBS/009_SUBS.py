'''
My solution to Rosalind Bioinformatics Problem 009

Title: Finding a Motif in DNA
Rosalind ID: SUBS
Rosalind #: 009
URL: http://rosalind.info/problems/subs
'''

# Basic Motif Searching
from Bio import motifs
from Bio.Seq import Seq
import Bio.Alphabet

f = open("data/rosalind_subs.txt", 'r')
raw_seq = f.readline().rstrip()
motif = f.readline().rstrip()
f.close()

# motif instances must be in a list
instances = [Seq(motif)]
m = motifs.create(instances)

seq = Seq(raw_seq, Bio.Alphabet.IUPAC.unambiguous_dna)

# only output locations
locations = []
for pos in m.instances.search(seq):
    locations.append(pos[0]+1) # changes default from \n

o = open("output/009_SUBS.txt", 'w')
o.write(" ".join(map(str, locations)))
o.close()

''' If would like to have both position and the motif displayed.
    This is helpful if searching multiple motifs '''
#for pos, seq in m.instances.search(seq):
#    print pos+1, seq.tostring() # add 1 becuase of 0-based numbering
