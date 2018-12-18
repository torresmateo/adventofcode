import itertools
import sys
sys.setrecursionlimit(10000)


def print_structure(s, colour=True):
    for e, i in enumerate(s):
        if colour:
            print(f'{e:4} -',''.join(i).replace('.',' ').replace('~','\033[44m \033[0m').replace('|','\033[34m|\033[0m'))
        else:
            print(f'{e:4} -',''.join(i))


def expand_list(l):
    if len(l) > 1:
        return list(range(l[0], l[1] + 1))
    return l

def build_structure(s):
    min_x = min(min(x) for x in s['x'])
    max_x = max(max(x) for x in s['x'])
    min_y = min(min(y) for y in s['y'])
    max_y = max(max(y) for y in s['y'])
    m = [[]]*(max_y-min_y+1)
    for i in range(len(m)):
        m[i]=['.']*(max_x - min_x + 10)
    for i in range(len(s['x'])):
        
        for x, y in itertools.product(expand_list(s['x'][i]),expand_list(s['y'][i])):
            x = x-min_x+5
            y = y-min_y
            m[y][x]='#'
    return m, min_x, min_y

def count_water(s):
    sw = 0
    rw = 0
    for r in s:
        for c in r:
            rw += 1 if c == '|' else 0
            sw += 1 if c == '~' else 0
    return rw, sw, rw+sw   

def flow(a, y, x, debug=False):
    if debug:
        print(y, x)
        print_structure(a)
        print('\n\n--------\n\n')

    if a[y][x] == '.':
        a[y][x]='|'
        expand = a[y+1][x] != '|'
        try:
            if a[y+1][x] == '.':
                #print('down')
                expand = flow(a, y+1, x, debug=debug) # down
                if expand:
                    flow(a, y+1, x, debug=debug) # down
            if expand and a[y+1][x] in '~#':
                l = a[y][x-1] != '|'
                r = a[y][x+1] != '|'
                if a[y][x+1] == '.':
                    expand = flow(a, y, x+1, debug=debug) # right
                if a[y][x-1] == '.' and x > 0:
                    #print('left')
                    expand &= flow(a, y, x-1, debug=debug) # left
                expand &= (l or r)
                
            return expand
    
        except IndexError:
            return False
    elif a[y][x] == '|':
        a[y][x]='~'
        try:
            if a[y][x+1] == '|':
                flow(a, y, x+1, debug=debug) # right
            if a[y][x-1] == '|' and x > 0:
                #print('left')
                flow(a, y, x-1, debug=debug) # left
    
        except IndexError:
            pass


structure = {'x':[], 'y':[]}
for line in open('day17.input'):
    parts = line.strip().split(', ')
    for p in parts:
        var, val = p.split('=')
        structure[var].append(list(map(int,val.split('..'))))

a, mx, my = build_structure(structure)
y, x = 0,505-mx #fountain
flow(a, y, x, debug=False)
rw, sw, total = count_water(a)
print(f'running water: {rw}, stable water: {sw}, total: {total}')
print_structure(a, colour=False)