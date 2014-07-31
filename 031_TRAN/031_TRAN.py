'''
My solution to Rosalind Bioinformatics Problem 031

Title: Transitions and Transversions
Rosalind ID: TRAN
Rosalind #: 031
URL: http://rosalind.info/problems/tran

Goal - Provide the ratio of transitions to transversions for two provided
sequences.
'''

from Bio import SeqIO

f = open("~/Rosalind/data/rosalind_tran.txt", 'r')
raw_data = list(SeqIO.parse(f, "fasta"))
f.close()

seq1 = raw_data[0].seq
seq2 = raw_data[1].seq

transitions = 0
transversions = float(0)
for nt in xrange(len(seq1)):
    if seq1[nt] == seq2[nt]:
        continue
    elif seq1[nt] == "A" and (seq2[nt] == "C" or seq2[nt] == "T"):
        transversions += 1
    elif seq1[nt] == "G" and (seq2[nt] == "C" or seq2[nt] == "T"):
        transversions += 1
    elif seq1[nt] == "C" and (seq2[nt] == "A" or seq2[nt] == "G"):
        transversions += 1
    elif seq1[nt] == "T" and (seq2[nt] == "A" or seq2[nt] == "G"):
        transversions += 1
    else:
        transitions += 1

print transitions/transversions
