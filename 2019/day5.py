def add(a,b,c,regs, modes=[0,0]):
    r = regs.copy()
    if modes[0] == 0:
        a = r[a]
    if modes[1] == 0:
        b = r[b]
    r[c] = a + b
    return r

def mul(a,b,c,regs, modes=[0,0]):
    r = regs.copy()
    if modes[0] == 0:
        a = r[a]
    if modes[1] == 0:
        b = r[b]
    r[c] = a * b
    return r
    
def save(a,regs, modes=[0]):
    r = regs.copy()
    r[c] = int(input())
    return r

def output(a, regs, modes=[0]):
    print(regs[a])
    return regs
    
def jump_if_true(a,b,regs, modes=[0,0]):
    global ptr
    r = regs.copy()
    if modes[0] == 0:
        a = r[a]
    if modes[1] == 0:
        b = r[b]
    ptr = b-3 if a != 0 else ptr
    return r

def jump_if_false(a,b,regs, modes=[0,0]):
    global ptr
    r = regs.copy()
    if modes[0] == 0:
        a = r[a]
    if modes[1] == 0:
        b = r[b]
    ptr = b-3 if a == 0 else ptr
    return r

def less_than(a,b,c, regs, modes=[0,0,0]):
    r = regs.copy()
    if modes[0] == 0:
        a = r[a]
    if modes[1] == 0:
        b = r[b]
    r[c] = 1 if a < b else 0
    return r

def equals(a,b,c, regs, modes=[0,0,0]):
    r = regs.copy()
    if modes[0] == 0:
        a = r[a]
    if modes[1] == 0:
        b = r[b]
    r[c] = 1 if a == b else 0   
    return r


def halt():
    print('halt')

OPERATIONS = {
    1: {'func':add, 'next_instr':4, 'def_mode':[0,0,0]},
    2: {'func':mul, 'next_instr':4, 'def_mode':[0,0,0]},
    3: {'func':save, 'next_instr':2, 'def_mode':[0]},
    4: {'func':output, 'next_instr':2, 'def_mode':[0]},
    5: {'func':jump_if_true, 'next_instr':3, 'def_mode':[0,0]},
    6: {'func':jump_if_false, 'next_instr':3, 'def_mode':[0,0]},
    7: {'func':less_than, 'next_instr':4, 'def_mode':[0,0,0]},
    8: {'func':equals, 'next_instr':4, 'def_mode':[0,0,0]},
    99:{'func':halt, 'next_instr':1, 'def_mode':[0]},
}

# part 1
total_fuel = 0

def reset_program():
    program = [int(i) for i in open('day5.input').read().strip().split(',')]
    #program[1] = a
    #program[2] = b
    ptr = 0
    return ptr, program

def parse_opcode(op):
    code = int(str(op)[-2:])
    modes = [int(i) for i in str(op)[:-2]]
    if len(modes) == 0:
        modes = OPERATIONS[code]['def_mode'].copy()
    while len(modes) < len(OPERATIONS[code]['def_mode']):
        modes.insert(0,0)

    modes.reverse()
    return code, modes

ptr, p = reset_program()
while p[ptr] != 99:
    op, a, b, c = p[ptr:ptr+4]
    op, modes = parse_opcode(p[ptr])
    print(op, modes)
    params = p[ptr+1:ptr+OPERATIONS[op]['next_instr']]
    p = OPERATIONS[op]['func'](*params,p,modes)
    ptr += OPERATIONS[op]['next_instr']

print('part 1:', p[0])

