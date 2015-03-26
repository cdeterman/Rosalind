'''
My solution to Rosalind Algorithmic Heights Problem 007

Title: Merge Two Sorted Arrays
Rosalind ID: MER
Rosalind #: 007
URL: http://rosalind.info/problems/mer
'''

from collections import Counter
import os


if __name__ == '__main__':
    # read data
    f =  open(os.path.join(os.path.split(os.getcwd())[0], "data", "rosalind_mer.txt"), 'r')
    data = [map(int, line.rstrip().split()) for line in f.readlines()]

    A_len = data.pop(0)
    A = data.pop(0)
    B_len = data.pop(0)
    B = data.pop(0)

    C = A + B
    C.sort()

    # save output file
    outhandle = open(
        os.path.join(
            os.path.split(
                os.getcwd())[0],
            "output", "Algorithmic_007.txt"),
        'w')
    print >> outhandle, " ".join(map(str, C))
    outhandle.close()
