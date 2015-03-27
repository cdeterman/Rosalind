'''
My solution to Rosalind Bioinformatics Problem 022

Title: RNA Splicing
Rosalind ID: SPLC
Rosalind #: 022
URL: http://rosalind.info/problems/splc

Goal to return translated protein of a dna strand after removing a list of
introns.
'''

from Bio import SeqIO
from Bio.Seq import Seq

f = open("data/rosalind_splc.txt", 'r')

# simple parsing to have sequences as strings for subsequent splicing
dna = ''
introns = []
count = 1
for record in SeqIO.parse(f, "fasta"):
    if count == 1: # first record is the DNA string
        dna = str(record.seq)
    else: # collect the introns
        introns.append(str(record.seq))
    count += 1
f.close()

for intron in introns:
    if intron in dna: # if intron present, remove from dna string
        dna = dna.replace(intron, "")

o = open("output/022_SPLC.txt", 'w')
# convert to Seq object and translate to protein
print >> o, Seq(dna).translate(to_stop=True)
o.close()


