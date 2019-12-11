
from itertools import permutations
from collections import defaultdict
import numpy as np
import matplotlib.pyplot as plt


class Painter(object):

    def __init__(self, filename):
        self.ptr = 0 
        self.relative_base = 0
        self.p = defaultdict(int)
        for e, i in enumerate(open(filename).read().strip().split(',')):
            self.p[e] = int(i)

        self.OPERATIONS = {
            1: {'func':self.add, 'next_instr':4, 'def_mode':[0,0,0]},
            2: {'func':self.mul, 'next_instr':4, 'def_mode':[0,0,0]},
            3: {'func':self.save_map_colour, 'next_instr':2, 'def_mode':[0]},
            4: {'func':self.output_g, 'next_instr':2, 'def_mode':[0]},
            5: {'func':self.jump_if_true, 'next_instr':3, 'def_mode':[0,0]},
            6: {'func':self.jump_if_false, 'next_instr':3, 'def_mode':[0,0]},
            7: {'func':self.less_than, 'next_instr':4, 'def_mode':[0,0,0]},
            8: {'func':self.equals, 'next_instr':4, 'def_mode':[0,0,0]},
            9: {'func':self.adjust_rb, 'next_instr':2, 'def_mode':[0]},
            99:{'func':self.halt, 'next_instr':1, 'def_mode':[0]},
        }

        self.turns = {'u':(0, 1), 'r': (1, 0), 'l': (-1, 0), 'd': (0, -1)}
        self.orientation = 'u'
        self.halted = False
        self.map = defaultdict(int)
        self.coord = (0,0)
        #self.map[self.coord] = 1

    def turn(self, direction):
        if self.orientation == 'u':
            return 'r' if direction == 1 else 'l'
        if self.orientation == 'd':
            return 'l' if direction == 1 else 'r'
        if self.orientation == 'l':
            return 'u' if direction == 1 else 'd'
        if self.orientation == 'r':
            return 'd' if direction == 1 else 'u'

    def paint(self):
        op, modes = self.parse_opcode(self.p[self.ptr])
        colour = None
        direction = None
        count = 0
        while op != 99:
            count += 1
            colour = self.run()
            direction = self.run()
            if not self.halted:
                self.map[self.coord] = colour
                self.orientation = self.turn(direction)
                s = self.turns[self.orientation]
                self.coord = (self.coord[0] + s[0], self.coord[1] + s[1])
                op, modes = self.parse_opcode(self.p[self.ptr])
            else:
                break
            if count > 10:
                pass
        print(f'part 1: {len(self.map.keys())}')        

    def run(self):
        r = None
        while r is None and not self.halted:
            op, modes = self.parse_opcode(self.p[self.ptr])
            params = [self.p[i] for i in range(self.ptr +1,self.ptr+self.OPERATIONS[op]['next_instr'])]
            r = self.OPERATIONS[op]['func'](*params,modes)
            self.ptr += self.OPERATIONS[op]['next_instr']
        return r

    def get_param(self, value, mode):
        if mode == 0:
            return self.p[value]
        if mode == 1:
            return value
        if mode == 2:
            return self.p[value + self.relative_base]

    def get_addr(self, value, mode):
        if mode == 2:
            return value + self.relative_base
        return value

    def add(self, a, b, c, modes=[0,0]):
        a = self.get_param(a, modes[0])
        b = self.get_param(b, modes[1])
        c = self.get_addr(c, modes[2])
        self.p[c] = a + b

    def mul(self, a, b, c, modes=[0,0]):
        a = self.get_param(a, modes[0])
        b = self.get_param(b, modes[1])
        c = self.get_addr(c, modes[2])
        self.p[c] = a * b

    def save_map_colour(self, a, modes=[0]):
        a = self.get_addr(a, modes[0])
        self.p[a] = self.map[self.coord]

    def save_input(self, a, i, modes=[0]):
        a = self.get_addr(a, modes[0])
        self.p[a] = i
        
    def save(self, a, modes=[0]):
        a = self.get_addr(a, modes[0])
        self.p[a] = int(input('INPUT:'))

    def output_g(self, a, modes=[0]):
        a = self.get_param(a, modes[0])
        return a

    def output(self, a, modes=[0]):
        a = self.get_param(a, modes[0])
        print(f'OUTPUT: {a}')
        
    def jump_if_true(self, a, b, modes=[0,0]):
        a = self.get_param(a, modes[0])
        b = self.get_param(b, modes[1])
        self.ptr = b-3 if a != 0 else self.ptr

    def jump_if_false(self, a, b, modes=[0,0]):
        a = self.get_param(a, modes[0])
        b = self.get_param(b, modes[1])
        self.ptr = b-3 if a == 0 else self.ptr

    def less_than(self, a, b, c, modes=[0,0,0]):
        a = self.get_param(a, modes[0])
        b = self.get_param(b, modes[1])
        c = self.get_addr(c, modes[2])
        self.p[c] = 1 if a < b else 0

    def equals(self, a, b, c, modes=[0,0,0]):
        a = self.get_param(a, modes[0])
        b = self.get_param(b, modes[1])
        c = self.get_addr(c, modes[2])
        self.p[c] = 1 if a == b else 0   

    def adjust_rb(self, a, modes=[0]):
        a = self.get_param(a, modes[0])
        self.relative_base += a

    def halt(self, modes=[0,0,0]):
        self.halted = True

    def parse_opcode(self, op):
        code = int(str(op)[-2:])
        modes = [int(i) for i in str(op)[:-2]]
        if len(modes) == 0:
            modes = self.OPERATIONS[code]['def_mode'].copy()
        while len(modes) < len(self.OPERATIONS[code]['def_mode']):
            modes.insert(0,0)
        modes.reverse()
        return code, modes


P = Painter('day11.input')
P.paint()

P = Painter('day11.input')
P.map[P.coord] = 1
P.paint()

x_max = max(i[0] for i in P.map.keys()) + 1
x_min = min(i[0] for i in P.map.keys())
y_max = max(i[1] for i in P.map.keys()) +1
y_min = min(i[1] for i in P.map.keys())

m = np.zeros((y_max - y_min, x_max - x_min))
for (i,j), col in P.map.items():
    m[y_max-1 - j, i-x_min] = col
plt.spy(m)

plt.show()