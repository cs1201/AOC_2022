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
    data = list(zip(*(iter(data),) * 3))
    return sum(get_priority(list(set(x[0]).intersection(x[1]).intersection(x[2]))[0]) for x in data)


with open("day_3_input.txt") as f:
    data = [x for x in f.read().splitlines()]
    print(f"Part One: {part_one(data)}")
    print(f"Part Two: {part_two(data)}")