import sys
sys.path.insert(0, '../util')
from profiler import profile
from parse import *
from collections import defaultdict

def create_map(data):
    obs = defaultdict(lambda: False)
    for line in data:
        for i in range(len(line)-1):
            x1,y1 = line[i]
            x2,y2 = line[i+1]
            for dy in range(min(y1,y2), max(y1,y2)+1):
                for dx in range(min(x1,x2), max(x1,x2)+1):
                    obs[(dx,dy)] = True
    return obs

@profile
def part_one(data):
    sand_cnt = 0
    max_y = max([y for _,y in data])
    sx,sy = (500,0)
    while sy < max_y:
        for nx,ny in [(sx,sy+1),(sx-1,sy+1),(sx+1,sy+1)]:
            if not data[(nx,ny)]:
                sx,sy = nx,ny
                break
        else:
            data[(sx,sy)] = True
            sx, sy = (500,0)
            sand_cnt +=1
    return sand_cnt


@profile
def part_two(data):
        sand_cnt = 0
        max_y = max([y for _,y in data]) + 2
        sx,sy = (500,0)
        while not data[(500,0)]:
            for nx,ny in [(sx,sy+1),(sx-1,sy+1),(sx+1,sy+1)]:
                if not data[(nx,ny)] and sy < max_y-1:
                    sx,sy = nx,ny
                    break
            else:
                data[(sx,sy)] = True
                sx, sy = (500,0)
                sand_cnt +=1
        return sand_cnt


with open("day_14_input.txt") as f:
    data = [[tuple(map(int, x.split(','))) for x in line.split(" -> ")] for line in f.read().splitlines()]
    data = create_map(data)
    print(f"Part One: {part_one(data.copy())}")
    print(f"Part Two: {part_two(data.copy())}")