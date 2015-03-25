if(FALSE){
"My solution to Rosalind Bioinformatics Problem 010
Title: Consensus and Profile
Rosalind ID: CONS
Rosalind #: 010
URL: http://rosalind.info/problems/cons
"
}

library(Biostrings)

file_name <- file.path(dirname(getwd()), "data", "010_CONS.txt")
f <- readDNAStringSet(file_name)

# index first four rows because default returns full
# IUPAC DNA alphabet
cm <- consensusMatrix(f)[1:4,]
cs <- consensusString(cm)

outhandle = "010_CONS.txt"

# write consensus string
write(cs, outhandle)

# append each line of consensus matrix
# formatted to contain the colon
for(i in 1:nrow(cm)){
    nextLine <- paste(row.names(cm)[i], 
                      paste(cm[i,],collapse=" "), 
                      sep=": ")
    write(nextLine, 
          file=outhandle, 
          append=TRUE)
}
