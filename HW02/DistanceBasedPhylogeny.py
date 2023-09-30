# Creating a Distance Matrix

import numpy as np

string = """>Rosalind_9499
TTTCCATTTA
>Rosalind_0942
GATTCATTTC
>Rosalind_6568
TTTCCATTTT
>Rosalind_1833
GTTCCATTTA"""
lines = string.splitlines()

names_index = []
for i, name in enumerate(lines):
    if name[0] == '>':
        names_index.append(i)

dna_strings = []
for i in range(len(names_index)-1):
    dna_strings.append(''.join(lines[names_index[i]+1:names_index[i+1]]))
dna_strings.append(''.join(lines[names_index[-1] + 1:len(lines)]))

n = len(dna_strings)
matrix = np.zeros((n, n))
l = len(dna_strings[0])

for i in range(n):
    for j in range(i+1, n):
        dist = sum(s1 != s2 for s1, s2 in zip(dna_strings[i], dna_strings[j])) / l
        matrix[i, j] = dist
        matrix[j, i] = dist

[print(*row) for row in matrix]



