if(FALSE){
  "
  My solution to Rosalind Bioinformatics Problem 003
  
  Title: Complementing a Strand of DNA
  Rosalind ID: 
  Rosalind #: 003
  URL: http://rosalind.info/problems/revc

  Goal to provide the reverse complement of a DNA string.
  "
}

require(Biostrings)
file_name = "data/rosalind_revc.txt"
raw_data = readChar(file_name, file.info(file_name)$size)

# remove return/newline characters
raw_seq = gsub("\r\n","",raw_data)
dna = DNAString(raw_seq)

# Reverse Complement
revc = as.character(reverseComplement(dna))

outhandle = "utput/003_REVC.txt"
# nchar - size of character string
writeChar(revc, outhandle, nchar(revc))