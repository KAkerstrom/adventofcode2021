import os, time
import day_1.part_1
import day_1.part_2

directory = os.path.abspath(os.path.dirname(__file__))

print('Advent of Code 2021\nKyle Akerstrom\n-------------------')
with open(f'{directory}\\day_1\\input.txt', 'r') as file:
    contents = file.read()
    start = time.perf_counter_ns()
    result = day_1.part_1.Run(contents)
    end = time.perf_counter_ns()
    print(f'1-1\t{result}\t{(end-start) / 1_000_000}ms')

    start = time.perf_counter_ns()
    result = day_1.part_2.Run(contents)
    end = time.perf_counter_ns()
    print(f'1-2\t{result}\t{(end-start) / 1_000_000}ms')
