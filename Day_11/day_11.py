import sys
sys.path.insert(0, '../util')
from profiler import profile
from parse import *
from typing import List
import math
from functools import reduce
from copy import deepcopy

class Monkey():
    def __init__(self, items: List[int], op, divisor: int, test_true: int, test_false: int):
        self.items = items
        self.op = op
        self.divisor = divisor
        self.test_true = test_true
        self.test_false = test_false
        self.inspection_count = 0

    def catch_item(self, item: int):
        self.items.append(item)
        return self.items

    def inspect_pt1(self):
        self.inspection_count += 1
        val = math.floor(self.op(self.items.pop(0))/3)
        return val, (self.test_true if val % self.divisor == 0 else self.test_false)

    def inspect_pt2(self, mod_product):
        self.inspection_count += 1
        val = self.op(self.items.pop(0)) % mod_product
        return val, (self.test_true if val % self.divisor == 0 else self.test_false)


def parse_monkey(data: str):
    data = data.splitlines()
    op_operator = data[2].split()[4]
    op_value = data[2].split()[5]
    op_value = int(op_value) if op_value.isdigit() else "x"
    if op_operator == "+":
        op_lambda = lambda x: x + (x if op_value == "x" else op_value)
    elif op_operator == "*":
        op_lambda = lambda x: x * (x if op_value == "x" else op_value)

    monkey = Monkey(
        items = [int(x.strip()) for x in data[1].split(":")[1].split(",")],
        op = op_lambda,
        divisor = int(data[3].split()[-1]),
        test_true = int(data[4].split()[-1]),
        test_false = int(data[5].split()[-1])
    )
    return monkey   

@profile
def part_one(data: List[Monkey]):
    for _ in range(20):
        for monkey in data:
            while len(monkey.items):
                item, new_monkey = monkey.inspect_pt1()
                data[new_monkey].catch_item(item)
    a,b= sorted([x.inspection_count for x in data])[-2:]
    return a*b


@profile
def part_two(data):
    mod_product = reduce(lambda x,y: x*y, [x.divisor for x in data])
    for _ in range(10000):
        for monkey in data:
            while len(monkey.items):
                item, new_monkey = monkey.inspect_pt2(mod_product)
                data[new_monkey].catch_item(item)
    a,b= sorted([x.inspection_count for x in data])[-2:]
    return a*b


with open("day_11_input.txt") as f:
    data = [parse_monkey(x.strip()) for x in f.read().split("\n\n")]
    print(f"Part One: {part_one(deepcopy(data))}")
    print(f"Part Two: {part_two(deepcopy(data))}")