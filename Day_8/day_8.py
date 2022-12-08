import sys
sys.path.insert(0, '../util')
from profiler import profile
from parse import *


@profile
def part_one(data):
    x_len, y_len = len(data[0]), len(data)
    visible = (2*y_len) + 2*(x_len-2)
    data_transposed = list(zip(*data))
    for y, row in enumerate(data):
        for x, height in enumerate(row):
            if x == 0 or y == 0 or x == x_len-1 or y == y_len-1:
                continue
            left, right, above, below = data[y][:x], data[y][x+1:], data_transposed[x][:y], data_transposed[x][y+1:]
            visible += any([all(z < height for z in direction) for direction in [left,right,above,below]])
    return visible

@profile
def part_two(data):
    scores = []
    x_len, y_len = len(data[0]), len(data)
    data_transposed = list(zip(*data))
    for y, row in enumerate(data):
        for x, height in enumerate(row):
            if x == 0 or y == 0 or x == x_len-1 or y == y_len-1:
                continue
            left, right, above, below = data[y][:x], data[y][x+1:], data_transposed[x][:y][::-1], data_transposed[x][y+1:]
            score = 1
            for direction in [left[::-1], right, above, below]:
                vd = 0
                for step in direction:
                    vd+=1
                    if step >= height:
                        break
                score *= vd
            scores.append(score)
    return max(scores)

with open("day_8_input.txt") as f:
    data = f.read()
    data = [[int(x) for x in line] for line in data.splitlines()]
    print(f"Part One: {part_one(data)}")
    print(f"Part Two: {part_two(data)}")