priorities = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

total = 0

rucksacks = []
for line in open("day3.input"):
    line = line.strip()
    n = len(line)
    rucksacks.append(set(line))
    c1 = line[:n//2]
    c2 = line[n//2:]
    shared = set(c1) & set(c2)
    total += priorities.index(next(iter(shared))) + 1

print(f"part 1: {total}")

group_start = 0
total = 0
while group_start < len(rucksacks):
    r1, r2, r3 = rucksacks[group_start:group_start+3]
    shared = r1 & r2 & r3
    total += priorities.index(next(iter(shared))) + 1
    group_start += 3

print(f"part 2: {total}")
