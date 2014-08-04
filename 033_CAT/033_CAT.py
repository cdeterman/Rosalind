'''
My solution to Rosalind Bioinformatics Problem 033

Title: Catalan Numbers and RNA Secondary Structures
Rosalind ID: CAT
Rosalind #: 033
URL: http://rosalind.info/problems/cat

Goal - Return the number of possible noncrossing, perfect matches of a base pairs when
given an rna string. 

I was sincerely irritated by this question as I have yet to come across a solution that
actually uses the Catalan number sequence in any form for this problem.  The scientific
literature is also quite terse in regard to the application of such a sequence and tend
to only mention it in passing.  As such, if you manage to develop such a solution please
do share it with me.  I will continue to explore this in the future as well and post any
additional solutions.

As a result the following solution is this recursive solution.  This appears to be the way
most haved solved the problem.  For those unfamiliar with recursive functions, I have
tried to copiously comment this one.
'''


def countRNA2Structures(seq):    
    # if sequence not in dictionary
    if seq not in cache:
        # iterate over range by 2's as we don't want odd lengths
        tmp = []
        for k in range(1, len(seq), 2):
            ''' Multiply first half of the string * the first nt and ending nt of first half
            * second half
            This multiplication is to combine the number of noncrossing
            perfect matches from the subproblems.

            The actual value/counts comes from the dynamically generated dictionary.
            '''
            tmp.append(countRNA2Structures(seq[1:k]) * cache[seq[0]+seq[k]] * countRNA2Structures(seq[k+1:]))
        # assign current sequence into dictionary for later use
        cache[seq] = sum(tmp)
    return cache[seq]


if __name__ == "__main__":
    from Bio import SeqIO
    f = open("/Rosalind/data/rosalind_cat.txt", 'r')
    raw = SeqIO.read(f, "fasta")
    f.close()

    rna = str(raw.seq)

    # set up initial dictionary for number of matches for the sequence
    cache = {'':1, 'A':0, 'C':0, 'G':0, 'U':0, 'AA':0, 'AC':0, 'AG':0, 'AU':1, 'CA':0, 'CC':0,
             'CG':1, 'CU':0, 'GA':0, 'GC':1, 'GG':0, 'GU':0, 'UA':1, 'UC':0, 'UG':0, 'UU':0}

    print countRNA2Structures(rna) % 10**6
