'''
My solution to Rosalind Bioinformatics Problem 008

Title: Translating RNA into Protein
Rosalind ID: PROT
Rosalind #: 008
URL: http://rosalind.info/problems/prot
'''

from Bio.Seq import Seq
import Bio.Alphabet

f = open("data/rosalind_prot.txt", 'r')
seq = Seq(f.read().replace('\n', ''), Bio.Alphabet.IUPAC.unambiguous_rna)
f.close

protein = seq.translate(to_stop=True)

o = open("output/008_PROT.txt", 'w')
o.write(str(protein))
o.close()
