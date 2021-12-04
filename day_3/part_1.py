def Run(input):
    input = input.splitlines()
    counts = [0] * len(input[0])
    total_count = 0
    for line in input:
        total_count += 1
        for i, val in enumerate(line):
            if val == '1':
                counts[i] += 1
    half = total_count / 2
    most_common = ['1' if x > half else '0' for x in counts]
    least_common = ['0' if x == '1' else '1' for x in most_common]
    gamma = int(''.join(x for x in most_common), 2)
    epsilon = int(''.join(x for x in least_common), 2)
    return str(gamma * epsilon)

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
    aoc = '198'
    print(f'AoC: {aoc}\nYou: {result}{"  ☑" if result == aoc else "  ☒"}')