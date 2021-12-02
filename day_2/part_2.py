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