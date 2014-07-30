'''
My solution to Rosalind Bioinformatics Problem 030

Title: Finding a Spliced Motif
Rosalind ID: SSEQ
Rosalind #: 030
URL: http://rosalind.info/problems/sseq

Goal - Provided indicies of the nucleotides of a string t in string s.
'''

from Bio import SeqIO

f = open("data/rosalind_sseq.txt", 'r')
records = list(SeqIO.parse(f, "fasta"))
f.close()

s = str(records[0].seq)
t = str(records[1].seq)

indicies = []
index = 0
for nt in t:
    s_temp = s[index:]
    # get index of nucleotide, add prior index to keep position
    index = s_temp.index(nt) + 1 + index
    indicies.append(index)

o = open("output/030_SSEQ.txt", 'w')
o.write(" ".join(map(str, indicies)))
o.close()
    
