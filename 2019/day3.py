from collections import defaultdict
import numpy as np

def print_world(w):
    wire0 = np.zeros((10,10))
    wire1 = np.zeros((10,10))
    for r,c in w[0].keys():
        wire0[r,c] = 1
    for r,c in w[1].keys():
        wire1[r,c] = 1
    zawarudo = wire0 + wire1
    print(zawarudo)


wires = [i.strip().split(',') for i in open('day3.input').read().split('\n')]

world = {i:defaultdict(int) for i in range(len(wires))}

for i in range(len(wires)):
    r=c=0
    step = 1
    for coord in wires[i]:
        if coord.startswith('U'):
            for k in range(1,int(coord[1:])+1):
                if (r+k,c) not in world[i]:
                    world[i][(r+k,c)] = step
                step += 1
            r+=k
        elif coord.startswith('D'):
            for k in range(1,int(coord[1:])+1):
                if (r-k,c) not in world[i]:
                    world[i][(r-k,c)] = step
                step += 1
            r-=k
        elif coord.startswith('R'):
            for k in range(1,int(coord[1:])+1):
                if (r,c+k) not in world[i]:
                    world[i][(r,c+k)] = step
                step += 1
            c+=k
        elif coord.startswith('L'):
            for k in range(1,int(coord[1:])+1):
                if (r,c-k) not in world[i]:
                    world[i][(r,c-k)] = step
                step += 1
            c-=k

intersections = set(world[0].keys()) & set(world[1].keys())
intersections -= {(0,0)}
distances = [abs(r)+abs(c) for r,c in intersections]
print('part1', min(distances))

distances2 = [world[0][r,c] + world[1][r,c] for r,c in intersections]
print('part2', min(distances2))


#print_world(world)