from itertools import permutations

from collections import defaultdict


class Intcode(object):

    def __init__(self, filename):
        self.ptr = 0 
        self.relative_base = 0
        self.p = defaultdict(int)
        for e, i in enumerate(open(filename).read().strip().split(',')):
            self.p[e] = int(i)

        self.OPERATIONS = {
            1: {'func':self.add, 'next_instr':4, 'def_mode':[0,0,0]},
            2: {'func':self.mul, 'next_instr':4, 'def_mode':[0,0,0]},
            3: {'func':self.save, 'next_instr':2, 'def_mode':[0]},
            4: {'func':self.output, 'next_instr':2, 'def_mode':[0]},
            5: {'func':self.jump_if_true, 'next_instr':3, 'def_mode':[0,0]},
            6: {'func':self.jump_if_false, 'next_instr':3, 'def_mode':[0,0]},
            7: {'func':self.less_than, 'next_instr':4, 'def_mode':[0,0,0]},
            8: {'func':self.equals, 'next_instr':4, 'def_mode':[0,0,0]},
            9: {'func':self.adjust_rb, 'next_instr':2, 'def_mode':[0]},
            99:{'func':self.halt, 'next_instr':1, 'def_mode':[0]},
        }
        self.halted = False

    def run(self):
        r = None
        while r is None:
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
        return True

    def parse_opcode(self, op):
        code = int(str(op)[-2:])
        modes = [int(i) for i in str(op)[:-2]]
        if len(modes) == 0:
            modes = self.OPERATIONS[code]['def_mode'].copy()
        while len(modes) < len(self.OPERATIONS[code]['def_mode']):
            modes.insert(0,0)
        modes.reverse()
        return code, modes


P = Intcode('day9.test')
P.run()

print('=========================')
P = Intcode('day9.test2')
P.run()

print('=========================')
P = Intcode('day9.test3')
P.run()

print('=========================')
P = Intcode('day9.input')
P.run()
