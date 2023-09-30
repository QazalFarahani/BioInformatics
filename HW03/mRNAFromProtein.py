map = {'A': 4, 'R': 6, 'D': 2, 'N': 2, 'C': 2, 'E': 2, 'Q': 2, 'G': 4, 'H': 2, 'I': 3, 'L': 6,
       'K': 2, 'M': 1, 'F': 2, 'P': 4, 'S': 6, 'T': 4, 'W': 1, 'Y': 2, 'V': 4}

string = input()
count = 3
for char in string:
    count *= map[char]
    count = count % 1000000

print(count)