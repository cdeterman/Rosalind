'''
My solution to Rosalind Bioinformatics Problem 001

Title: Counting DNA Nucleotides
Rosalind ID: DNA
Rosalind #: 001
URL: http://rosalind.info/problems/dna
'''

f = open("C:/Users/Chaz/python_code/Rosalind/data/rosalind_dna.txt", 'r')
raw_seq = f.readline().rstrip()
f.close()

print raw_seq.count("A"),
print raw_seq.count("C"),
print raw_seq.count("G"),
print raw_seq.count("T")
