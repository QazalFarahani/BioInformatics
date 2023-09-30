def reverse_complement(read):
    seq = read.replace("A", "t").replace("C", "g").replace("T", "a").replace("G", "c")
    return str(seq.upper()[::-1])


def create_super_string(dna):
    l = len(dna[0])
    k = l - 1
    main_list = dna

    for k in range(l - 1, 1, -1):
        adj_list = {}
        for d in main_list:
            adj_list[d[:k]] = d[1:k + 1]
        main_list = list(adj_list.items())
        temp_list = []
        for item in main_list:
            temp_list.append(item[0])
            temp_list.append(item[1])
        main_list = temp_list
        first_node = next(iter(adj_list))
        current = first_node
        super_string = ''

        while True:
            if current in adj_list:
                super_string += current[-1]
                current = adj_list.pop(current)
                if first_node == current:
                    return super_string
            else:
                break


if __name__ == '__main__':
    with open('in.txt', 'r') as f:
        lines = f.readlines()

    lines = [line.strip() for line in lines]
    rcs = [reverse_complement(line) for line in lines]
    lines.extend(rcs)

    res_string = create_super_string(lines)
    print(res_string)
