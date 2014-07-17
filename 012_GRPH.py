'''
My solution to Rosalind Bioinformatics Problem 012

Title: Overlap Graphs
Rosalind ID: GRPH
Rosalind #: 012
URL: http://rosalind.info/problems/grph
'''

# collections of strings (sequences)
# k - length of match
# return adjacency list corresponding to k, edges returned in any order

from Bio import SeqIO

def adjacency_list(k, input_handle, output_handle):

    seqs = list(SeqIO.parse(input_handle, "fasta"))
    
    output = open(output_handle, 'w')
    for value in range(len(seqs)-1): # iterate through all combinations
        for inner_value in range(len(seqs)):
            # check to make sure sequences aren't the same
            if seqs[value].seq.tostring() != seqs[inner_value].seq.tostring():
                # check if sequences contain overlap
                if seqs[value].seq.tostring()[:k] == seqs[inner_value].seq.tostring()[-k:]:
                    # save just the sequence id's
                    print >> output, " ".join([seqs[inner_value].id, seqs[value].id])
            else:
                continue
    output.close()

k = 3
input_handle = "data/rosalind_grph.txt"
output_handle = "output/012_GRPH.txt"

adjacency_list(k, input_handle, output_handle)

