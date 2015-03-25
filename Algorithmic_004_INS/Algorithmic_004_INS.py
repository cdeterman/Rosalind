import os

def insertionSortCount(A):
    swaps = 0
    for i in xrange(1, len(A)):
        k = i
        while k > 0 and A[k] < A[k-1]:
            A[k-1], A[k] = A[k], A[k-1]
            k -= 1
            swaps += 1
    return swaps


if __name__ == '__main__':
    # read data
    f = open(os.path.join(os.path.split(os.getcwd())[0], "data", "rosalind_ins.txt")).readlines()
    f = [x.rstrip('\n') for x in f]

    # get the array of numbers
    A = f[1]

    # run insertionSortCount
    print insertionSortCount(map(int, A.split()))
    
    
