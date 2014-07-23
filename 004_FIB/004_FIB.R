if(FALSE){
  "
  My solution to Rosalind Bioinformatics Problem 004
  
  Title: Rabbit and Recurrence Relations
  Rosalind ID: FIB
  Rosalind #: 004
  URL: http://rosalind.info/problems/fib

  Concept - Rabbits reproducing k offspring each month while
  you assume immortality.  Return how many rabbits after 'n'
  months.
  "
}

if(FALSE){
  "R doesn't work with objects the same way as python.
  Values are updated immediately.  As such, one cannot 
  iteratively update values if dependently upon the one
  immediately prior.  To work around this, adding a third
  digit to a vector allows for iterative reassignment and
  allow access to the 'prior' value for the fibonacci
  sequence.

  As with the python example, I have also provided the list
  version (although technically a vector here) to provide all
  the values of the sequence.
  "
}

fib = function(n,k){
  a <- c(1,1)  
  for(i in seq(n-2)){  
    if(i == 1){
      a = append(a, a[2]+(a[1]*k))
    }else{
      a[1] = a[2]
      a[2] = a[3]
      a[3] = a[3]+(a[1]*k)
    }
  }
  return(a)
}

fib_list = function(n,k){
  fib_table <- c(1)
  for(i in seq(n-1)){
    if(i < 2){
      fib_table = append(fib_table, 1)
    }else{
      fib_table = append(fib_table, (fib_table[length(fib_table)]+(fib_table[length(fib_table)-1]*k)))
    }
  }
  return(fib_table)
}
