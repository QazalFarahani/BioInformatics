# Enumerating k-mers Lexicographically

import numpy as np

alphabet_string = "A B C D E F G H"
alphabet = alphabet_string.split(' ')
alphabet_len = len(alphabet)
n = 3

cols = []
for i in range(n):
    cols.append(np.repeat(alphabet, alphabet_len ** (n-1-i)).tolist() * alphabet_len ** i)

[print(''.join(s)) for s in list(zip(*cols))]


