def Run(input):
    input = iter(input.splitlines())
    aim = 0
    ver = 0
    hor = 0
    for line in input:
        line = line.split(' ')
        if line[0] == 'up':
            aim -= int(line[1])
        elif line[0] == 'down':
            aim += int(line[1])
        elif line[0] == 'forward':
            dist = int(line[1])
            hor += dist
            ver += aim * dist
    return str(ver * hor)

if __name__ == '__main__':
    result = Run('''forward 5
down 5
forward 8
up 3
down 8
forward 2''')
    aoc = '900'
    print(f'AoC: {aoc}\nYou: {result}{"  ☑" if result == aoc else "  ☒"}')