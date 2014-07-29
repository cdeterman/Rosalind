if (FALSE){
"My solution to Rosalind Bioinformatics Problem 007

Title: Mendel's First Law
Rosalind ID: IPRB
Rosalind #: 007
URL: http://rosalind.info/problems/iprb

Not much different than Python solution.  Only major thing
is the lack of a nice assignment operator (e.g. +=, -=)
"
}

# k homozygous dominant
# m heterozygous recessive
# n homozygous recessive

prob_dom <- function(k,m,n){
  t = k+m+n
  pk = k/t
  pm = m/t
  pn = n/t

  # Max probability
  prob = 1
  
  # subtract probability if both homozygous
  prob <- prob - (pn*((n-1)/(t-1)))
  
  # subtract prob if one homozygous recessive & one heterozygous recessive
  # double because two scenarios (e.g. Aa * aa & aa * Aa)
  prob <- prob - (2*pn*(m/(t-1))*0.5)
  
  # subtract prob if both heterozygous recessive
  prob <- prob - (pm*((m-1)/(t-1))*0.25)
  
  return(prob)
}
