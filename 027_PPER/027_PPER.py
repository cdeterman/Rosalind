'''
My solution to Rosalind Bioinformatics Problem 027

Title: Partial Permutations
Rosalind ID: PPER
Rosalind #: 027
URL: http://rosalind.info/problems/pper

Goal to return number of partial permutations of length r
from a collection of length n
'''

from math import factorial

def numPartialPerms(n,r):
    np = (factorial(n)/factorial(n-r)) % 1000000
    return np

''' Note - easy way to generate all said permutations
from itertools import permutations
perms = permutations(range(1,n), r)
'''

if __name__ == '__main__':
    f = open("data/rosalind_pper.txt", 'r')
    n,r = map(int, f.readline().split())
    f.close()
    print numPartialPerms(n,r)
