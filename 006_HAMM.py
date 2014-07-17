'''
My solution to Rosalind Bioinformatics Problem 006

Title: Counting Point Mutations
Rosalind ID: HAMM
Rosalind #: 006
URL: http://rosalind.info/problems/hamm
'''

f = open("C:/Users/Chaz/python_code/Rosalind/data/rosalind_hamm.txt", 'r')
raw_data = f.readlines()
f.close()

mutations = 0 # initialize mutations

# iterate through the sequences
for i in range(len(raw_data[0])):
    if raw_data[0][i] != raw_data[1][i]:
        mutations += 1

print mutations
