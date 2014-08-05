'''
My solution to Rosalind Bioinformatics Problem 037

Title: Speeding up Motif Finding
Rosalind ID: KMP
Rosalind #: 037
URL: http://rosalind.info/problems/kmp

Goal to return the Knuth-Morris-Pratt Failure Array for a given rna string.
'''


def KMP_failure_table(seq):
    failure_array = [0]*len(seq)
    k = 0
    for i in range(2, len(seq)):
        # check if substring can be expanded
        # print i, k, seq[k], seq[i-1]
        # if subsequence (k > 0) but sequence doesn't continue
        while k > 0 and seq[k] != seq[i-1]:
            # reset k index to 1 before ending character to avoid repetition
            k = failure_array[k-1]
        # if subsequence starting or continuing
        if seq[k] == seq[i-1]:
            k += 1
            # -1 for 0-indexing
        failure_array[i-1] = k
    return failure_array

if __name__ == "__main__":
    from Bio import SeqIO

    f = open("/Rosalind/data/rosalind_kmp.txt", 'r')
    raw = SeqIO.read(f, "fasta")
    f.close()
    seq = str(raw.seq)

    o = open("/Rosalind/output/037_KMP.txt", 'w')
    print >> o, " ".join(map(str, KMP_failure_table(seq)))
    o.close()
