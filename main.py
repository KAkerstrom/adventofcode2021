import os, time
import day_1.part_1
import day_1.part_2
import day_2.part_1
import day_2.part_2
import day_3.part_1
import day_3.part_2
import day_4.part_1
import day_4.part_2
import day_5.part_1
import day_5.part_2

directory = os.path.abspath(os.path.dirname(__file__))

def GetAndPrintResults(day : int, part : int, input_data : str, func):
    start = time.perf_counter_ns()
    result = func(input_data)
    end = time.perf_counter_ns()
    if result == None:
        result = 'INVALID'
    print(f'{str.rjust(str(day), 2)}-{part}\t{str.ljust(result, 20)}{(end-start) / 1_000_000}ms')


print('\n\nAdvent of Code 2021\nKyle Akerstrom\n-------------------')

with open(f'{directory}\\day_1\\input.txt', 'r') as file:
    contents = file.read()
    GetAndPrintResults(1, 1, contents, day_1.part_1.Run)
    GetAndPrintResults(1, 1, contents, day_1.part_2.Run)

with open(f'{directory}\\day_2\\input.txt', 'r') as file:
    contents = file.read()
    GetAndPrintResults(2, 1, contents, day_2.part_1.Run)
    GetAndPrintResults(2, 2, contents, day_2.part_2.Run)

with open(f'{directory}\\day_3\\input.txt', 'r') as file:
    contents = file.read()
    GetAndPrintResults(3, 1, contents, day_3.part_1.Run)
    GetAndPrintResults(3, 2, contents, day_3.part_2.Run)

with open(f'{directory}\\day_4\\input.txt', 'r') as file:
    contents = file.read()
    GetAndPrintResults(4, 1, contents, day_4.part_1.Run)
    GetAndPrintResults(4, 2, contents, day_4.part_2.Run)

with open(f'{directory}\\day_5\\input.txt', 'r') as file:
    contents = file.read()
    GetAndPrintResults(5, 1, contents, day_5.part_1.Run)
    GetAndPrintResults(5, 2, contents, day_5.part_2.Run)

print('\n')