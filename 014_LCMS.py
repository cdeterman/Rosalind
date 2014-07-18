'''
My solution to Rosalind Bioinformatics Problem 014

Title: Finding a Shared Motif
Rosalind ID: lcsm
Rosalind #: 014
URL: http://rosalind.info/problems/lcms
'''

'''First and foremost, I believe these days a problem such as this
would employ the use of another program such as MEME and then parse
the output from such a program with BioPython.

However for the sake of learning, my readings tell me the bioinformatics
approach to this problem appears to usually consist of a generalized suffix
tree.  My initial strategy was to apply such a method with the suffix_tree
module below.  The module description and download is at http://www.daimi.au.dk/~mailund/suffix_tree.html for
those who wish to apply this solution themselves.  However, this module
for generalized suffix trees was limited to 35 strings making it unusable for
these purposes.  One further caveat, this module, to my knowledge, only works with the 32-bit implementation
of python.

My next approach was to switch back to a brute-force method.  To avoid major
memory concerns and time constraints, I applied two separate 'break' instances.
So far, this approach seems to work rather well.
'''


from Bio import SeqIO

input_handle = "data/rosalind_lcsm.txt"

raw_data = list(SeqIO.parse(input_handle, 'fasta'))

sequences = []
for seq in raw_data:
    sequences.append(str(seq.seq))

lengths = map(len, sequences)
index = lengths.index(min(lengths))
shortest_sequence = sequences[index]

lcs = ''
for start in xrange(len(shortest_sequence)):
    for end in xrange(len(shortest_sequence), start, -1):
        if len(shortest_sequence[start:end]) > len(lcs):
               matches = []
               for seq in sequences:
                   if shortest_sequence[start:end] in seq:
                       matches.append(True)
                   else:
                       matches.append(False)
                       break
               if all(matches):
                   lcs = shortest_sequence[start:end]
                   break
        else:
               break

o = open("output/014_LCMS.txt", 'w')
o.write(lcs)
o.close()


'''
The suffix tree method that doesn't work so far with so many strings.

from suffix_tree import GeneralisedSuffixTree

# file import methods as above

st = GeneralisedSuffixTree(sequences)
substring_lengths = ''
diff = 0
for shared in st.sharedSubstrings():
    start = shared[0][-2]
    stop = shared[0][-1]
    new_diff = stop-start
    if new_diff > diff:
        diff = new_diff
        substring_lengths = (start, stop)

o = open("C:/Users/Chaz/python_code/Rosalind/output/014_LCMS.txt", 'w')
print >> o, sequences[0][substring_lengths[0]:substring_lengths[1]]
o.close()

'''

