'''
My solution to Rosalind Bioinformatics Problem 039

Title: Ordering Strings of Varying Length Lexicographically
Rosalind ID: LEXV
Rosalind #: 039
URL: http://rosalind.info/problems/lexv

Goal to return all repeated permutations of lengths 1-'n' from a
list of letters in lexicographical order.
'''

from itertools import product

f = open("/Rosalind/data/rosalind_lexv.txt", 'r')
s = ''.join(f.readline().rstrip().split())
n = int(f.readline().rstrip())

perms = []
for perm in product(s, repeat=n):
    for j in range(1, n+1):
        if perm[:j] not in perms:
            perms.append(perm[:j])

o = open("/Rosalind/output/039_LEXV.txt", 'w')
for i in perms:
    print >> o, ''.join(i)
o.close()
