'''
My solution to Rosalind Bioinformatics Problem 015

Title: Independent Alleles
Rosalind ID: lia
Rosalind #: 015
URL: http://rosalind.info/problems/lia

Assuming independent allele's according to Mendel's Second Law,
What is the probability there will be at least 'N' AaBb organisms
after 'k' generations (just final, not including parents)?

k - how many generations to pass
N - how many AaBb organisms in final generation
'''

import math

def prob_het(k,N):
    ''' AaBb probability - true for all iterative combinations.
    Draw punnit squares to verify if you don't believe me.
    '''
    prob_AaBb = 4/16.0

    prob = []
    total = 2**k
    # summation of your general binomial probability function
    for r in xrange(N,(total+1)):
        prob.append(nCr(total,r)*(prob_AaBb**r)*((1-prob_AaBb)**(total-r)))
    return sum(prob)

# quick combinatorial function
def nCr(n,r):
    f = math.factorial
    return f(n) / f(r) / f(n-r)

if __name__ == '__main__':
    print prob_het(6,18)


