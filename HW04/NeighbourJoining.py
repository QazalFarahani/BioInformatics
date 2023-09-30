import numpy as np


def create_d_prime(distances, matrix, n):
    dp = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            dp[i][j] = (n - 2) * matrix[i][j] - distances[i] - distances[j]
            dp[i][i] = 0
    return dp


def create_delta(distances, n):
    delta = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            delta[i][j] = (distances[i] - distances[j]) / (n - 2)
            delta[i][i] = 0
    return delta


def add_link(n1, n2, distance, graph):
    if n1 in graph.keys():
        graph[n1].append((n2, distance))
    else:
        graph[n1] = [(n2, distance)]


def get_new_row(matrix, i, j, n):
    row = []
    for k in range(n):
        value = (matrix[k][i] + matrix[k][j] - matrix[i][j]) / 2
        row.append(value)
    return row


def neighbor_joining(dist_matrix, n, nodes, graph):
    if len(nodes) == 0:
        nodes = list(range(n))

    if n == 2:
        add_link(nodes[0], nodes[1], dist_matrix[0][1], graph)
        add_link(nodes[1], nodes[0], dist_matrix[0][1], graph)
        return graph
    elif n > 2:
        distances = [sum(row) for row in dist_matrix]
        dp = create_d_prime(distances, dist_matrix, n)
        delta = create_delta(distances, n)
        min_value, (i, j) = np.min(dp), np.unravel_index(np.argmin(dp, axis=None), dp.shape)
        limb_i, limb_j = (dist_matrix[i][j] + delta[i][j]) / 2, (dist_matrix[i][j] - delta[i][j]) / 2

        new_row = get_new_row(dist_matrix, i, j, n)
        dist_matrix = np.column_stack((dist_matrix, (new_row + [0])[:dist_matrix.shape[0]]))
        dist_matrix = np.row_stack((dist_matrix, (new_row + [0])[:dist_matrix.shape[1]]))

        m = nodes[len(nodes) - 1] + 1
        nodes.append(m)

        dist_matrix = np.delete(dist_matrix, max(i, j), 0)
        dist_matrix = np.delete(dist_matrix, max(i, j), 1)
        dist_matrix = np.delete(dist_matrix, min(i, j), 0)
        dist_matrix = np.delete(dist_matrix, min(i, j), 1)

        node_i, node_j = nodes[i], nodes[j]
        nodes.remove(node_i)
        nodes.remove(node_j)
        graph = neighbor_joining(dist_matrix, n - 1, nodes, graph)

        add_link(node_i, m, limb_i, graph)
        add_link(m, node_i, limb_i, graph)
        add_link(node_j, m, limb_j, graph)
        add_link(m, node_j, limb_j, graph)
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
    for u in range(len(graph)):
        for v, w in graph[u]:
            print(u, '->', v, ':', '%.3f' % w, sep='')


if __name__ == '__main__':
    distance_matrix, n = read_data()
    g = neighbor_joining(distance_matrix, n, [], dict())
    print_graph(g)
