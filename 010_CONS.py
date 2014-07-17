'''
My solution to Rosalind Bioinformatics Problem 010

Title: Consensus and Profile
Rosalind ID: CONS
Rosalind #: 010
URL: http://rosalind.info/problems/cons
'''

# Basic Motif Comparisons
from Bio import motifs
from Bio.Seq import Seq
import Bio.Alphabet

f = open("data/rosalind_cons.txt", 'r')
raw_data = f.readlines()
f.close()

motif_dict = {}
cur_key = ''

# need to parse the dataset (similar to FASTA format with the '>')
for i in raw_data:
    if i[0] == '>':
        cur_key = i[1:].rstrip() # removes > and newline character
        motif_dict[cur_key] = '' # value is currently blank for current key
    else:
        # fill in values
        # again remove newline and appends elements
        motif_dict[cur_key] += i.rstrip()

# create motifs instances
instances = []
for seq in motif_dict.values():
    instances.append(Seq(seq))
m = motifs.create(instances)

''' m.counts create profile matrix but also
    has a header which is not part of the answer.
    Must create table manually by iterating over
    the dictionary.'''
profile = m.counts
consensus = m.consensus

o = open("output/010_CONS.txt", 'w')
print >> o, consensus
for key, value in profile.iteritems():
    # must convert integers to str for concatenating
    print >> o, "".join(key + ": " + " ".join(map(str, value)))
o.close()
