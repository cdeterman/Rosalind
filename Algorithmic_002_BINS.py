'''
My solution to Rosalind Algorithmic Heights Problem 002

Title: Binary Search
Rosalind ID: BINS
Rosalind #: 002
URL: http://rosalind.info/problems/bins

The problem was to return index of array (ol) of ul[i] and
return -1 if k[i] is not in the array.

The solution provided here is what I still consider a long coded way, for a
higher programming language anyway.  I initially would have preferred the
solution I also have at the bottom of this script but have run into a bug
that is currently vexing me (please see below for details).
'''

f = open("data/rosalind_bins.txt", 'r')
n = int(f.readline().strip())
m = int(f.readline().strip())
ol = list(map(int, f.readline().strip().split(" ")))
ul = list(map(int, f.readline().strip().split(" ")))
f.close()

indicies = []
for item in ul:
    value = False
    start = 0
    end = n-1

    # continue search until found or exhaust possibilities
    while value == False:
        if end < start:
            indicies.append(-1)
            value = True
        else:
            mid = (sum([start, end])/2)
            if item < ol[mid]: # less than, want lower half of dataset
                start = start
                end = mid - 1
            elif item > ol[mid]: # greater than, want upper half of dataset
                start = mid+1
                end = end
            else:
                indicies.append(mid+1)
                value = True

o = open("output/Algorithmic_002_BINS.txt", 'w')
print >> o, " ".join(map(str, indicies)) #integers must be converted to strings for join
o.close()

'''
The following is another example with code much shorter.  However, it doesn't
give the correct answer.  This is a complete mystery to me and I have no idea
as to why it sometimes gives the correct index and others it is off by 1.  If
anyone has any clue as to why this is the case, please feel free to post a note.
'''
'''
indicies = []
for i in ul[0:10]:
    try:
        indicies.append(ol.index(i)+1)
    except ValueError:
        indicies.append(-1)
print indicies
'''
