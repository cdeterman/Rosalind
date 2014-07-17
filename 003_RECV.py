'''
My solution to Rosalind Bioinformatics Problem 003

Title: Complementing a Strand of DNA
Rosalind ID: RNA
Rosalind #: 003
URL: http://rosalind.info/problems/revc
'''

from Bio.Seq import Seq
import Bio.Alphabet

# open txt file with sequence to transcribe
f = open('C:/Users/Chaz/python_code/Rosalind/data/rosalind_revc.txt', 'r')
# read all lines by removing newline character
data = f.read().replace('\n', '')
# close file
f.close()

# assign sequence as a DNA sequence
t = Seq(data, Bio.Alphabet.IUPAC.unambiguous_dna)
# use transcribe function
o = open('C:/Users/Chaz/python_code/Rosalind/output/003_REVC.txt', 'w')
o.write(str(t.reverse_complement()))
o.close()
