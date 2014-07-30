'''
My solution to Rosalind Bioinformatics Problem 029

Title: Enumerating Oriented Gene Orders
Rosalind ID: SIGN
Rosalind #: 029
URL: http://rosalind.info/problems/sign

Goal to return number of and all signed permutations of length 'n'.
This means, for example, that [1, -1] is not acceptable.
'''

from itertools import product

def signedPermutations(iterable, r):
    pool = tuple(iterable)
    n = len(pool)
    for indicies in product(range(n), repeat=r):
        check = tuple(abs(pool[i]) for i in indicies)
        # set checks for duplicates of absolute values
        if len(set(check)) == r:
            yield tuple(pool[i] for i in indicies)

if __name__ == "__main__":
    f = open("data/rosalind_sign.txt", 'r')
    n = int(f.read())
    f.close()

    sign_perms = range(1, n+1) + range(-n, 0)
    perms = list(signedPermutations(sign_perms, r=n))
    
    o = open("output/029_SIGN.txt", 'w')
    print >> o, len(perms)
    for seq in perms:
        print >> o, ' '.join(map(str, seq))
    o.close()
