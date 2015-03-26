'''
My solution to Rosalind Algorithmic Heights Problem 009

Title: Breadth-First Search
Rosalind ID: BFS
Rosalind #: 009
URL: http://rosalind.info/problems/bfs
'''

import os
from collections import defaultdict

def bfs(edges, n):
    # Build the graph.
    G = defaultdict(list)
    
    for n1, n2 in edges:
        G[n1].append(n2)

    # All min_dist set at -1 unless possible to reach
    min_dist = [0] + [-1]*(n-1)
    
    vertices = range(2, n+1)
    Q = [1]

    # search until Q is empty
    while Q:
        # remove current node
        current = Q.pop(0)

        # check all connections for current node
        for edge in G[current]:
            # check if edge hasn't been discovered yet
            if edge in vertices:
                # add new edge
                Q.append(edge)
                # discard edge that has been visited
                vertices.remove(edge)
                # Rosalind is 1-based indexing
                min_dist[edge-1] = min_dist[current-1] + 1

    return min_dist
                

if __name__ == '__main__':
    # read data
    f =  open(
        os.path.join(
            os.path.split(
                os.getcwd())[0],
            "data", "rosalind_bfs.txt"),
        'r')
    edge_list = [map(int, line.rstrip().split()) for line in f.readlines()]
    n = edge_list.pop(0)[0]

    min_dists = bfs(edge_list, n)
    #print ' '.join(map(str, min_dists))

    # save output file
    outhandle = open(
        os.path.join(
            os.path.split(
                os.getcwd())[0],
            "output", "Algorithmic_009.txt"),
        'w')
    print >> outhandle, ' '.join(map(str, min_dists))
    outhandle.close()
    
