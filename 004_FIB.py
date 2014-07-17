'''
My solution to Rosalind Bioinformatics Problem 004

Title: Rabbit and Recurrence Relations
Rosalind ID: FIB
Rosalind #: 004
URL: http://rosalind.info/problems/fib
'''

# take one month to reach reproductive maturity
# n - # of months
# k - # of pairs in litter

# for loop function for only the total
def fib(n,k):
    # total number of rabbit pairs
    a,b = 1,1
    for i in range(n-1):
        a,b = b, b+(a*k)
    return a

# using a list function to return all values
def fib_list(n,k):
    fib_table = []
    for i in range(n):
        if i < 2:
            fib_table.append(1)
        else:
            fib_table.append(fib_table[-1] + fib_table[-2]*k)
    return fib_table
