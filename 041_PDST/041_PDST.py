'''
My solution to Rosalind Bioinformatics Problem 041

Title: Creating a Distance Matrix
Rosalind ID: PDST
Rosalind #: 041
URL: http://rosalind.info/problems/pdst

Goal to return a matrix of the proprotion of symbols different
between each provided sequence.
'''


# Function to calculate distance proportion
def pDistance(s1, s2):
    total = float(len(s1))
    count = 0
    for i in xrange(len(s1)):
        if s1[i] == s2[i]:
            count += 1
    return 1.0 - float(count/total)

if __name__ == "__main__":
    from Bio import SeqIO
    import numpy as np

    f = open("/Rosalind/data/rosalind_pdst.txt", 'r')
    taxa = []
    for taxon in SeqIO.parse(f, "fasta"):
        taxa.append(str(taxon.seq))
    f.close()

    # Create empty array
    distMat = np.zeros((len(taxa), len(taxa)), dtype=np.float)

    # Fill array with all comparisons
    for i in xrange(len(taxa)):
        for j in xrange(len(taxa)):
            distMat[i, j] = float(pDistance(taxa[i], taxa[j]))

    output_handle = '/Rosalind/output/041_PDST.txt'
    # Note fmt to specify 5 decimal places in output
    np.savetxt(output_handle, distMat, delimiter=" ", fmt='%.5f')
