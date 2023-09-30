from scipy.spatial import distance


def get_min(child, char, alphabet):
    min_value = 10000000000
    for i in alphabet:
        value = node_list[child].score[i] + int(char != i)
        if value < min_value:
            min_value = value
    return min_value


class Node:
    def __init__(self, index, leaf):
        self.index = index
        self.score = dict()
        self.label = ''
        self.tag = False
        self.leaf = leaf
        self.children = []
        self.edges = []

    def is_leaf(self):
        return self.leaf

    def is_ripe(self):
        if self.is_leaf():
            ripe = True
        else:
            ripe = True
            for i in self.children:
                if not node_list[i].tag:
                    ripe = False
                    break
        return ripe

    def scoring(self, character, alphabet):
        if self.is_leaf():
            for char in alphabet:
                self.score[char] = 0
                if char != self.label[character]:
                    self.score[char] = 100000000.0
        else:
            for char in alphabet:
                for child in self.children:
                    if char not in self.score.keys():
                        self.score[char] = 0
                    self.score[char] += get_min(child, char, alphabet)
        self.tag = True


def build_tree(node, parent_letter, alphabet):
    if not node.is_leaf():
        min_value = 100000000.0
        choice = ''
        for letter in alphabet:
            score = node.score[letter]
            if parent_letter != letter:
                score += 1
            if score < min_value:
                min_value = score
                choice = letter
        node.label += choice
        for i in node.children:
            build_tree(node_list[i], choice, alphabet)


def score_tree(character, alphabet):
    for node in node_list:
        if node.is_leaf():
            node.scoring(character, alphabet)
    while not node_list[-1].tag:
        for node in node_list:
            if not node.tag and node.is_ripe():
                node.scoring(character, alphabet)


def adjacency_list(node, labels):
    remaining_nodes = [node]
    while len(remaining_nodes) != 0:
        current_node = remaining_nodes.pop(0)
        for index, item in enumerate(current_node.children):
            child = node_list[item]
            labels.append(node.label + '->' + child.label + ':' + str(int(current_node.edges[index])))
            labels.append(child.label + '->' + node.label + ':' + str(int(current_node.edges[index])))
            remaining_nodes.append(child)
    return labels


def assign_score(node):
    score = 0
    remaining_nodes = [node]
    while len(remaining_nodes) != 0:
        current_node = remaining_nodes.pop(0)
        for index, item in enumerate(current_node.children):
            child = node_list[item]
            dd = distance.hamming(list(current_node.label), list(node_list[item].label)) * len(current_node.label)
            score += dd
            current_node.edges[index] = dd
            remaining_nodes.append(child)
    return score


def small_parsimony(alphabet):
    for char in range(len(node_list[0].label)):
        score_tree(char, alphabet)
        build_tree(node_list[-1], '', alphabet)
        for node in node_list:
            node.score = dict()
            node.tag = False
    score = assign_score(node_list[-1])
    labels = adjacency_list(node_list[-1], [])
    return labels, score


def print_graph(score, labels):
    print(int(score))
    print("%s\n" % ('\n'.join(labels)))


with open('../HW05/in.txt') as f:
    n = int(f.readline())
    node_list = [Node(i, True) for i in range(n)]
    lines = f.readlines()
    for i, line in enumerate(lines):
        l1, l2 = line.split('->')
        n1 = int(l1)
        if n1 == len(node_list):
            node_list.append(Node(n1, False))
        if i < n:
            node_list[n1].children.append(i)
            node_list[n1].edges.append(0)
            node_list[i].label = l2[:-1]
        if i >= n:
            node_list[n1].children.append(int(l2))
            node_list[n1].edges.append(0)

tree_labels, parsimony_score = small_parsimony('ACGT')
print_graph(parsimony_score, tree_labels)
