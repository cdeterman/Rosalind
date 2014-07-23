'''
My solution to Rosalind Bioinformatics Problem 011

Title: Rabbit and Recurrence Relations
Rosalind ID: FIBD
Rosalind #: 011
URL: http://rosalind.info/problems/fibd
'''

# Mortal rabbits
# n - how many months
# m - lifespan in months
# one month to reach reproductive maturity
# only produce a single pair of offspring (male & female)

def fib_mortal(n,m):
    # track number
    # track age of each
    fib_table = []
    for i in range(n):
        if i < 2:
            fib_table.append(1)
        elif i < m:
            fib_table.append(fib_table[-2] + fib_table[-1])
        elif i == m or i == m+1:
            fib_table.append((fib_table[-2] + fib_table[-1]) - 1)
        else:
            fib_table.append((fib_table[-2] + fib_table[-1]) - fib_table[-(m+1)])
    return fib_table
