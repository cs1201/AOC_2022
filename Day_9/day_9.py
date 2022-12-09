import sys
sys.path.insert(0, '../util')
from profiler import profile
from parse import *
from typing import NamedTuple

class coord(NamedTuple):
    x: int
    y: int

def move_head(dir, h: coord):
    if dir == "L":
        h = coord(h.x-1, h.y)
    elif dir == "R":
        h = coord(h.x+1, h.y)
    elif dir == "U":
        h = coord(h.x, h.y+1)
    elif dir == "D":
        h = coord(h.x, h.y-1)
    return h

def update_knot(h: coord, t: coord):
    if ((abs(t.x - h.x) > 1 or abs(t.y - h.y) > 1)):
        if t.x < h.x:
            t = coord(t.x+1, t.y)
        if t.x > h.x:
            t = coord(t.x-1, t.y)
        if t.y < h.y:
            t = coord(t.x, t.y+1)
        if t.y > h.y:
            t = coord(t.x, t.y-1)
    return t

@profile
def part_one(data):
    h, t = coord(0,0), coord(0,0)
    tail_positions = [t]
    for dir, mag in data:
        for _ in range(mag):
            h = move_head(dir, h)
            t = update_knot(h, t)
            tail_positions.append(t)
    return len(set(tail_positions))

@profile
def part_two(data):
    rope = [coord(0,0) for _ in range(10)]
    tail_positions = [rope[-1]]
    for dir, mag in data:
        for _ in range(mag):
            rope[0] = move_head(dir, rope[0])
            for i, knot in enumerate(rope[1:]):
                rope[i+1] = update_knot(rope[i], knot)
            tail_positions.append(rope[-1])
    return len(set(tail_positions))

with open("day_9_input.txt") as f:
    data = [(x.split()[0], int(x.split()[1])) for x in f.read().splitlines()]
    print(f"Part One: {part_one(data)}")
    print(f"Part Two: {part_two(data)}")