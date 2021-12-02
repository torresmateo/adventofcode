
def part1(data):
    x, y = 0, 0
    for command, amount in data:
        if command == 'forward':
            x += amount
        elif command == 'down':
            y += amount
        elif command == 'up':
            y -= amount
    return x * y


def part2(data):
    x, y, aim = 0, 0, 0
    for command, amount in data:
        if command == 'forward':
            x += amount
            y += aim * amount
        elif command == 'down':
            aim += amount
        elif command == 'up':
            aim -= amount
    return x * y

def parseline(l):
    command, amount = l.strip().split()
    return command, int(amount)

def run():
    data = [parseline(line) for line in open('day2.input')]
    print(f'Part 1: {part1(data)}')
    print(f'Part 2: {part2(data)}')

if __name__ == '__main__':
    run()