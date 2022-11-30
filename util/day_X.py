import sys
sys.path.insert(0, '../util')
from profiler import profile
from parse import *

@profile
def part_one(data):
    ...

@profile
def part_two(data):
    ...

with open("day_X_input.txt") as f:
    data = f.read()
    print(f"Part One: {part_one(data)}")
    print(f"Part Two: {part_two(data)}")