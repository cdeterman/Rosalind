if(FALSE){
"My solution to Rosalind Bioinformatics Problem 011

Title: Rabbit and Recurrence Relations
Rosalind ID: FIBD
Rosalind #: 011
URL: http://rosalind.info/problems/fibd
"
}

# Mortal rabbits
# n - how many months
# m - lifespan in months
# one month to reach reproductive maturity
# only produce a single pair of offspring (male & female)

# function returns vector containing the number of pairs
# of rabbits for each consecutive month
fib_mortal <- function(n,m){
    # track number
    # track age of each
    fib_table = c()
    for(i in seq(n)){
        if(i < 3){
            fib_table <- append(fib_table, 1)
        }else if(i < m+1){
            count <- tail(fib_table, 2)[1] + tail(fib_table, 1)
            fib_table <- append(fib_table, count)
        }else if(i == m+1 | i == m+2){
            count <- (tail(fib_table, 2)[1] + tail(fib_table, 1)) - 1
            fib_table <- append(fib_table, count)
        }else{
            count <- tail(fib_table, 2)[1] + 
                tail(fib_table, 1) - 
                tail(fib_table, m+1)[1]
            fib_table <- append(fib_table, count)
        }
    }
    return(fib_table)
}