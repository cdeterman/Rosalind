'''
My solution to Rosalind Bioinformatics Problem 020

Title: Calculating Protein Mass
Rosalind ID: PRTM
Rosalind #: 020
URL: http://rosalind.info/problems/prtm

Goal to return the weight of a protein sequence from the monoisotopic mass
table.
'''

# Create mass dictionary from mass table file
f = open("C:/Users/Chaz/Rosalind/data/protein_mass_table.txt", 'r')
aa_mass_dict = {}
for line in f.readlines():
    data = line.rstrip().split()
    aa_mass_dict[data[0]] = data[1]
f.close()

# open sequence
f = open("C:/Users/Chaz/Rosalind/data/rosalind_prtm.txt", 'r')
protein = f.readline().rstrip()
f.close()

mw = 0
for letter in protein: # iterate through each letter and add weight of aa
    mw += float(aa_mass_dict[letter])

print mw

'''
Personally, the method below I would have preferred.  The Biopython method
allows for access to several more aspects of the protein. However, there appears
to be some rounding error in addition to adding a water molecule.  The water
molecular weight can be removed but the rounding error doesn't appear to have
an accessible solution.  As such, the method above works simply enough for a
user specific dictionary of weights.
'''

'''
from Bio.SeqUtils.ProtParam import ProteinAnalysis
protein_analysis = ProteinAnalysis(protein)
print protein_analysis.molecular_weight()
'''
