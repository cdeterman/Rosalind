'''
My solution to Rosalind Bioinformatics Problem 005

Title: Computing GC Content
Rosalind ID: GC
Rosalind #: 005
URL: http://rosalind.info/problems/gc
'''

from Bio.SeqUtils import GC

f = open("data/rosalind_gc.txt", 'r')
raw_data = f.readlines()
f.close()

samples = {}
cur_key = ''

# need to parse the dataset
for i in raw_data:
    if i[0] == '>':
        cur_key = i[1:].rstrip() # removes > and newline character
        samples[cur_key] = '' # value is currently blank for current key
    else:
        # fill in values
        # again remove newline and appends elements
        samples[cur_key] += i.rstrip()

# need GC content and id
gc_samples = {}

# Note iteritems() -> items() in Python 3.X
for s_id, s in samples.iteritems(): # dict.iteritems - iterate both keys and values
    gc_samples[s_id] = GC(s) # Use GC function from BioPython

gc_id = max(gc_samples, key = gc_samples.get)
gc_value = max(gc_samples.values())

o = open('output/005_GC.txt', 'w')
o.writelines('\n'.join([gc_id, str(gc_value)]))
o.close()

