def Run(input):
    input = iter(input.splitlines())
    hor = 0
    ver = 0
    for line in input:
        line = line.split(' ')
        if line[0] == 'up':
            ver -= int(line[1])
        elif line[0] == 'down':
            ver += int(line[1])
        elif line[0] == 'forward':
            hor += int(line[1])
    return str(ver * hor)