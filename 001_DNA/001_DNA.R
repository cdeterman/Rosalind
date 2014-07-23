if(FALSE){
  '''
  My solution to Rosalind Bioinformatics Problem 001
  
  Title: Counting DNA Nucleotides
  Rosalind ID: DNA
  Rosalind #: 001
  URL: http://rosalind.info/problems/dna

  Goal to count the number of each nucleotide in a string.
  
  Note - To my knowledge, R does not possess a means
  for multiline comments.  As such, to avoid the hassle
  of excessive # and computation of the useless string
  the use of if(FALSE){} provides a workaround.  Not
  pretty but it works.
  '''
}

require(stringr)

file_name = "data/rosalind_dna.txt"
seq = readChar(file_name, file.info(file_name)$size)
str_count(seq, c("A","C","G","T"))