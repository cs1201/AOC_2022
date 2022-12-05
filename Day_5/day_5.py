import sys
sys.path.insert(0, '../util')
from profiler import profile
from parse import *
from copy import deepcopy


@profile
def part_one(crates, moves):
    for n,s,e in moves:
        for _ in range(n):
            crates[e-1].append(crates[s-1].pop())
    return "".join([x.pop() for x in crates])


@profile
def part_two(crates, moves):
    for n,s,e in moves:
        crates[e-1].extend(crates[s-1][-n:])
        crates[s-1] = crates[s-1][:-n]
    return "".join([x.pop() for x in crates])


with open("day_5_input.txt") as f:
    crates, moves = f.read().split("\n\n")
    moves = [[int(x) for x in x.split() if x.isdigit()] for x in moves.splitlines()]
    crates = list(zip(*[x[1::4] for x in crates.splitlines()[:-1][::-1]]))
    crates = [[x for x in line if x != " "] for line in crates]
    print(f"Part One: {part_one(deepcopy(crates), moves)}")
    print(f"Part Two: {part_two(deepcopy(crates), moves)}")