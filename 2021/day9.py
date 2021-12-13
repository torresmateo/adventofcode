import numpy as np

def part1(values):
    h, w = values.shape
    mins_r = []
    mins_c = []
    for i in range(h):
        for j in range(w):
            value = values[i,j]
            coords = [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]
            neighbors = []
            for r, c in coords:
                if 0 <= r < h and 0 <= c < w:
                    neighbors.append(values[r, c])
            if all(value < n for n in neighbors):
                mins_r.append(i)
                mins_c.append(j)
    return np.sum(values[(mins_r, mins_c)]) + values[(mins_r, mins_c)].shape[0]



def part2(values):

    h, w = values.shape
    mins_r = []
    mins_c = []
    for i in range(h):
        for j in range(w):
            value = values[i,j]
            coords = [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]
            neighbors = []
            for r, c in coords:
                if 0 <= r < h and 0 <= c < w:
                    neighbors.append(values[r, c])
            if all(value < n for n in neighbors):
                mins_r.append(i)
                mins_c.append(j)
    basins = []
    for coord in range(len(mins_r)):
        i, j = mins_r[coord], mins_c[coord]
        visited = [(i, j)]
        coords = [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]
        to_visit = []
        for r, c in coords:
            if 0 <= r < h and 0 <= c < w and values[r,c] != 9 and (r, c) not in visited:
                to_visit.append((r, c))
        while to_visit:
            r, c = to_visit.pop()
            visited.append((r, c))
            coords = [(r-1, c), (r+1, c), (r, c-1), (r, c+1)]
            for y, x in coords:
                if 0 <= y < h and 0 <= x < w and values[y,x] != 9 and (y, x) not in visited and (y, x) not in to_visit:
                    to_visit.append((y, x))
        basins.append(visited.copy())
    basins = sorted(basins, key=len)
    top_sizes = [len(b) for b in basins[-3:]]
    return np.prod(top_sizes)

def parsefile(infile):
    values = []
    for line in open(infile):
        line = line.strip()
        values.append([int(i) for i in line])
    return np.array(values)

def run():
    values = parsefile('day9.input')
    print(f'Part 1: {part1(values)}')
    print(f'Part 2: {part2(values)}')
    
if __name__ == '__main__':
    run()