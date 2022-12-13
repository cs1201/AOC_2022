import sys
sys.path.insert(0, '../util')
from profiler import profile
import ast
from functools import cmp_to_key

CORRECT = 1
INCORRECT = -1
CONTINUE = None


def parse_pair(l,r):
    if isinstance(l, list) and isinstance(r, list):
        for i in range(max(len(l),len(r))):
            if i >= len(l):
                return CORRECT
            elif i >= len(r):
                return INCORRECT
            x = parse_pair(l[i], r[i])
            if x != CONTINUE:
                return x
    elif isinstance(l, int) and isinstance(r,int):
        return CORRECT if (l<r) else INCORRECT if (l > r) else CONTINUE
    elif isinstance(l, int) and isinstance(r, list):
        x = parse_pair([l],r)
        if x != CONTINUE:
            return x
    elif isinstance(l, list) and isinstance(r,int):
        x = parse_pair(l,[r])
        if x != CONTINUE:
            return x


@profile
def part_one(data):
    return sum([i+1 for i,(l,r) in enumerate(data) if parse_pair(l,r) == 1])


@profile
def part_two(data):
    data = [x for pair in data for x in pair]
    add1, add2 = ast.literal_eval('[[2]]'), ast.literal_eval('[[6]]')
    data.extend([add1, add2])
    sorted_packets = sorted(data, key=cmp_to_key(parse_pair), reverse=True)
    return (sorted_packets.index(add1)+1) * (sorted_packets.index(add2)+1)


with open("day_13_input.txt") as f:
    data = [[ast.literal_eval(p) for p in x.split()] for x in f.read().split("\n\n")]
    print(f"Part One: {part_one(data)}")
    print(f"Part Two: {part_two(data)}")