'''
My solution to Rosalind Bioinformatics Problem 007

Title: Mendel's First Law
Rosalind ID: IPRB
Rosalind #: 007
URL: http://rosalind.info/problems/iprb
'''

# k homozygous dominant
# m heterozygous recessive
# n homozygous recessive

''' Probability two random organisms mate and produce individual
with a dominant allele'''

def prob_dom(k,m,n):
    k,m,n = map(float, (k,m,n))
    t = k+m+n
    pk = k/t
    pm = m/t
    pn = n/t

    # Max probability
    prob = 1

    # subtract probability if both homozygous recessive
    prob -= pn*((n-1)/(t-1))

    # subtract prob if one homozygous recessive & one heterozygous recessive
    # double because two scenarios (e.g. Aa * aa & aa * Aa)
    prob -= 2*pn*(m/(t-1))*0.5

    # subtract prob if both heterozygous recessive
    prob -= pm*((m-1)/(t-1))*0.25

    return prob

'''Also possible to accomplish by calculating the dominant
allele probabilities instead'''

def prob_dom_alleles(k,m,n):
    k,m,n = map(float, (k,m,n))
    t = k+m+n

    # Simply add up probabilities of possessing dominant allele
    # AA x anything
    prob = k/t
    
    # Aa x AA
    prob += pm*(k/(t-1))
    
    # Aa x Aa
    prob += pm*((m-1)/(t-1))*.75)
    
    # Aa x aa & aa x Aa
    prob += 2*pm*(n/(t-1)*.5))
    
    # aa x AA
    prob += pn*(k/(t-1))
    return prob
