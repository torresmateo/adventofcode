elves = [0]

curr_elf = 0
for line in open("day1.input"):
    l = line.strip()
    if l:
        cals = int(l)
        elves[curr_elf] += cals
    else:
        curr_elf += 1
        elves.append(0)

print(f"part1: {max(elves)}")
print(f"part2: {sum(sorted(elves)[-3:])}")
