import numpy as np


def limb_length(matrix, n, j):
    min_value = 1000000
    for i in range(n):
        for k in range(n):
            value = matrix[i][j] + matrix[k][j] - matrix[i][k]
            if i != j and j != k and value <= min_value:
                min_value = value
    return min_value // 2


if __name__ == '__main__':
    with open('../HW05/in.txt') as file:
        n = int(file.readline())
        j = int(file.readline())
        lines = file.readlines()
        distance_matrix = []
        for line in lines:
            distance_matrix.append([int(x) for x in line.split()])
        distance_matrix = np.array(distance_matrix)

    limb_len = limb_length(distance_matrix, n, j)
    print(limb_len)
