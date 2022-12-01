import sys
sys.path.insert(0, '../util')
from profiler import profile
from parse import *

@profile
def part_one(data):
    return max(data)

@profile
def part_two(data):
    return sum(sorted(data)[-3:])

with open("day_1_input.txt") as f:
    data = [sum([int(x) for x in elf.split()]) for elf in f.read().split("\n\n")]
    print(f"Part One: {part_one(data)}")
    print(f"Part Two: {part_two(data)}")