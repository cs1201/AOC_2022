def parse_ints(s):
    return [int(x) for x in s.split()]

def parse_ints_comma(s):
    return [int(x) for x in s.split(',')]

def parse_coords_int(s):
    coords = {}
    for y,line in enumerate(s.splitlines()):
        for x,c in enumerate(line):
            coords[(x,y)] = int(c)
    return coords

def parse_coords_hash(s):
    coords = set()
    for y,line in enumerate(s.splitlines()):
        for x,c in enumerate(line):
            if c == "#":
                coords.add((x,y))
    return coords
