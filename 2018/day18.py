import itertools

class World(object):
    
    def __init__(self, filename):
        self.map = []
        self.build_map(filename)
    
    def print_status(self, distances=None):
        for r in self.map:
            print(''.join(r).replace('.','.').replace('#','\033[35m#\033[0m').replace('|','\033[32m|\033[0m'))
        print('\n\n--------\n')
    

    def get_value(self, i, j):
        # check surroundings
        lumberyard = []
        trees = []
        empty = []
        me = ''
        for r, c in itertools.product([i-1,i, i+1], [j-1,j, j+1]):
            #print(f'{r}, {c}')
            if r >= 0 and c >= 0:
                if r == i and c == j:
                    me = self.map[r][c]
                else:
                    try:
                        if self.map[r][c] == '#':
                            lumberyard.append((r,c))
                        elif self.map[r][c] == '|':
                            trees.append((r,c))
                        elif self.map[r][c] == '.':
                            empty.append((r,c))
                    except IndexError:
                        pass
        if me == '.' and len(trees) >= 3:
            return '|'
        if me == '|' and len(lumberyard) >= 3:
            return '#'
        if me == '#':
           # print(len(lumberyard), len(trees), len(empty))
            if not(len(lumberyard) >= 1 and len(trees) >= 1):
                return '.'
        return me
    
    def compute_score(self):
        trees = 0
        lumberyards = 0
        for r in self.map:
            for v in r:
                trees += 1 if v == '|' else 0
                lumberyards += 1 if v == '#' else 0
        return trees * lumberyards
                
    
    def transition(self, debug = False):
        next_map = [[]] * len(self.map)
        for i in range(len(next_map)):
            next_map[i] = ['.'] * len(self.map[i])

        for i in range(len(self.map)):
            for j in range(len(self.map[i])):
                next_map[i][j] = self.get_value(i,j)
        self.map = next_map.copy()
        if debug:
            self.print_status()
                
    def build_map(self, filename):
        width = -1
        for line in open(filename):
            r = [c for c in line.strip()]
            self.map.append(r)

w = World('day18.input')

seen_maps = {}
scores = {}
cycle_begin = cycle_end = 0

for i in range(10000):
    scores[i] = w.compute_score()
    curr_map = ''.join(''.join(row) for row in w.map)
    if i == 9:
        print(f'part1: {scores[i]}')

    if curr_map in seen_maps:
        cycle_begin = seen_maps[curr_map]
        cycle_end = i
        break

    seen_maps[curr_map] = i
    w.transition(False)
period = cycle_end - cycle_begin
if period != 0:
    iteration = cycle_begin + (i - cycle_begin) % period
print(f'part2: {scores[iteration]}')


w.compute_score()