import sys
sys.path.insert(0, '../util')
from profiler import profile
from parse import *

@profile
def part_one(data):
    for i in range(len(data)-4):
        if len(set(data[i:i+4])) == 4:
            return i+4

@profile
def part_two(data):
    for i in range(len(data)-14):
        if len(set(data[i:i+14])) == 14:
            return i+14

with open("day_6_input.txt") as f:
    data = f.read().strip()
    print(f"Part One: {part_one(data)}")
    print(f"Part Two: {part_two(data)}")