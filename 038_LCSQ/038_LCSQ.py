'''
My solution to Rosalind Bioinformatics Problem 038

Title: Finding a Shared Spliced Motif
Rosalind ID: LCSQ
Rosalind #: 038
URL: http://rosalind.info/problems/lcsq

Goal to return the longest noncontinous subsequence of two strings.  This
is essentially a longest subsequence problem.  I strongly suggest looking
at the wikipedia page for longest common subsequence problem.
'''

import numpy as np


def LCSQ(seq1, seq2):
    return backtrack(LCSQmatrix(seq1, seq2), seq1, seq2)


def LCSQmatrix(seq1, seq2):
    # create array of zeros
    C = np.zeros((len(seq1)+1, len(seq2)+1), dtype=np.int)
    for i in xrange(1, len(seq1)+1):
        for j in xrange(1, len(seq2)+1):
            # if elements in sequences match, add one to previous corner
            if seq1[i-1] == seq2[j-1]:
                C[i, j] = C[i-1, j-1] + 1
            else:
                # otherwise add maximum of two sides of corner
                C[i, j] = max(C[i, j-1], C[i-1, j])
    return C


def backtrack(C, seq1, seq2):
    # function to backtrack the sequence matrix
    lcsq = ''
    i, j = len(seq1), len(seq2)
    # run until reach end of sequence
    while i != 0 and j != 0:
        # if the nt in sequences match, add to lcsq
        if seq1[i-1] == seq2[j-1]:
            lcsq = seq1[i-1] + lcsq
            i -= 1
            j -= 1
        elif C[i, j] == C[i-1, j]:
            # if not matching and count next lower is equal decrease i
            # look at LCSQmatrix to understand the movement
            i -= 1
        else:
            # if not matching and next lower not equal, decrease j
            j -= 1
    return lcsq


'''
# A recursive backtrack function
# Errors out on long sequences because of recursion depth limitations
def backtrack(C, seq1, seq2, i, j):
    if i == 0 or j == 0:
        return ""
    if seq1[i-1] == seq2[j-1]:
        return backtrack(C, seq1, seq2, i-1, j-1) + seq1[i-1]
    else:
        if C[i,j] == C[i-1, j]:
            return backtrack(C, seq1, seq2, i-1, j)
        else:
            return backtrack(C, seq1, seq2, i, j-1)
'''


if __name__ == "__main__":
    from Bio import SeqIO

    input_handle = "/home/charles/Rosalind/data/rosalind_lcsq.txt"
    raw_data = list(SeqIO.parse(input_handle, 'fasta'))
    sequences = []
    for seq in raw_data:
        sequences.append(str(seq.seq))

    lcsq = LCSQ(sequences[0], sequences[1])
    o = open("/home/charles/Rosalind/output/038_LCSQ.txt", 'w')
    o.write(lcsq)
    o.close()
