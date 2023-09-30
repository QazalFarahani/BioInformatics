import numpy as np


def limb_length(matrix, n, j):
    min_value = 1000000
    for i in range(n):
        for k in range(n):
            value = matrix[i][j] + matrix[k][j] - matrix[i][k]
            if i != j and j != k and value <= min_value:
                min_value = value
    return min_value // 2


def delete_edge(graph, s, d):
    for i, (neighbor, _) in enumerate(graph[s]):
        if neighbor == d:
            break
    graph[s].pop(i)
    for i, (neighbor, _) in enumerate(graph[d]):
        if neighbor == s:
            break
    graph[d].pop(i)


def get_path(graph, src, dst, visited):
    visited.append(src)
    for v, w in graph[src]:
        if v == dst:
            return [(src, w), (dst, 0)]
        if v in visited:
            continue
        path = get_path(graph, v, dst, visited)
        if path is not None:
            return [(src, w)] + path


def insert(graph, path, distance, m):
    curr = 0
    length = path[0][1]
    curr_node, next_node, = path[curr][0], path[curr + 1][0]

    while True:
        if distance < length:
            break
        distance -= length
        curr += 1
        length = path[curr][1]
        curr_node, next_node = path[curr][0], path[curr + 1][0]

    graph[curr_node].append((m, distance))
    graph[next_node].append((m, length - distance))
    graph[m] = [(curr_node, distance), (next_node, length - distance)]
    delete_edge(graph, curr_node, next_node)


def find_ij(d_matrix, n):
    for i in range(n - 1):
        for j in range(i + 1, n - 1):
            if d_matrix[i][j] == d_matrix[i][n - 1] + d_matrix[j][n - 1]:
                return i, j, d_matrix[i][n - 1]
    return 0, 0, 0


def additive_phylogeny(d_matrix, n, m, graph):
    if n == 2:
        distance = d_matrix[0][1]
        graph[0] = [(1, distance)]
        graph[1] = [(0, distance)]
        return graph

    limb_l = limb_length(d_matrix, n, n - 1)
    for i in range(n - 1):
        d_matrix[i][n - 1] -= limb_l
        d_matrix[n - 1][i] = d_matrix[i][n - 1]

    src, dst, x = find_ij(d_matrix, n)
    graph = additive_phylogeny(d_matrix, n - 1, m - 1, graph)
    path = get_path(graph, src, dst, [])
    insert(graph, path, x, m)
    graph[n - 1] = [(m, limb_l)]
    graph[m].append((n - 1, limb_l))
    return graph


def read_data():
    with open('../HW05/in.txt') as file:
        n = int(file.readline())
        lines = file.readlines()
        matrix = []
        for line in lines:
            matrix.append([int(x) for x in line.split()])
        matrix = np.array(matrix)
    return matrix, n


def print_graph(graph):
    for src in graph:
        for dst, length in graph[src]:
            print(src, '->', dst, ':', length, sep='')


if __name__ == '__main__':
    distance_matrix, n = read_data()

    graph = additive_phylogeny(distance_matrix, n, 2 * len(distance_matrix) - 3, dict())
    print_graph(graph)
