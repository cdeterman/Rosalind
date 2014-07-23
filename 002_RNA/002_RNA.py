'''
My solution to Rosalind Bioinformatics Problem 002

Title: Transcribing DNA into RNA
Rosalind ID: RNA
Rosalind #: 002
URL: http://rosalind.info/problems/rna
'''

from Bio.Seq import Seq
import Bio.Alphabet

# open txt file with sequence to transcribe
f = open('data/rosalind_rna.txt', 'r')
# read all lines by removing newline character
data = f.read().replace('\n', '')
# close file
f.close()

# assign sequence as a DNA sequence
t = Seq(data, Bio.Alphabet.IUPAC.unambiguous_dna)
# use transcribe function
o = open('output/002_RNA.txt', 'w')
o.write(str(t.transcribe()))
o.close()
