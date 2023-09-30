def reverse_complement(read):
    seq = read.replace("A", "t").replace(
        "C", "g").replace("T", "a").replace("G", "c")
    return str(seq.upper()[::-1])


def create_tree(nodes):
    adj_list = set()
    for node in nodes:
        rc = reverse_complement(node)
        if node not in adj_list:
            adj_list.add(node)
        if rc not in adj_list:
            adj_list.add(rc)
    return adj_list


if __name__ == '__main__':
    with open('in.txt', 'r') as f:
        lines = f.readlines()

    lines = [line.strip() for line in lines]
    de_bruijn = create_tree(lines)
    [print("(", edge[:-1], ", ", edge[1:], ")", sep='') for edge in de_bruijn]
