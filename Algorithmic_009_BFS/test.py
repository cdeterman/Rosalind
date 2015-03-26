import os

with open(os.path.join(os.path.split(os.getcwd())[0], "data", "rosalind_bfs.txt"), 'r') as input_data:
        n = map(int, input_data.readline().strip().split())[0]
        edges = [map(int, line.strip().split()) for line in input_data]

print edges
