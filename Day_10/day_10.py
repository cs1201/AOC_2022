import sys
sys.path.insert(0, '../util')
from profiler import profile
from parse import *

@profile
def part_one(data):
    strength = []
    x = cycle = 1
    for op in data:
        strength.append(x*(cycle))
        cycle += 1
        if op[0] == "addx":
            strength.append(x*(cycle))
            cycle += 1
            x += int(op[1])
    return sum(strength[i-1] for i in [20, 60, 100, 140, 180, 220])


@profile
def part_two(data):
    screen = list(list('.' for _ in range(40)) for _ in range(6))
    cycle, x = 0, 1
    for op in data:
        if cycle%40 in range(x-1, x+2):
            screen[cycle//40][cycle % 40] = "#"
        cycle += 1
        if op[0] == "addx":
            if cycle%40 in range(x-1, x+2):
                screen[cycle//40][cycle % 40] = "#"
            cycle += 1
            x += int(op[1])
    for line in screen:
        print(''.join(line))


with open("day_10_input.txt") as f:
    data = [[x for x in line.split()] for line in f.readlines()]
    print(f"Part One: {part_one(data)}")
    print(f"Part Two: {part_two(data)}")