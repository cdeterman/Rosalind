if(FALSE){
  '''
  My solution to Rosalind Bioinformatics Problem 002
  
  Title: Transcribing DNA into RNA
  Rosalind ID: RNA
  Rosalind #: 002
  URL: http://rosalind.info/problems/rna

  Goal to transcribe the DNA sequence to RNA sequence.

  Note - As with my python solutions, I prefer to implement
  methods provided by some Biology specific packages.  In 
  the case of R, Bioconductor.  For this specific instance,
  Biostrings is the package for working with sequences.
  '''
}

require(Biostrings)

file_name = "data/rosalind_rna.txt"
raw_data = readChar(file_name, file.info(file_name)$size)

# remove newline character
# Note - \r\n is a consequence of Windows files
raw_seq = gsub("\r\n","",raw_data)
dna = DNAString(raw_seq)

# transcribe DNA string to RNA
rna = as.character(RNAString(dna))

outhandle = "output/002_RNA.txt"
# nchar - size of character string
writeChar(rna, outhandle, nchar(rna))
