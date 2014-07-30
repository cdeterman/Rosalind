'''
My solution to Rosalind Bioinformatics Problem 026

Title: Perfect Matchings and RNA Secondary Structures
Rosalind ID: PMCH
Rosalind #: 026
URL: http://rosalind.info/problems/pmch

Goal to number of possible perfect matchings of basepairs in a sequence.
Assumed to have the same number of A to U and C to G.
Given the recurrence relationship described in the problem, this can
be solved relatively easily withe factorials.  However, graph theory
has other methods for counting the number of perfect matches involving
adjacency matricies.  Something to potentially add on to this solution
for more general application.
'''

from collections import Counter
from math import factorial
from Bio import SeqIO

f = open("data/rosalind_pmch.txt", 'r')
raw_data = SeqIO.read(f, "fasta")
f.close()
seq = str(raw_data.seq)

counts = Counter(seq)

''' This is your recursive calculation
    You only use one from each pair of nucleotides otherwise it is
    just duplications.  Then, the idea is the same thing as a normal
    graph of (2n-1)*(2n-3)(2n-5)...
    The factorial of A (e.g. 3*2*1) times factorial of C (e.g. 2*1) = 12
'''
pn = factorial(counts["A"])*factorial(counts["C"])


o = open("output/027_PMCH.txt", 'w')
print >> o, pn
o.close()
