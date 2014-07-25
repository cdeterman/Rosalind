'''
My solution to Rosalind Bioinformatics Problem 024

Title: Enumerating k-mers Lexicographically
Rosalind ID: LEXF
Rosalind #: 024
URL: http://rosalind.info/problems/lexf

Goal to return all resampled permutations of a provided sequence in the
lexicographical order of the sequence.
'''

from itertools import product

f = open("C:/Users/Chaz/Rosalind/data/rosalind_lexf.txt", 'r')
alphabet = list(f.readline().rstrip().split())
n = int(f.readline().rstrip())
f.close()

''' Used product instead of permutations to get resampling.
    Also sorting is unneccessary because the inner product
    produces the order of the sequence provided
'''
outhandle = open("C:/Users/Chaz/Rosalind/output/024_LEXF.txt", 'w')
for perm in product(alphabet, repeat=n):
    print >> outhandle, "".join(perm)
outhandle.close()
