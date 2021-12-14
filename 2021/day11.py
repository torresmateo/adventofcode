import numpy as np

def neighbors(m, i, j):
    h, w = m.shape
    coords = [
        (i-1, j-1),
        (i-1, j),
        (i-1, j+1),
        (i, j-1), 
        (i, j+1),
        (i+1, j-1),
        (i+1, j),
        (i+1, j+1),
    ]
    neighbors = []
    for r, c in coords:
        if 0 <= r < h and 0 <= c < w:
            neighbors.append((r, c)) 
    return neighbors

def part1(m):
    h, w = m.shape
    curr_state = m
    new_state = np.zeros((h,w))
    num_flashes = 0
    for _ in range(100):
        new_state = curr_state + 1
        flash_r, flash_c = np.where(new_state > 9)
        seen_flashes = []
        new_flashes = [(flash_r[i], flash_c[i]) for i in range(len(flash_r))]
        while new_flashes:
            i, j = new_flashes.pop()
            seen_flashes.append((i, j))
            for r, c in neighbors(new_state, i, j):
                new_state[r, c] += 1
            flash_r, flash_c = np.where(new_state > 9)
            for i in range(len(flash_r)):
                if (flash_r[i], flash_c[i]) not in seen_flashes and (flash_r[i], flash_c[i]) not in new_flashes:
                    new_flashes.append((flash_r[i], flash_c[i]))
        flash_r, flash_c = np.where(new_state > 9)
        new_state[flash_r, flash_c] = 0
        num_flashes += (new_state == 0).sum()

        curr_state = new_state
    return num_flashes

def part2(m):
    h, w = m.shape
    curr_state = m
    new_state = np.zeros((h,w))
    num_flashes = 0
    step = 0
    while True:
        step += 1
        new_state = curr_state + 1
        flash_r, flash_c = np.where(new_state > 9)
        seen_flashes = []
        new_flashes = [(flash_r[i], flash_c[i]) for i in range(len(flash_r))]
        while new_flashes:
            i, j = new_flashes.pop()
            seen_flashes.append((i, j))
            for r, c in neighbors(new_state, i, j):
                new_state[r, c] += 1
            flash_r, flash_c = np.where(new_state > 9)
            for i in range(len(flash_r)):
                if (flash_r[i], flash_c[i]) not in seen_flashes and (flash_r[i], flash_c[i]) not in new_flashes:
                    new_flashes.append((flash_r[i], flash_c[i]))
        flash_r, flash_c = np.where(new_state > 9)
        new_state[flash_r, flash_c] = 0
        num_flashes = (new_state == 0).sum()
        if num_flashes == 100 or step > 10000:
            break
        curr_state = new_state
    return step

def parsefile(infile):
    values = []
    for line in open(infile):
        line = line.strip()
        values.append([int(i) for i in line])
    return np.array(values)

def run():
    m = parsefile('day11.input')
    print(f'Part 1: {part1(m)}')
    print(f'Part 2: {part2(m)}')
    
if __name__ == '__main__':
    run()