import numpy as np


def read_data(file_name):
    with open(file_name, 'r') as file:
        n = int(file.readline().strip())
        adj_matrix = {}
        weights = {}
        lines = file.readlines()
        for line in lines:
            line = line.strip()
            temp = line.split("->")
            i = int(temp[0])
            temp = temp[1].split(":")
            j = int(temp[0])
            w = int(temp[1])

            if i not in adj_matrix.keys():
                adj_matrix[i] = []
            adj_matrix[i].append(j)
            weights[(i, j)] = w

    return n, adj_matrix, weights


def bfs(d_mat, adj_mat, w_mat, node):
    visited = []
    queue = []
    visited.append(node)
    queue.append(node)

    while queue:
        current_node = queue.pop(0)
        for neighbour in adj_mat[current_node]:
            if neighbour not in visited:
                if d_mat[node][neighbour] == 0 and node != neighbour:
                    weight = w_mat[(current_node, neighbour)]
                    d_mat[node][neighbour] = d_mat[node][current_node] + weight
                visited.append(neighbour)
                queue.append(neighbour)

    return d_mat


def get_distance_matrix(s, n, adj_mat, w_mat):
    d_matrix = np.zeros((s, s))
    for i in range(n):
        d_matrix = bfs(d_matrix, adj_mat, w_mat, i)
    return d_matrix


if __name__ == "__main__":
    n, adjacency_matrix, weights_matrix = read_data("../HW05/in.txt")
    size = len(adjacency_matrix)
    distance_matrix = get_distance_matrix(size, n, adjacency_matrix, weights_matrix)
    for i in range(n):
        print(' '.join([str(int(i)) for i in distance_matrix[i][0:n]]))
