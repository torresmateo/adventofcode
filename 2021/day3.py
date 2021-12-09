
import collections


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
    from collections import Counter 
    oxygen_rating = 'not_found'
    curr_data = data
    for i in range(len(data[0])):
        commons = Counter([d[i] for d in curr_data])
        max_common = max(commons, key=commons.get)
        print(commons, max_common)
        curr_data = [d for d in curr_data if d[i] == max_common]
        print(i, len(curr_data))
        if len(curr_data) == 1:
            oxygen_rating = curr_data[0]
            break
        
    co2_rating = 'not_found'
    curr_data = data
    for i in range(len(data[0])):
        commons = Counter([d[i] for d in curr_data])
        min_common = min(commons, key=commons.get)
        curr_data = [d for d in curr_data if d[i] == min_common]
        if len(curr_data) == 1:
            co2_rating = curr_data[0]
            break
    print(f'[{oxygen_rating}, {co2_rating}]')
    return int(oxygen_rating, 2) * int(co2_rating, 2)

def parseline(l):
    return l.strip()

def run():
    data = [parseline(line) for line in open('day3.input')]
    print(f'Part 1: {part1(data)}')
    print(f'Part 2: {part2(data)}')

if __name__ == '__main__':
    run()