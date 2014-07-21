'''
My solution to Rosalind Algorithmic Heights Problem 001

Title: Fibonacci Numbers
Rosalind ID: FIBO
Rosalind #: 001
URL: http://rosalind.info/problems/fibo

The problem was to return the n-th value of the fibonacci sequence.
'''

# for loop function for only the total
def fib(n):
    a,b = 1,1
    for i in range(n-1):
        a,b = b, b+a
    return a

if __name__ == "__main__":
    print fib(22)
