'''
My solution to Rosalind Bioinformatics Problem 028

Title: Introduction to Random Strings
Rosalind ID: PROB
Rosalind #: 028
URL: http://rosalind.info/problems/prob

Goal to return probability that random sequence will exactly match the
provided sequence given the GC content.
'''

from math import log10

f = open("data/rosalind_prob.txt")
my_seq = f.readline().rstrip()
gc_array = map(float, f.readline().rstrip().split())
f.close()

output_handle = open("output/025_PROB.txt", 'w')
for gc in gc_array:
    prob_gc = gc/2
    prob_at = (1-gc)/2
    #print prob_gc

    prob = 1
    for nucleotide in my_seq:
        if nucleotide == 'A' or nucleotide == 'T':
            prob *= prob_at
        else:
            prob *= prob_gc
    print >> output_handle, log10(prob),

output_handle.close()
