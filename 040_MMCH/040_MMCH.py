'''
My solution to Rosalind Bioinformatics Problem 040

Title: Maximum Matchings and RNA Secondary Structures
Rosalind ID: MMCH
Rosalind #: 040
URL: http://rosalind.info/problems/mmch

Goal to return the number of possible maximum matchings of
basepair edges in a given rna sequence.
'''

from Bio import SeqIO
from math import factorial

f = open("/Rosalind/data/rosalind_mmch.txt", 'r')
raw = SeqIO.read(f, "fasta")
f.close()

seq = str(raw.seq)


# also in my combination functions script in 'scripts'
def nPr(n, r):
    return factorial(n)/factorial(n-r)

AU = []
for nt in 'AU':
    AU.append(seq.count(nt))
GC = []
for nt in 'GC':
    GC.append(seq.count(nt))

''' Since we don't care about overlapping edges, we can just
    look at the number of permutations.  They can only be
    a length of the minimum between complementary base pairs.
'''
num_matches = nPr(max(AU), min(AU))*nPr(max(GC), min(GC))

o = open("/Rosalind/output/040_MMCH.txt", 'w')
o.write(str(num_matches))
o.close()
