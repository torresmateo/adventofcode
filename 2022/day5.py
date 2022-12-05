load_stacks = True

stacks = {i:[] for i in range(1, 10)}
index_map = {
    1: 1, 2: 5, 3:9, 4:13, 5:17, 6:21, 7:25, 8:29, 9:33
}

for line in open("day5.input"):
    line = line

    if len(line) < 5:
        continue
    
    if load_stacks and len(line) < 33:
        load_stacks = False
        for i in stacks.keys():
            stacks[i].pop()
            stacks[i] = list(reversed(stacks[i]))

    if load_stacks:
        for i in stacks.keys():
            if line[index_map[i]] != " ":
                stacks[i].append(line[index_map[i]])
    else:
        parts = line.strip().split()
        n = int(parts[1])
        f = int(parts[3])
        t = int(parts[5])
        for i in range(n):
            e = stacks[f].pop()
            stacks[t].append(e)

print("".join([stacks[i][-1] for i in range(1, 10)]))
        
load_stacks = True
stacks = {i:[] for i in range(1, 10)}
index_map = {
    1: 1, 2: 5, 3:9, 4:13, 5:17, 6:21, 7:25, 8:29, 9:33
}

for line in open("day5.input"):
    line = line

    if len(line) < 5:
        continue
    
    if load_stacks and len(line) < 33:
        load_stacks = False
        for i in stacks.keys():
            stacks[i].pop()
            stacks[i] = list(reversed(stacks[i]))

    if load_stacks:
        for i in stacks.keys():
            if line[index_map[i]] != " ":
                stacks[i].append(line[index_map[i]])
    else:
        parts = line.strip().split()
        n = int(parts[1])
        f = int(parts[3])
        t = int(parts[5])
        stacks[t] = stacks[t] + stacks[f][-n:]
        for i in range(n):
            stacks[f].pop()

print("".join([stacks[i][-1] for i in range(1, 10)]))
