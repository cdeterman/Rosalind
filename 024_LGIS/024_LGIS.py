'''
A solution to a ROSALIND bioinformatics problem.

Problem Title: Longest Increasing Subsequence
Rosalind ID: LGIS
Rosalind #: 024
URL: http://rosalind.info/problems/lgis/

Goal - Provided a permutation sequence and should return the longest increasing
and longest decreasing subsequences.

I drew heavily from other people's code for this solution and therefore
don't take much credit for its' implementation.  As such, there
currently is not much novelty herein.  I created a brute-force method but
it is extremely inefficient and would not have much use.  I have some potential
other ideas but at the moment here is a very solid answer only slightly modified
from other very talented programmers.
'''

from math import ceil

# Binary search to decrease time and computation
def BS(S, data, value):
    original_S = S
    while len(S)>1:
        # index is the exact middle if odd, and the lower value if even.
        index = int(ceil(len(S)/2.0 - 1))
        if data[S[index]] < value:
            S = S[index+1:]
        else:
            S = S[:index+1]
    return original_S.index(S[0])

def LongestIncSubstring(data):
    '''Returns an ordered list of the longest increasing substring.'''
    S = [0]
    parent = [None]*len(data)
    for index in range(1,len(data)):
        if data[index] > data[S[len(S)-1]]:
            parent[index] = S[len(S)-1]
            S.append(index)
        else:
            update_index = BS(S, data, data[index])
            S[update_index] = index
            parent[index] = S[update_index-1]

    ''' Get the indicies of each element in the longest increasing
        subsequence in reverse order.'''
    LIS = [S[len(S)-1]]
    for i in range(0,len(S)-1):
        LIS.append(parent[LIS[len(LIS)-1]])

    # Convert indicies to values and reverse.
    LIS = [data[i] for i in LIS]
    LIS.reverse()

    return LIS


if __name__ == '__main__':

    f = open('data/rosalind_lgis.txt')
    f.next()
    perm = map(int, f.readline().rstrip().split())
    f.close()

    LIS = map(str, LongestIncSubstring(perm))

    ''' The longest decreasing subsequence is equal to
        LIS of -1*permutation.'''
    negperm = [-1*i for i in perm]
    LDS = map(str, [-1*i for i in LongestIncSubstring(negperm)])

    outhandle = open('output/024_LGIS.txt', 'w')
    outputhandle.write(' '.join(LIS) + '\n')
    outputhandle.write(' '.join(LDS))
    outhandle.close()
