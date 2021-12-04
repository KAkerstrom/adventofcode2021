def Run(input):
    input = iter(input.splitlines())
    inc_count = 0
    buffer = [int(next(input)), int(next(input)), int(next(input))]
    prev_sum = sum(buffer)
    for line in input:
        buffer = [buffer[1], buffer[2], int(line)]
        curr_sum = sum(buffer)
        if curr_sum > prev_sum:
            inc_count += 1
        prev_sum = curr_sum
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
    aoc = '5'
    print(f'AoC: {aoc}\nYou: {result}{"  ☑" if result == aoc else "  ☒"}')