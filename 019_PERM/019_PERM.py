'''
My solution to Rosalind Bioinformatics Problem 019

Title: Enumerating Gene Orders
Rosalind ID: PERM
Rosalind #: 019
URL: http://rosalind.info/problems/perm

Goal to return the total number and all possible permutations of an iterative
sequence of length 'n'.
'''

from itertools import permutations
from math import factorial

n = 6
seq = range(1, n+1)

o = open("C:/Users/Chaz/Rosalind/output/019_PERM.txt", 'w')

# how many possible combinations
print >> o, factorial(n)

# evaluate all permutations
for perm in permutations(seq):
    print >> o, " ".join(map(str, perm))

o.close()
