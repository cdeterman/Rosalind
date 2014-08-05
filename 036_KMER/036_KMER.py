'''
My solution to Rosalind Bioinformatics Problem 036

Title: k-Mer Composition
Rosalind ID: KMER
Rosalind #: 036
URL: http://rosalind.info/problems/kmer

Goal to return number of each possible kmer in the given sequence in
lexicographical order.
'''

from Bio import SeqIO
from itertools import product
import re

# generate all possible 4-mers
alphabet = ["A", "C", "G", "T"]
# generates the cartesian products of length 'n' (e.g. 4)
perms = product(alphabet, repeat=4)
kmers = []
for i in perms:
    kmers.append("".join(i))

f = open("/Rosalind/data/rosalind_kmer.txt", 'r')
raw = SeqIO.read(f, "fasta")
f.close()

'''
The following uses a little regex to count all overlapping
occurances of each kmer.  The syntax for finding all of them
is re.findall((?=string), full_string)
'''
o = open("/Rosalind/output/036_KMER.txt", 'w')
for kmer in kmers:
    print >> o, len(re.findall(''.join(['(?=', kmer, ')']), str(raw.seq))),
o.close()
