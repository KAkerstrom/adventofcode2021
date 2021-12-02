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