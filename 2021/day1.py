import numpy as np

def part1(data):
    previous = None
    increased = 0
    for i in data:
        if previous is None:
            previous = i
            continue
        if i > previous:
            increased += 1
        previous = i
    return increased


def part2(data):
    k = 3
    previous = None
    increased = 0
    for i in range(len(data) - k + 1):
        if previous is None:
            previous = np.sum(data[i:i+k])
            continue
        if np.sum(data[i:i+k]) > previous:
            increased += 1
        previous = np.sum(data[i:i+k])
    return increased

def run():
    data = [int(line.strip()) for line in open('day1.input')]
    print(f'Part 1: {part1(data)}')
    print(f'Part 2: {part2(data)}')

if __name__ == '__main__':
    run()