import sys
sys.path.insert(0, '../util')
from profiler import profile
from parse import *


class Directory:
    def __init__(self, size: int, parent: str, subs=[]):
        self.size = size
        self.parent = parent
        self.subs = subs


def calculate_directory_size(tree, dir):
    if not dir.subs:
        return dir.size
    size = dir.size
    size += sum(calculate_directory_size(tree, tree[sub]) for sub in dir.subs)
    return size


def build_tree(data):
    dirs = {"/": Directory(size=0, parent=None, subs=[])}
    cur_dir = ""
    for x in data:
        if x[0] == "$":
            if x[1] == "cd":
                cur_dir = dirs[cur_dir].parent if x[2] == ".." else (cur_dir+"/"+x[2] if cur_dir != "" else cur_dir+x[2])
        elif x[0] == "dir":
            dirs[cur_dir+"/"+x[1]] = Directory(0, cur_dir, [])
            dirs[cur_dir].subs.append(cur_dir+"/"+x[1])
        else:
            dirs[cur_dir].size += int(x[0])
    weights = [calculate_directory_size(dirs, dirs[x]) for x in dirs]
    return dirs, weights


@profile
def part_one(data):
    return sum(x for x in build_tree(data)[1] if x <= 100000)


@profile
def part_two(data):
    tree, weights = build_tree(data)
    to_free = 30000000 - (70000000 - calculate_directory_size(tree, tree["/"]))
    return min(x for x in weights if x >= to_free)


with open("day_7_input.txt") as f:
    data = [x.strip().split() for x in f.read().splitlines()]
    print(f"Part One: {part_one(data)}")
    print(f"Part Two: {part_two(data)}")