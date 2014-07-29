if(FALSE){
  "
  My solution to Rosalind Bioinformatics Problem 006
  
  Title: Counting Point Mutations
  Rosalind ID: HAMM
  Rosalind #: 006
  URL: http://rosalind.info/problems/hamm

  Goal to calculate hamming distance between two provided sequences.
  "
}


file_name = file("C:/Users/Chaz/Rosalind/data/rosalind_hamm.txt", "r")
raw_data = readLines(file_name)
close(file_name)

# could cheat with built-in function
library(stringdist)
stringdist(raw_data[1], raw_data[2], method="hamming")

# hand solution is far less pretty because R doesn't natively index strings
seq1 = unlist(strsplit(raw_data[1], split = ""))
seq2 = unlist(strsplit(raw_data[2], split = ""))

mutations = 0
for (i in seq(nchar(raw_data[1]))){
  if(seq1[i] != seq2[i]){
    mutations = mutations + 1
  }
}
mutations

