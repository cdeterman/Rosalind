'''
My solution to Rosalind Bioinformatics Problem 043
Title: Matching Random Motifs
Rosalind ID: RSTR
Rosalind #: 043
URL: http://rosalind.info/problems/rstr
'''

import os
import sys
from random import random



if __name__ == '__main__':
    # read data
    f =  open(
        os.path.join(
            os.path.split(
                os.getcwd())[0],
            "data", "rosalind_rstr.txt"),
        'r')

    # first line contains n and gc content
    line1 = f.readline().split()
    n,prob_gc = int(line1[0]), float(line1[1])

    # second line contains dna string
    s = f.readline().strip()

    # close the file
    f.close()

    # Probability A or T
    prob_at = 1-prob_gc

    # General idea
    # 1 - P(not match s)
    # for each nucl P(not correct nucl)

    # Example with coin flip, N trials
    # Prob at least one head
    # Pr(not all tails) = 1 - Pr(all tails)
    # Pr(not all tails) = 1 - (.5)**N

    # same thing as 028_PROB
    prob = 1
    for nucleotide in s:
        if nucleotide == 'A' or nucleotide == 'T':
            prob *= prob_at/2
        elif nucleotide == 'C' or nucleotide == 'G':
            prob *= prob_gc/2
        else:
            sys.exit('strange nucleotide')

    # use complement to match coin example above
    print 1-(1-prob)**n
