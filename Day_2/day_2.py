import sys
sys.path.insert(0, '../util')
from profiler import profile
from parse import *

score = {
    "A": 1,
    "B": 2,
    "C": 3,
    "X": 1,
    "Y": 2,
    "Z": 3
}

outcomes = [
    [3, 6, 0],
    [0, 3, 6],
    [6, 0, 3]
]

@profile
def part_one(data):
    return sum(y + outcomes[x-1][y-1] for x,y in data)

@profile
def part_two(data):
    result = {1: 0, 2: 3, 3: 6}
    return sum(result[y] + outcomes[x-1].index(result[y]) + 1 for x,y in data)

with open("day_2_input.txt") as f:
    data = [(score[x.split()[0]], score[x.split()[1]]) for x in f.read().splitlines()]
    print(f"Part One: {part_one(data)}")
    print(f"Part Two: {part_two(data)}")