# This needs refactoring big time...


def checkDigit(vals, valid_list, most):
    entries = 0
    ones = 0
    for i, val in enumerate(vals):
        if valid_list[i]:
            entries += 1
            if val == '1':
                ones += 1
    half  = entries  / 2
    common  = '1' if ones > half else ('0' if ones < half else '')
    for i, val in enumerate(vals):
            if valid_list[i]:
                if common != '':
                    if (most and val != common) or (not most and val == common):
                        valid_list[i] = False
                        entries -= 1
                else:
                    if most and val != '1':
                        valid_list[i] = False
                        entries -= 1
                    elif not most and val != '0':
                        valid_list[i] = False
                        entries -= 1
    if entries == 1:
        return valid_list.index(True)
    else:
        return None

def Run(data):
    o2 = None
    co2 = None

    data = data.splitlines()
    valid_most = [True] * len(data)
    valid_least = [True] * len(data)
    for i in range(len(data[0])):
        vals = [x[i] for x in data]
        if o2 == None:
            index = checkDigit(vals, valid_most, True)
            if index != None:
                o2 = int(''.join(x for x in data[index]), 2)
        if co2 == None:
            index = checkDigit(vals, valid_least, False)
            if index != None:
                co2 = int(''.join(x for x in data[index]), 2)
    return str(o2 * co2)

if __name__ == '__main__':
    result = Run('''00100
11110
10110
10111
10101
01111
00111
11100
10000
11001
00010
01010''')
    aoc = '230'
    print(f'AoC: {aoc}\nYou: {result}{"  ☑" if result == aoc else "  ☒"}')