import numpy as np

def part1(state):
    steps = 80
    curr_state = state.copy()
    for _ in range(steps):
        new_fish = []
        for i, f in enumerate(curr_state):
            f -= 1
            if f < 0:
                new_fish.append(8)
            curr_state[i] = f if f >= 0 else 6
        curr_state += new_fish
    return len(curr_state)

def part2(state):
    steps = 256
    curr_status = {k:0 for k in range(9)}
    for n in state:
        curr_status[n] += 1
    for _ in range(steps):
        new_status = {}
        for n in range(9):
            if n == 8:
                new_status[n] = curr_status[0]
            elif n == 6:
                new_status[n] = curr_status[0] + curr_status[7]
            else:
                new_status[n] = curr_status[n+1]
        curr_status = new_status
    return sum(v for v in curr_status.values())

def run():
    state = [int(i) for i in open('day6.input').read().strip().split(',')]
    print(f'Part 1: {part1(state)}')
    print(f'Part 2: {part2(state)}')
    
if __name__ == '__main__':
    run()