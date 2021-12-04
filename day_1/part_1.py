def Run(input):
    input = iter(input.splitlines())
    inc_count = 0
    prev = int(next(input))
    for line in input:
        curr = int(line)
        if curr > prev:
            inc_count += 1
        prev = curr
    return str(inc_count)

if __name__ == '__main__':
    result = Run('''199
200
208
210
200
207
240
269
260
263''')
    aoc = '7'
    print(f'AoC: {aoc}\nYou: {result}{"  ☑" if result == aoc else "  ☒"}')