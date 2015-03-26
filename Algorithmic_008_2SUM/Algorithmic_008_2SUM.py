'''
My solution to Rosalind Algorithmic Heights Problem 008

Title: 2SUM
Rosalind ID: 2sum
Rosalind #: 008
URL: http://rosalind.info/problems/2sum
'''

import os

def two_sum(A):
    # empty dictionary
    indices = {}

    # iterate through array elements
    for t in range(len(A)):
        # check if 'opposite sign' exists in remainder
        if -A[t] in A[t+1:]:
            # check which element sums to zero
            for s in xrange(t+1, len(A)):
                if(A[t] + A[s] == 0):
                    # returns indices (+1 for Rosalind)
                    return [t+1, s+1]
                
    # loop failed so return -1
    return [-1]


if __name__ == '__main__':
    # read data
    f =  open(
        os.path.join(
            os.path.split(os.getcwd())[0],
            "data", "rosalind_2sum.txt")
        , 'r')

    k,n = f.readline().rstrip().split()
    data = [map(int, line.strip().split()) for line in f.readlines()]

    for d in data:
        print " ".join(map(str, two_sum(d)))
