import os, time
import day_1.part_1
import day_1.part_2

directory = os.path.abspath(os.path.dirname(__file__))

def GetAndPrintResults(day : int, part : int, input_data : str, func):
    start = time.perf_counter_ns()
    result = func(input_data)
    end = time.perf_counter_ns()
    print(f'{day}-{part}\t{result}\t{(end-start) / 1_000_000}ms')


print('Advent of Code 2021\nKyle Akerstrom\n-------------------')
with open(f'{directory}\\day_1\\input.txt', 'r') as file:
    contents = file.read()
    GetAndPrintResults(1, 1, contents, day_1.part_1.Run)
    GetAndPrintResults(1, 1, contents, day_1.part_2.Run)
