# Global Alignment with Scoring Matrix and Affine Gap Penalty

import numpy as np
import blosum as bl

blosum62 = bl.BLOSUM(62)
a, b = 11, 1

string = """>Rosalind_3779
IQVYPITMHQWPTWWCVRGTFQEVKEVYGGFANSYHHFLGMGEREDKNPEDDYMWYVKAF
EPVWNKFIYQQSLM
>Rosalind_6736
IQVVRCLSPITMHQWPTWWCVRGNLKPFHNSYHHFLLKLTCYSMGEREDGNPEDDFEDFP
PIKTQSTM
"""
lines = string.splitlines()

names_index = []
for i, name in enumerate(lines):
    if name[0] == '>':
        names_index.append(i)

dna_strings = []
for i in range(len(names_index) - 1):
    dna_strings.append(''.join(lines[names_index[i] + 1:names_index[i + 1]]))
dna_strings.append(''.join(lines[names_index[-1] + 1:len(lines)]))

m = len(dna_strings[1])
n = len(dna_strings[0])
middle = np.zeros((m + 1, n + 1))
upper = np.zeros((m + 1, n + 1))
upper[:, 0] = -1000
lower = np.zeros((m + 1, n + 1))
lower[0, :] = -1000
arrows = np.zeros((m, n, 3))

middle[1, 0] = -a
for i in range(2, m + 1):
    middle[i, 0] = middle[i - 1, 0] - b
middle[0, 1] = -a
for j in range(2, n + 1):
    middle[0, j] = middle[0, j - 1] - b

for i in range(1, m + 1):
    for j in range(1, n + 1):
        up = upper[i, j - 1] - b
        mid = middle[i, j - 1] - a
        upper[i, j] = np.max([up, mid])
        arrows[i - 1, j - 1, 0] = np.argmax([up, mid]) + 1

        low = lower[i - 1, j] - b
        mid = middle[i - 1, j] - a
        lower[i, j] = np.max([low, mid])
        arrows[i - 1, j - 1, 1] = np.argmax([low, mid]) + 1

        up = upper[i, j]
        low = lower[i, j]
        mid = middle[i - 1, j - 1] + blosum62[dna_strings[0][j - 1] + dna_strings[1][i - 1]]
        middle[i, j] = np.max([low, mid, up])
        arrows[i - 1, j - 1, 2] = np.argmax([low, mid, up]) + 1


i, j, k = m - 1, n - 1, 2
s1, s2 = "", ""
cost = 0

while i >= 0 and j >= 0:
    if k == 2 and arrows[i, j, k] == 1:
        k = 1
    elif k == 2 and arrows[i, j, k] == 2:
        cost = cost + blosum62[dna_strings[0][j] + dna_strings[1][i]]
        s2 = s2 + dna_strings[0][j]
        s1 = s1 + dna_strings[1][i]
        i = i - 1
        j = j - 1
    elif k == 2 and arrows[i, j, k] == 3:
        k = 0
    elif k == 1 and arrows[i, j, k] == 1:
        cost = cost - b
        s1 = s1 + dna_strings[1][i]
        s2 = s2 + "-"
        i = i - 1
    elif k == 1 and arrows[i, j, k] == 2:
        cost = cost - a
        s1 = s1 + dna_strings[1][i]
        s2 = s2 + "-"
        i = i - 1
        k = 2
    elif k == 0 and arrows[i, j, k] == 1:
        cost = cost - b
        s2 = s2 + dna_strings[0][j]
        s1 = s1 + "-"
        j = j - 1
    elif k == 0 and arrows[i, j, k] == 2:
        cost = cost - a
        s2 = s2 + dna_strings[0][j]
        s1 = s1 + "-"
        j = j - 1
        k = 2

print(int(cost))
print(s2[::-1])
print(s1[::-1])
