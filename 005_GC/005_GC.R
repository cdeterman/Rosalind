if(FALSE){
  "
  My solution to Rosalind Bioinformatics Problem 005
  
  Title: Computing GC Content
  Rosalind ID: GC
  Rosalind #: 005
  URL: http://rosalind.info/problems/gc

  Goal to return ID and GC percent of sequence with the
  highest GC content
  "
}

require(Biostrings)

file_name <- "data/rosalind_gc.txt"
# read FASTA format
dna <- readDNAStringSet(file_name, format="fasta")
# calculate GC frequency
gc_contents <- letterFrequency(dna, c("GC"), as.prob=TRUE)
# which has the highest
index = which(gc_contents == max(gc_contents))
# collect the name of the highest
name = dna@ranges@NAMES[index]

outhandle = "output/005_GC.txt"
# don't forget to multiply 100 for percentage
writeLines(c(name, gc_contents[5,]*100), con = outhandle)
