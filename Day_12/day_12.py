import sys
sys.path.insert(0, '../util')
from profiler import profile
from parse import *
from collections import deque

def get_neighbours(cur, points):
    neighbours = []
    x,y = cur
    for (nx, ny) in [(x-1,y), (x+1,y), (x,y-1), (x,y+1)]:
        if (nx,ny) in points.keys():
            if points[(nx,ny)] <= points[cur] + 1:
                neighbours.append((nx,ny))
    return neighbours


def bfs(start, end, points):
    distance = {start: 0}
    previous = {start: None}
    q = deque([start])
    visited = set([start])
    while q:
        current = q.popleft()
        if current == end:
            break
        neighbours = get_neighbours(current, points)
        for n in neighbours:
            if n in visited:
                continue
            q.append(n)
            visited.add(n)
            distance[n] = distance[current] + 1
            previous[n] = current
    return distance

@profile
def part_one(data):
    points = {}
    for y, row in enumerate(data):
        for x, height in enumerate(row):
            if height == "S":
                start = (x,y)
                height = "a"
            elif height == "E":
                end = (x,y)
                height = "z"
            points[(x,y)] = ord(height) - 97
    return bfs(start, end, points)[end]
    
@profile
def part_two(data):
    possible_starts = []
    distances = []
    points = {}
    for y, row in enumerate(data):
        for x, height in enumerate(row):
            if height in ["S", "a"]:
                possible_starts.append((x,y))
                height = "a"
            elif height == "E":
                end = (x,y)
                height = "z"
            points[(x,y)] = ord(height) - 97
    for s in possible_starts:
        d = bfs(s, end, points)
        if end in d.keys():
            distances.append(d[end])
    return min(distances)


with open("day_12_input.txt") as f:
    data = [[x for x in line] for line in f.read().splitlines()]
    print(f"Part One: {part_one(data)}")
    print(f"Part Two: {part_two(data)}")