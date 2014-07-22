'''
My solution to Rosalind Algorithmic Heights Problem 003

Title: Degree Array
Rosalind ID: deg
Rosalind #: 003
URL: http://rosalind.info/problems/deg

Goal was to return the degree of each node (i.e. # of neighbors) from an edge
list formated graph.  Looking at the table, one can see that the # of neighbors
is simply how many times the node is present.  Therefore, one could simply convert
the array into a list and count the occurances of each node.
'''

# allows use of Python3.X print functionality
from __future__ import print_function
from collections import Counter
from itertools import chain

edges = []
with open('data/rosalind_deg.txt', 'r') as f:
    # Skip first line
    f.next() # NOTE - use next(f) in Python 3.X
    for line in f:
        edges.append(line.strip().split())
f.close()

my_list = []
for x in chain.from_iterable(edges): # flatten the lists
    my_list.append(x)

d = Counter(my_list) # count how many times each number present

o = open("output/Algorithmic_003_DEG.txt", 'w')
for key in sorted(d, key = int): # because keys are numbers, must be converted to int for sorting
    print(d[key], end = " ", file = o)
o.close()

