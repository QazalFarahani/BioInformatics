# Edit Distance Alignment

import numpy as np

string = """>Rosalind_43
PRETTY
>Rosalind_97
PRTTEIN"""
lines = string.splitlines()

names_index = []
for i, name in enumerate(lines):
    if name[0] == '>':
        names_index.append(i)

dna_strings = []
for i in range(len(names_index)-1):
    dna_strings.append(''.join(lines[names_index[i]+1:names_index[i+1]]))
dna_strings.append(''.join(lines[names_index[-1] + 1:len(lines)]))

m = len(dna_strings[1])
n = len(dna_strings[0])
hor_ver = np.ones((m+1, n+1))
arrows = np.zeros((m, n))

for i in range(1, m+1):
    for j in range(1, n+1):
        top = hor_ver[i-1, j] + 1
        left = hor_ver[i, j-1] + 1
        prev = hor_ver[i-1, j-1]
        if dna_strings[1][i-1] != dna_strings[0][j-1]:
            prev = prev + 1
        hor_ver[i, j] = np.min([top, left, prev])
        arrows[i-1, j-1] = np.argmin([top, left, prev]) + 1

i, j = m-1, n-1
s1, s2 = "", ""
cost = 0

while i >= 0 and j >= 0:
    if arrows[i, j] == 1:
        s1 = s1 + dna_strings[1][i]
        s2 = s2 + "-"
        i = i - 1
        cost = cost + 1
    if arrows[i, j] == 2:
        s2 = s2 + dna_strings[0][j]
        s1 = s1 + "-"
        j = j - 1
        cost = cost + 1
    if arrows[i, j] == 3:
        s1 = s1 + dna_strings[1][i]
        s2 = s2 + dna_strings[0][j]
        if dna_strings[1][i] != dna_strings[0][j]:
            cost = cost + 1
        i = i - 1
        j = j - 1

print(cost)
print(s2[::-1])
print(s1[::-1])
