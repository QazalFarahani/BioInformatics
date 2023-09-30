import numpy as np


def get_score(s1, s2):
    m, n = len(s1), len(s2)
    d = np.zeros((m + 1, n + 1))
    arrows = np.zeros((m + 1, n + 1))

    for i in range(1, m + 1):
        d[i, 0] = -i
    for j in range(1, n + 1):
        d[0, j] = -j

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            prev = d[i - 1][j - 1] - (s1[i - 1] != s2[j - 1])
            up = d[i - 1][j] - 1
            left = d[i][j - 1] - 1
            d[i][j] = np.max([prev, up, left])
            arrows[i][j] = np.argmax([prev, up, left])

    return d[m, n], arrows


def align(s1, s2, arrows):
    i_index, j_index = len(s1) - 1, len(s2) - 1

    while i_index > 0 and j_index > 0:
        if arrows[i_index][j_index] == 0:
            i_index = i_index - 1
            j_index = j_index - 1
        elif arrows[i_index][j_index] == 1:
            s2 = s2[:j_index] + '-' + s2[j_index:]
            i_index = i_index - 1
        elif arrows[i_index][j_index] == 2:
            s1 = s1[:i_index] + '-' + s1[i_index:]
            j_index = j_index - 1

    for dash in range(i_index):
        s2 = s2[:0] + '-' + s2[0:]
    for dash in range(j_index):
        s1 = s1[:0] + '-' + s1[0:]
    return s1, s2


string = """>Rosalind_2962
GCGGCGTAC
>Rosalind_3274
AACCCTTCT
>Rosalind_9073
ATAGCAAGGA
>Rosalind_8296
CTGGATTT"""
lines = string.splitlines()

names_index = []
for i, name in enumerate(lines):
    if name[0] == '>':
        names_index.append(i)

seqs = []
for i in range(len(names_index) - 1):
    seqs.append(''.join(lines[names_index[i] + 1:names_index[i + 1]]))
seqs.append(''.join(lines[names_index[-1] + 1:len(lines)]))

number_of_seqs = len(seqs)

scores = np.ones((number_of_seqs, number_of_seqs)) * -1000
matrices = np.zeros((number_of_seqs, number_of_seqs), dtype=list)
for i in range(number_of_seqs):
    for j in range(i + 1, number_of_seqs):
        aligned_strings = get_score(seqs[i], seqs[j])
        scores[i, j], matrices[i, j] = aligned_strings[0], aligned_strings[1]

remaining = [i for i in range(len(seqs))]
aligned_strings = [''] * len(seqs)
a, b = np.unravel_index(scores.argmax(), scores.shape)
max_score, matrix = scores[a, b], matrices[a, b]
aligned_strings[a], aligned_strings[b] = align(seqs[a], seqs[b], matrix)
remaining.remove(a)
remaining.remove(b)
print(aligned_strings)

while len(remaining) > 0:
    scores = {}
    i = remaining[0]

    for j in range(len(aligned_strings)):
        if aligned_strings[j] != '':
            scores[j] = get_score(seqs[i], aligned_strings[j])
    best = max(scores)
    best_score, matrix = scores[best]
    aligned_strings[i], aligned_strings[j] = align(seqs[i], aligned_strings[best], matrix)
    print(aligned_strings)
    remaining.remove(i)

max_score = 0
for i in range(len(aligned_strings)):
    for j in range(i + 1, len(aligned_strings)):
        max_score += get_score(aligned_strings[i], aligned_strings[j])[0]

for dash in range(10):
    aligned_strings[0] = aligned_strings[0][:0] + '-' + aligned_strings[0][0:]

print(int(max_score))
print('\n'.join(aligned_strings))
