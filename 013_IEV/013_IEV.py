'''
My solution to Rosalind Bioinformatics Problem 013

Title: Calculating Expected Offspring
Rosalind ID: IEV
Rosalind #: 013
URL: http://rosalind.info/problems/iev
'''

# Probability offspring display dominant phenotype
f = open("C:/Users/Chaz/python_code/Rosalind/data/rosalind_iev.txt", 'r')
# remove newline, split by comma, convert to integers
data = map(int, f.readline().rstrip().split())
f.close()

prob_dict = {}

for i in range(6):
    if i <= 2 and data[i] > 0:      # AA-AA, AA-Aa, AA-aa
        prob_dict[i] = data[i]*1
    elif i == 3 and data[i] > 0:    # Aa-Aa
        prob_dict[i] = data[i]*.75
    elif i == 4 and data[i] > 0:    # Aa-aa
        prob_dict[i] = data[i]*.5
    else:                           # aa-aa
        prob_dict[i] = 0

print 2*sum(prob_dict.values())
