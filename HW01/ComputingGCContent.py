# Computing GC Content

import numpy as np

string = """>Rosalind_6404
CCTGCGGAAGATCGGCACTAGAATAGCCAGAACCGTTTCTCTGAGGCTTCCGGCCTTCCC
TCCCACTAATAATTCTGAGG
>Rosalind_5959
CCATCGGTAGCGCATCCTTAGTCCAATTAAGTCCCTATCCAGGCGCTCCGCCGAAGGTCT
ATATCCATTTGTCAGCAGACACGC
>Rosalind_0808
CCACCCTCGTGGTATGGCTAGGCATTCAGGAACCGGAGAACGCTTCAGACCAGCCCGGAC
TGGGAACCTGCGGGCAGTAGGTGGAAT"""
lines = string.splitlines()

names_index = []
for i, name in enumerate(lines):
    if name[0] == '>':
        names_index.append(i)

dna_strings = []
for i in range(len(names_index)-1):
    dna_strings.append(''.join(lines[names_index[i]+1:names_index[i+1]]))
dna_strings.append(''.join(lines[names_index[-1] + 1:len(lines)]))

percentages = [(dna.count('G') + dna.count('C'))/len(dna)*100 for dna in dna_strings]

print(lines[names_index[np.argmax(percentages)]][1:])
print(np.max(percentages))

