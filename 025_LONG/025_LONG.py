'''
My solution to Rosalind Bioinformatics Problem 025

Title: Genome Assembly as Shortest Superstring
Rosalind ID: LONG
Rosalind #: 025
URL: http://rosalind.info/problems/long

Goal - Provided a list of sequencing reads and return a single string containing all
the given strings.

MANY ASSUMPTIONS!!!
1. No errors
2. No nested overlap, only on the ends
3. All reads will overlap
4. Reads will overlap by more than half their length
'''

from Bio import SeqIO
import pandas as pd

def assemble(seqs):
    # matrix of overlap lengths
    overlaps = getAllOverlaps(seqs)
    # list of reads in order of alignment
    seq_order = findOrder(overlaps)
    
    final_sequence = str(seqs[seq_order[0]].seq)
    for index in xrange(1, len(seq_order)):
        # find length of overlap
        over_len = int(overlaps[seq_order[index-1]][seq_order[index]])
        # remove overlap from first sequence and append next
        final_sequence = final_sequence[:-over_len] + str(seqs[seq_order[index]].seq)
    return final_sequence

def findOrder(overlaps):
    seq_order = [findStartRead(overlaps)]
    for seq in xrange(overlaps.shape[1]-1): #pd.shape returns dimensions of matrix
        seq_order.append(findLargestOverlap(seq_order[seq], overlaps))
    return seq_order

def findLargestOverlap(key, overlaps):
    # idxmax returns key (i.e. column name) of highest value (i.e. length of overlap)
    return overlaps[key].idxmax()

def findStartRead(overlaps):
    # the read with the lowest amount of overlap to the left will be the first read
    # add values and see which read had the lowest overlapping
    # idxmin returns key
    return overlaps.sum(axis=1, skipna=True).idxmin()

# Create dictionary of dictionaries of all overlap comparisons
def getAllOverlaps(reads):
    overlap_counts = {}
    for first_key, first_value in reads.iteritems():
        inner_dict = {}
        for second_key, second_value in reads.iteritems():
            if first_key == second_key:
                inner_dict[second_key] = 'NA'
            else:
                inner_dict[second_key] = getOverlap(first_value, second_value)
        overlap_counts[first_key] = inner_dict
    # to make the nested dictionaries more accessible (and pretty!) convert to pandas dataframe
    # minor issue - probably should make sure type is integer instead of float
    return pd.DataFrame(overlap_counts).convert_objects(convert_numeric=True)

''' since assuming no errors and no nested pairings, then only
    overlaps over a prefix and suffix of two strings '''
def getOverlap(first, second):
    # take prefix of second and compare to suffix of first
    nt = 3 # how many nucleotides must match at least, arbitrary for these purposes
    index = ''
    first = str(first.seq)
    second = str(second.seq)
    finish = False
    while finish == False:
        # keep extending length until no overlap
        if second[:nt] == first[-nt:]:
            index = second[:nt]
            nt += 1
        # check if the prefix is even in the other sequence/read
        elif second[:nt] in first[1:]:
            nt += 1
        else:
            finish = True
    return len(index)

if __name__ == '__main__':
    f = open("data/rosalind_long.txt", 'r')
    # possibly use SeqIO.index(f, "fasta")
    record_dict = SeqIO.to_dict(SeqIO.parse(f, "fasta"))
    f.close()
    
    outhandle = open("output/026_LONG.txt", 'w')
    outhandle.write(assemble(record_dict))
    outhandle.close()
