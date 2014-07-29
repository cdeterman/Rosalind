if(FALSE){
"My solution to Rosalind Bioinformatics Problem 008

Title: Translating RNA into Protein
Rosalind ID: PROT
Rosalind #: 008
URL: http://rosalind.info/problems/prot
"
}

require(Biostrings)

file_name = "data/rosalind_prot.txt"
raw_data = readChar(file_name, file.info(file_name)$size)

# remove return/newline characters
raw_seq = gsub("\r\n","",raw_data)
rna = RNAString(raw_seq)

# translate RNA sequence
protein = as.character(translate(rna))

# Annoying means to remove stop codons
trimLRPatterns(Rpatter='*', subject=protein)

outhandle = "output/008_PROT.txt"
# nchar - size of character string
writeChar(rna, outhandle, nchar(rna))