'''
My solution to Rosalind bioinformatics Problem 032

Title: Completing a Tree
Rosalind ID: TREE
Rosalind #: 032
URL: http://rosalind.info/problems/tree

Goal - Calculate the minimum number of edges required to complete a tree
with the provided adjacency matrix consisting of 'n' nodes.

It is important to remember the 'n' nodes as some will have no connections
at all.
'''

from itertools import chain


# function to see if item is in a sublist
def findItem(theList, item):
    for ind in theList:
        if item in ind:
            return str(theList.index(ind))


# function to create list of connections
def connections(sorted_adj_list):
    conns = []
    for index in xrange(0, len(adj_list_merge), 2):
        # see if first number in any sublist
        in_index = findItem(conns, adj_list_merge[index])
        # see if second number in any sublist
        in_index_2 = findItem(conns, adj_list_merge[index+1])
        if in_index:
            conns[int(in_index)].append(adj_list_merge[index+1])
        elif in_index_2:
            conns[int(in_index_2)].append(adj_list_merge[index])
        else:
            conns.append([adj_list_merge[index], adj_list_merge[index+1]])
    return conns

if __name__ == "__main__":
    f = open("~/Rosalind/data/rosalind_tree.txt", 'r')
    adj_list = [map(int, line.rstrip().split()) for line in f.readlines()]
    n = adj_list.pop(0)[0]
    adj_list.sort()
    f.close()

    adj_list_merge = list(chain.from_iterable(adj_list))
    conns = connections(adj_list_merge)
    conns_list = list(chain.from_iterable(conns))

    nodes = range(1, n+1)
    loners = []
    for i in nodes:
        if i not in conns_list:
            loners.append(i)
    lone_nodes = len(loners) - 1
    branches = len(conns)
    num_edges = lone_nodes + branches

    o = open("~/Rosalind/output/032_TREE.txt", 'w')
    print >> o, num_edges
    o.close()
