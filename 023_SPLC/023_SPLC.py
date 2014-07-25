from Bio import SeqIO
from Bio.Seq import Seq

f = open("C:/Users/Chaz/Rosalind/data/rosalind_splc.txt", 'r')

# simple parsing to have sequences as strings for subsequent splicing
dna = ''
introns = []
count = 1
for record in SeqIO.parse(f, "fasta"):
    if count == 1: # first record is the DNA string
        dna = str(record.seq)
    else: # collect the introns
        introns.append(str(record.seq))
    count += 1
f.close()

for intron in introns:
    if intron in dna: # if intron present, remove from dna string
        dna = dna.replace(intron, "")

o = open("C:/Users/Chaz/Rosalind/output/023_SPLC.txt", 'w')
# convert to Seq object and translate to protein
print >> o, Seq(dna).translate(to_stop=True)
o.close()


