'''
My solution to Rosalind Algorithmic Heights Problem 005

Title: Double-Degree Array
Rosalind ID: DDEG
Rosalind #: 005
URL: http://rosalind.info/problems/ddeg
'''

import numpy as np
import os

def adjacency_list(k, edge_u, edge_v):
    out = {}
    for i in xrange(1, k+1):
        idx1 = np.where(edge_u == i)[0]
        idx2 = np.where(edge_v == i)[0]
        out[i] = np.concatenate((edge_u[idx2], edge_v[idx1]), axis=0)
    return out


if __name__ == '__main__':
    # read data
    f =  open(os.path.join(os.path.split(os.getcwd())[0], "data", "rosalind_ddeg.txt"), 'r')
    adj_list = [map(int, line.rstrip().split()) for line in f.readlines()]
    n = adj_list.pop(0)[0]

    # create numpy arrays
    l = len(adj_list)
    edge_u = np.empty(l, dtype=np.int)
    edge_v = np.empty(l, dtype=np.int)

    i = 0
    for line in adj_list:
        edge_u[i] = line[0]
        edge_v[i] = line[1]
        i += 1

    f.close()
            
    # convert to adjacency list
    o = adjacency_list(n, edge_u, edge_v)

    # sum degrees of neighbors
    counts = np.empty(n, dtype=np.int)
    for key in o:
        elems = o[key]
        count = 0
        for i in range(len(elems)):
            count += len(o[elems[i]])
        counts[key-1] = count

    # save output file
    outhandle = open(os.path.join(os.path.split(os.getcwd())[0], "output", "Algorithmic_005.txt"), 'w')
    print >> outhandle, ' '.join(map(str, counts))
    outhandle.close()










