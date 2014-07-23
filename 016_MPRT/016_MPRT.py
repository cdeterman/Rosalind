'''
My solution to Rosalind Bioinformatics Problem 016

Title: Finding a Protein Motif
Rosalind ID: mprt
Rosalind #: 016
URL: http://rosalind.info/problems/mprt

The problem was to find all the N-glycosylation motifs in the provided proteins.
This provided an excellent opportunity for regex.  The strategy was to
create the regex object and itertively search each protein extracted
from the uniprot fasta file.

FYI - I neglected to realize that the question doesn't specify non-overlapping
motifs.  As such, see note by the regex code.
'''

# allows use of Python3.X print functionality
from __future__ import print_function
import re # for regex functions

# need regex for N-glycosylation motif
# N{any but P}[S or T]{any but P}
# parentheses and '?=' allow for overlapping
motif = re.compile('(?=N[^P][ST][^P])')

# loop through protein id's to import from uniprot website
import urllib2
from Bio import SeqIO

dataset = open("data/rosalind_mprt.txt", 'r')
protein_ids = dataset.readlines()
dataset.close()

outhandle = open("output/016_MPRT.txt", 'w')
uniprot_url = "http://www.uniprot.org/uniprot/"

for protein in protein_ids:
    request = urllib2.Request("".join([uniprot_url+protein.rstrip()+".fasta"]))
    opener = urllib2.build_opener()
    f = opener.open(request)
    raw_data = SeqIO.read(f, 'fasta')
    f.close()

    locations = []
    # Use search instead of match to search entire string
    if re.search(motif, str(raw_data.seq)):
        print(protein.strip(), file=outhandle)
        for m in re.finditer(motif, str(raw_data.seq)):
            locations.append(m.start()+1)
        print(" ".join(map(str, locations)), file=outhandle)
        
outhandle.close()
