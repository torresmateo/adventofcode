import collections
import itertools
Patch = collections.namedtuple('Patch', ['id', 'l', 't', 'w', 'h'])
patches = []
for line in open('day3.input'):
    parts = line.strip().split()
    i = parts[0][1:]
    l, t = list(map(int, parts[2].split(':')[0].split(',')))
    w, h = list(map(int, parts[3].split('x')))
    patches.append(Patch(i, l, t, w, h))
patches = sorted(patches, key=lambda p: (p.t, p.l))

overlap = set()
overlap_ids = set()
for p1, p2 in itertools.combinations(patches, 2):
    if p1.l < p2.l:
        if p2.l <= p1.l + p1.w and p2.t <= p1.t + p1.h:
            for i in range(p2.l, min(p1.l + p1.w, p2.l + p2.w)):
                for j in range(p2.t, min(p1.t + p1.h, p2.t + p2.h)):
                    overlap.add((i,j))
                    overlap_ids.add(p1.id)
                    overlap_ids.add(p2.id)
    else:
        if p1.l <= p2.l + p2.w and p2.t <= p1.t + p1.h:
            for i in range(p1.l, min(p1.l + p1.w, p2.l + p2.w)):
                for j in range(p2.t, min(p1.t + p1.h, p2.t + p2.h)):
                    overlap.add((i,j))
                    overlap_ids.add(p1.id)
                    overlap_ids.add(p2.id)
all_ids = set([p.id for p in patches])
all_ids - overlap_ids

print(f'part1: {len(overlap)}, part2: {all_ids - overlap_ids}')