from collections import Counter
from Bio.Seq import Seq


def hamming_distance(s1, s2):
    count = 0
    for i in range(len(s1)):
        count += not(s1[i] == s2[i])
    return count



string = """>Rosalind_52
TCATC
>Rosalind_44
TTCAT
>Rosalind_68
TCATC
>Rosalind_28
TGAAA
>Rosalind_95
GAGGA
>Rosalind_66
TTTCA
>Rosalind_33
ATCAA
>Rosalind_21
TTGAT
>Rosalind_18
TTTCC"""

lines = string.splitlines()

names_index = []
for i, name in enumerate(lines):
    if name[0] == '>':
        names_index.append(i)

seqs = []
main_seqs = []
for i in range(len(names_index) - 1):
    seq = Seq(''.join(lines[names_index[i] + 1:names_index[i + 1]]))
    main_seqs.append(str(seq))
    seqs.append(str(seq))
    seqs.append(str(seq.reverse_complement()))

seq = Seq(''.join(lines[names_index[-1] + 1:len(lines)]))
main_seqs.append(str(seq))
seqs.append(str(seq))
seqs.append(str(seq.reverse_complement()))

counts = Counter(seqs)

correct = []
incorrect = []
for s in counts:
    if counts[s] > 1:
        correct.append(s)
    elif s in main_seqs:
        incorrect.append(s)

corrected_strings = []
for s1 in incorrect:
    for s2 in correct:
        if hamming_distance(s1, s2) == 1:
            corrected_strings.append([s1, s2])

for s in corrected_strings:
    print("->".join(s))
