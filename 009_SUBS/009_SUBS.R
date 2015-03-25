if(FALSE){
"My solution to Rosalind Bioinformatics Problem 009
Title: Finding a Motif in DNA
Rosalind ID: SUBS
Rosalind #: 009
URL: http://rosalind.info/problems/subs
"
}

library(Biostrings)

file_name <- "C:/Users/cdeterman/Documents/Rosalind/data/rosalind_subs.txt"
f <- readLines(file_name)

dna <- f[1]
motif <- f[2]
idx <- start(matchPattern(motif, dna))

outhandle = "output/009_PROT.txt"
# nchar - size of character string
writeChar(as.character(idx), outhandle, nchar(idx))