def match(s, k_mers, k, output):
    for n in range(len(k_mers)):
        index, match = -1, -1
        for i, dna in enumerate(k_mers):
            if dna[:k-1] == s:
                index, match = i, dna
                break
        if index == -1:
            return output
        else:
            output.append(k_mers[index])
            s = k_mers[index][1:]
            k_mers = k_mers[:index] + k_mers[index+1:]
            # output = coverings(k_mers[index][1:], k_mers[:index] + k_mers[index+1:], k, output)
    return output


if __name__ == '__main__':
    with open('in.txt', 'r') as f:
        lines = f.readlines()
    reads = [line.strip() for line in lines]
    n = len(reads)
    k = len(reads[0])

    super_string = ''
    out = match(reads[0][1:], reads[1:], k, [reads[0]])
    for dna in out:
        super_string += dna[-1]
    print(super_string)
