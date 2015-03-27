'''
My solution to Rosalind Bioinformatics Problem 023

Title: Enumerating k-mers Lexicographically
Rosalind ID: LEXF
Rosalind #: 023
URL: http://rosalind.info/problems/lexf

Goal to return all resampled permutations of a provided sequence in the
lexicographical order of the sequence.
'''

from itertools import product

f = open("data/rosalind_lexf.txt", 'r')
alphabet = list(f.readline().rstrip().split())
n = int(f.readline().rstrip())
f.close()

''' Used product instead of permutations to get resampling.
    Also sorting is unneccessary because the inner product
    produces the order of the sequence provided
'''
outhandle = open("output/023_LEXF.txt", 'w')
for perm in product(alphabet, repeat=n): #note, repeat must be specifically stated
    print >> outhandle, "".join(perm)
outhandle.close()
