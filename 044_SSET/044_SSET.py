'''
My solution to Rosalind Bioinformatics Problem 044
Title: Counting Subsets
Rosalind ID: SSET
Rosalind #: 044
URL: http://rosalind.info/problems/sset
'''

import os

# read data
f =  open(
    os.path.join(
        os.path.split(
            os.getcwd())[0],
        "data", "rosalind_sset.txt"),
    'r')

n = int(f.readline())
f.close()

# this is simply 2^N mod 1000000
print 2**n % 1000000

# save output file
outhandle = open(
    os.path.join(
        os.path.split(
            os.getcwd())[0],
        "output", "044_sset.txt"),
    'w')
print >> outhandle, str(2**n % 1000000)
outhandle.close()
