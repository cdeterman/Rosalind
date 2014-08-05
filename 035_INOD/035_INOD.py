'''
My solution to Rosalind Bioinformatics Problem 035

Title: Counting Phylogenetic Ancestors
Rosalind ID: INOD
Rosalind #: 035
URL: http://rosalind.info/problems/inod

Goal to return number of internal nodes of any unrooted binary tree
having 'n' leaves.
'''


# number of leaves
f = open('/Rosalind/data/rosalind_inod.txt', 'r')
n = int(f.readline())
f.close()

'''
For an unrooted binary tree with 'n' leaves,
there will be n-2 internal nodes
'''
print n-2
