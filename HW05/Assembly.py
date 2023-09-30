import numpy as np


def ASMQ(strings, n):
    strings.sort()
    strings = strings[::-1]
    percents = strings / np.sum(strings)
    per = 0
    for i, p in enumerate(percents):
        per += p
        if per > n:
            result = i
            break
    return strings[result]


if __name__ == '__main__':
    with open('in.txt', 'r') as f:
        lines = f.readlines()

    lines = [len(line.strip()) for line in lines]
    print(ASMQ(lines, .5), ASMQ(lines, .75))
