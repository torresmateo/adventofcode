from collections import defaultdict

def part1(coords):
    visited_coords = defaultdict(int)
    for (x1, y1), (x2, y2) in coords:
        if x1 == x2:
            m = min(y1, y2)
            M = max(y1, y2)
            for i in range(m, M + 1):
                visited_coords[x1, i] += 1    
        if y1 == y2:
            m = min(x1, x2)
            M = max(x1, x2)
            for i in range(m, M + 1):
                visited_coords[i, y1] += 1
    counter = 0
    for v in visited_coords.values():
        if v >= 2:
            counter += 1
    return counter

def part2(coords):
    visited_coords = defaultdict(int)
    for (x1, y1), (x2, y2) in coords:
        if x1 == x2:
            m = min(y1, y2)
            M = max(y1, y2)
            for i in range(m, M + 1):
                visited_coords[x1, i] += 1
            continue
        if y1 == y2:
            m = min(x1, x2)
            M = max(x1, x2)
            for i in range(m, M + 1):
                visited_coords[i, y1] += 1
            continue
        x_start = min(x1, x2)
        x_end = max(x1, x2)
        x_dir = 1 if x1 < x2 else -1
        y_dir = 1 if y1 < y2 else -1
        for i in range(x_end - x_start + 1):
            visited_coords[x1 + x_dir*i, y1 + y_dir*i] += 1
    counter = 0
    for v in visited_coords.values():
        if v >= 2:
            counter += 1
    return counter

def parsefile(infile):
    lines = []
    for line in open(infile):
        fp, sp = line.strip().split(' -> ')
        fp = tuple(int(i) for i in fp.split(','))
        sp = tuple(int(i) for i in sp.split(','))
        lines.append([fp, sp])
    return lines

def run():
    coords = parsefile('day5.input')
    print(f'Part 1: {part1(coords)}')
    print(f'Part 2: {part2(coords)}')
    
if __name__ == '__main__':
    run()