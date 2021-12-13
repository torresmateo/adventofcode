import numpy as np

def part1(state):
    leftmost = min(state)
    rightmost = max(state)
    min_position = np.inf
    min_cost = np.inf
    for h in range(leftmost, rightmost + 1):
        curr_cost = 0
        for s in state:
            curr_cost += np.abs(s - h)
        if curr_cost < min_cost:
            min_position = h
            min_cost = curr_cost
    return min_cost

def part2(state):
    leftmost = min(state)
    rightmost = max(state)
    min_position = np.inf
    min_cost = np.inf
    for h in range(leftmost, rightmost + 1):
        curr_cost = 0
        for s in state:
            curr_cost += np.sum(np.arange(np.abs(s - h) + 1))
        if curr_cost < min_cost:
            min_position = h
            min_cost = curr_cost
    return min_cost

def run():
    state = [int(i) for i in open('day7.input').read().strip().split(',')]
    print(f'Part 1: {part1(state)}')
    print(f'Part 2: {part2(state)}')
    
if __name__ == '__main__':
    run()