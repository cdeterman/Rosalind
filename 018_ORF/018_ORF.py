'''
My solution to Rosalind Bioinformatics Problem 018

Title: Open Reading Frames
Rosalind ID: ORF
Rosalind #: 018
URL: http://rosalind.info/problems/orf

Goal to return all possible proteins from the 6 different reading frames of a
sequence given that they must possess a start and stop codon.
'''

from __future__ import print_function
from Bio import SeqIO
from Bio.Data import CodonTable

f = open("data/rosalind_orf.txt", 'r')
record = SeqIO.read(f, "fasta")

# Get stop codons
standard_table = CodonTable.unambiguous_dna_by_name["Standard"]
stop_codons = standard_table.stop_codons

# function to split string into fragments for searching
def chunker(seq, size):
    return (seq[pos:pos + size] for pos in xrange(0, len(seq), size))

''' Normally I would do a list but a set avoids the need to check
if there are duplicates.'''
proteins = set()
# loop over sequence and reverse complement
for strand in [record.seq, record.seq.reverse_complement()]:
    # loop until only 3 nucleotides remain
    for start in xrange(len(strand)-2):
        start_codon = str(strand[start:start+3])
        # check start codon presence
        if start_codon == "ATG":
            frame = str(strand[start:])
            # check stop codon presence
            if any(st in chunker(frame[3:], 3) for st in stop_codons):
                # translate protein and add to set
                prot = str(strand[start:].translate(to_stop=True))
                proteins.add(prot)

outhandle = open("output/018_ORF.txt", 'w')
print ("\n".join(proteins), file = outhandle)
outhandle.close()
