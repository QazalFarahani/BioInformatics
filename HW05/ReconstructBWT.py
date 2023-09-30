def decompression(last_col):
    n = len(last_col)
    columns = [sorted(last_col)]
    matrix = columns[0]

    for i in range(1, len(last_col)):
        matrix = sorted([last_col[i] + matrix[i] for i in range(n)])

    return matrix[0]


if __name__ == "__main__":
    with open("in.txt", "r") as file:
        data = file.readline().strip()
    s = decompression(data)
    print(s[1:] + s[0])
