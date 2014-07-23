'''
My solution to Rosalind Bioinformatics Problem 017

Title: Inferring mRNA from Protein
Rosalind ID: mrna
Rosalind #: 017
URL: http://rosalind.info/problems/mrna

Goal to return number of possible mRNA strings which could have translated
the given protein, modulo 1000000.

This approach creates a new codon table with counts of possible rna/dna
sequences. Since we are not actually going to back translate, the specific table
is unneccesary and one can just use the generic codon table from Biopython.
'''

from Bio.SeqUtils.CodonUsage import SynonymousCodons
from Bio.SeqUtils import seq1

f = open("data/rosalind_mrna.txt", 'r')
protein = f.readline().rstrip()
f.close()

#Codon dictionary of just possibility counts (e.g. Met = 1, Ala = 4)
codonTable = {}
for key in SynonymousCodons.keys():
    # Use seq1 to convert three letter codes to one letter
    codonTable[seq1(key)] = len(SynonymousCodons[key])

# Amino acid combinations
aa_comb = 1
for aa in protein:
    aa_comb *= codonTable[aa]

# Times 3 for the 3 possible stop codons
# Modulo 1000000 to make final number reasonable sized
print aa_comb * 3 % 1000000



