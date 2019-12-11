from itertools import permutations

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

def save_input(a, i, regs, modes=[0]):
    r = regs.copy()
    r[a] = i
    return r
    
def save(a,regs, modes=[0]):
    r = regs.copy()
    r[a] = int(input())
    return r


DAOUT = None
def output_g(a, regs, modes=[0]):
    global DAOUT
    DAOUT = regs[a]
    return regs


def output(a, regs, modes=[0]):
    print(regs[a])
    return regs
    
JUMP_LOC = None
def jump_if_true(a,b,regs, modes=[0,0]):
    global JUMP_LOC
    r = regs.copy()
    if modes[0] == 0:
        a = r[a]
    if modes[1] == 0:
        b = r[b]
    JUMP_LOC = b-3 if a != 0 else JUMP_LOC
    return r

def jump_if_false(a,b,regs, modes=[0,0]):
    global JUMP_LOC
    r = regs.copy()
    if modes[0] == 0:
        a = r[a]
    if modes[1] == 0:
        b = r[b]
    JUMP_LOC = b-3 if a == 0 else JUMP_LOC
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


def halt(regs, modes=[0,0,0]):
    pass

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
    program = [int(i) for i in open('day7.input').read().strip().split(',')]
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



max_seq = None
curr_max = -1
for inputs in permutations(range(5)):
    signal = 0
    input_count = 0
    for i in inputs:
        ptr, p = reset_program()
        while p[ptr] != 99:
            op, modes = parse_opcode(p[ptr])
            params = p[ptr+1:ptr+OPERATIONS[op]['next_instr']]
            JUMP_LOC = ptr
            if op == 3:
                if input_count%2 == 0:
                    p = save_input(*params, i, p,modes)
                else:
                    p = save_input(*params, signal, p,modes)
                input_count += 1
            elif op == 4:
                p = output_g(*params, p, modes)
            else:
                p = OPERATIONS[op]['func'](*params,p,modes)
            if op in [5,6]:
                ptr = JUMP_LOC
            ptr += OPERATIONS[op]['next_instr']
        signal = DAOUT
    if signal > curr_max:
        curr_max = signal
        max_seq = inputs

print('part 1:', curr_max, max_seq)



max_seq = None
curr_max = -1

programs = {}
for inputs in permutations(range(5,10)):
    signal = 0
    for machine in range(5):
        ptr, p = reset_program()
        programs[machine] = {'ptr':ptr, 'p':p, 'init':False}
    DAOUTE = None
    DAOUT = 0
    curr_machine = 0
    while programs[4]['p'][programs[4]['ptr']] != 99:
        #print('>\t', programs[curr_machine]['p'])
        p = programs[curr_machine]['p']
        ptr = programs[curr_machine]['ptr']
        JUMP_LOC = ptr
        op, modes = parse_opcode(p[ptr])
        params = p[ptr+1:ptr+OPERATIONS[op]['next_instr']]
        if op == 3:
            if programs[curr_machine]['init']:
                p = save_input(*params, signal, p,modes)
            else:
                p = save_input(*params, inputs[curr_machine], p,modes)
                programs[curr_machine]['init'] = True
        elif op == 4:
            p = output_g(*params, p, modes)
            if curr_machine == 4:
                DAOUTE = DAOUT
        else:
            p = OPERATIONS[op]['func'](*params,p,modes)
        
        if op in [5,6]:
            ptr = JUMP_LOC
        if op != 99:
            programs[curr_machine]['ptr'] = ptr + OPERATIONS[op]['next_instr']
            programs[curr_machine]['p'] = p
                
        #print('<\t',programs[curr_machine]['p'])
        if op in [4,99]:
            next_machine = (curr_machine + 1)%5
            if programs[next_machine]['p'][programs[next_machine]['ptr']] != 99:
                curr_machine = next_machine
        signal = DAOUT
    if DAOUTE > curr_max:
        curr_max = DAOUTE
        max_seq = inputs

print('part 2:', curr_max, max_seq)