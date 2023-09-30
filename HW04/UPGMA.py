import numpy as np


class Cluster(object):
    def __init__(self, id, age, size):
        self.id = id
        self.age = age
        self.nodes = size


def compute_distance(cluster1, cluster2, matrix):
    return sum(float(matrix[i][j]) for i in cluster1.nodes for j in cluster2.nodes) \
           / float(len(cluster1.nodes) * len(cluster2.nodes))


def find_closest_clusters(list_of_clusters, cluster_ids, dist_matrix):
    min_distance = 100000000
    for cluster1 in cluster_ids:
        for cluster2 in cluster_ids:
            if cluster1 != cluster2:
                cluster_1 = list_of_clusters[cluster1]
                cluster_2 = list_of_clusters[cluster2]
                distance = compute_distance(cluster_1, cluster_2, dist_matrix)
                if distance <= min_distance:
                    min_distance = distance
                    c1, c2 = cluster_1, cluster_2

    return c1, c2


def connect_nodes(graph, p, c1, c2):
    add_node(graph, c1.id, p.id, p.age - c1.age)
    add_node(graph, p.id, c1.id, p.age - c1.age)
    add_node(graph, c2.id, p.id, p.age - c2.age)
    add_node(graph, p.id, c2.id, p.age - c2.age)


def add_node(graph, id1, id2, distance):
    if id1 in graph.keys():
        graph[id1].append((id2, distance))
    else:
        graph[id1] = [(id2, distance)]


def update_distance_matrix(new_cluster, list_of_clusters, matrix):
    distances = [compute_distance(new_cluster, cluster, matrix) for cluster in list_of_clusters]
    matrix = np.column_stack((matrix, distances[:matrix.shape[0]]))
    matrix = np.row_stack((matrix, distances[:matrix.shape[1]]))
    return matrix


def upgma(dist_matrix, n):
    graph = dict()
    list_of_clusters = [Cluster(i, 0, [i]) for i in range(n)]
    clusters = list([i for i in range(n)])
    current_node = n

    while True:
        if len(clusters) < 2:
            break
        c1, c2 = find_closest_clusters(list_of_clusters, clusters, dist_matrix)
        age = compute_distance(c1, c2, dist_matrix) / 2
        new_cluster = Cluster(current_node, age, c1.nodes + c2.nodes)
        current_node += 1
        connect_nodes(graph, new_cluster, c1, c2)
        clusters.remove(c1.id)
        clusters.remove(c2.id)
        clusters.append(new_cluster.id)
        list_of_clusters.append(new_cluster)
        dist_matrix = update_distance_matrix(new_cluster, list_of_clusters, dist_matrix)
    return graph


def print_graph(graph):
    for u in range(len(graph)):
        for v, w in graph[u]:
            print(u, '->', v, ':', '%.3f' % w, sep='')


def read_data():
    with open('../HW05/in.txt') as file:
        n = int(file.readline())
        lines = file.readlines()
        matrix = []
        for line in lines:
            matrix.append([int(x) for x in line.split()])
        matrix = np.array(matrix)
    return matrix, n


if __name__ == '__main__':
    distance_matrix, n = read_data()
    g = upgma(distance_matrix, n)
    print_graph(g)
