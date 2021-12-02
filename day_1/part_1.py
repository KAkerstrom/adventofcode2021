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