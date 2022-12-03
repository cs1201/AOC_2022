import sys
sys.path.insert(0, '../util')
from profiler import profile
from parse import *
from itertools import islice

def get_priority(x):
    return ord(x) - (96 if x.islower() else 38)

@profile
def part_one(data):
    return sum(get_priority(list(set(bag[:int(len(bag)/2)]).intersection(bag[int(len(bag)/2):]))[0]) for bag in data)

@profile
def part_two(data):
    iterator = iter(data)
    total = 0
    while chunk := list(islice(iterator, 3)):
        common = list(set(chunk[0]).intersection(chunk[1]).intersection(chunk[2]))[0]
        total +=  get_priority(common)
    return total


with open("day_3_input.txt") as f:
    data = [x for x in f.read().splitlines()]
    print(f"Part One: {part_one(data)}")
    print(f"Part Two: {part_two(data)}")