
def part1(data):
    digits = {}
    for number in data:
        for i, digit in enumerate(number):
            if i not in digits.keys():
                digits[i] = {'0': 0, '1':0}
            digits[i][digit] += 1
    gamma_rate = ''
    epsilon_rate = ''
    for i in range(len(digits.keys())):
        gamma_rate += max(digits[i], key=digits[i].get)
        epsilon_rate += min(digits[i], key=digits[i].get)
    return int(gamma_rate, 2) * int(epsilon_rate, 2)


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
    return l.strip()

def run():
    data = [parseline(line) for line in open('day3.input')]
    print(f'Part 1: {part1(data)}')
    #print(f'Part 2: {part2(data)}')

if __name__ == '__main__':
    run()