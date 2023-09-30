def bw_matching(last, patterns_list):
    output = []
    for pattern in patterns_list:
        top, bottom = 0, len(last) - 1
        first = sorted(last)
        while top <= bottom:
            if len(pattern) > 0:
                symbol, pattern = pattern[-1], pattern[:-1]
                if symbol in last[top:bottom + 1]:
                    top = first.index(symbol) + last.count(symbol, 0, top)
                    bottom = first.index(symbol) + last.count(symbol, 0, bottom + 1) - 1
                else:
                    output.append(0)
                    break
            else:
                output.append(bottom - top + 1)
                break
    return output


if __name__ == "__main__":
    with open("in.txt", "r") as file:
        lines = file.readlines()
        last_col = lines[0].strip()
        patterns = lines[1].strip().split()

    print(*bw_matching(last_col, patterns), sep=' ')
