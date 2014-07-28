'''
My solution to Rosalind Bioinformatics Problem 024

Title: Longest Increasing Subsequence
Rosalind ID: LGIS
Rosalind #: 024
URL: http://rosalind.info/problems/lgis

Goal to return the longest increasing subsequence and longest decreasing
subsequence from a permutation of length n.
'''

#perm = [5,1,4,2,3]

f = open("C:/Users/Chaz/Rosalind/data/test2.txt", 'r')
n = f.readline().rstrip()
data = f.readline().rstrip().split()
f.close()

# create list of short subsequences
#increasing = []
#decreasing = []
'''
for start in xrange(len(perm)-1):
    for end in xrange(start+1, len(perm)):
        if perm[start] < perm[end]:
            increasing.append([perm[start], perm[end]])
        elif perm[start] > perm[end]:
            decreasing.append([perm[start], perm[end]])

increasing = sorted(increasing)
decreasing = sorted(decreasing, reverse = True)
'''
def BS(S, data, value):
    '''Use a binary search to return the index of the smallest item
    in 'S' greater than or equal to 'value'.'''
    original_S = S
    while len(S)>1:
    # index is the exact middle if odd, and the lower value if even.
        mid = int(ceil(len(S)/2.0 - 1))
        if data[S[mid]] < value:
            S = S[mid+1:]

        else:
            S = S[:mid+1]
    return original_S.index(S[0])

#mid = len(increasing)/2
#print mid
from math import ceil
S = [0]
parent = [None]*len(data)

for index in range(1, len(data)):
    if data[index] > data[S[len(S)-1]]:
        parent[index] = S[len(S)-1]
        S.append(index)
    else:
        update_index = BS(S, data, data[index])
        print update_index
        
        #S[update_index] = index
        #parent[index] = S[update_index-1]
#print S
'''
# combine overlapping sequences to get longest sequence
def lgis(perms, direction="increasing"):
    result = []
    if direction == "increasing":
        for start in xrange(len(perms)):
            for end in xrange(start,len(perms)):
                if perms[start][-1] <= perms[end][0] and perms[start][-1] < perms[end][-1]:
                    if not result: #if blank, fill in beginning
                        result.append(perms[start])
                        result.append(perms[end])
                    else:
                        result.append(perms[end])

    elif direction == "decreasing":
        for start in xrange(len(perms)):
            for end in xrange(start,len(perms)):
                if perms[start][-1] >= perms[end][0]:
                    if result:
                        if result[-1][-1] > perms[end][-1]:
                            result.append(perms[end])
                    elif not result: #if blank, fill in beginning
                        result.append(perms[start])
                        result.append(perms[end])
                    else:
                        result.append(perms[end])

    return rm_duplicates(flatten(result))

def flatten(lst):
	return sum( ([x] if not isinstance(x, list) else flatten(x)
		     for x in lst), [] )

def rm_duplicates(seq):
    seen = set()
    seen_add = seen.add
    return [ x for x in seq if not (x in seen or seen_add(x))]

outhandle = open("C:/Users/Chaz/Rosalind/output/025_LGIS.txt", 'w')
#print " ".join(map(str, lgis(increasing)))

print >> outhandle, " ".join(map(str, lgis(increasing)))
print >> outhandle, " ".join(map(str, lgis(decreasing, direction = "decreasing")))
outhandle.close()
'''
