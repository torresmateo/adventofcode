def addr(a,b,c,regs):
    r = regs.copy()
    r[c] = r[a] + r[b]
    return r
    
def addi(a,b,c,regs):
    r = regs.copy()
    r[c] = r[a] + b
    return r

def mulr(a,b,c,regs):
    r = regs.copy()
    r[c] = r[a] * r[b]
    return r
    
def muli(a,b,c,regs):
    r = regs.copy()
    r[c] = r[a] * b
    return r
    
def banr(a,b,c,regs):
    r = regs.copy()
    r[c] = r[a] & r[b]
    return r

def bani(a,b,c,regs):
    r = regs.copy()
    r[c] = r[a] & b
    return r

def borr(a,b,c,regs):
    r = regs.copy()
    r[c] = r[a] | r[b]
    return r

def bori(a,b,c,regs):
    r = regs.copy()
    r[c] = r[a] | b
    return r

def setr(a,b,c,regs):
    r = regs.copy()
    r[c] = r[a]
    return r

def seti(a,b,c,regs):
    r = regs.copy()
    r[c] = a
    return r

def gtir(a,b,c,regs):
    r = regs.copy()
    r[c] = 1 if a > r[b] else 0
    return r

def gtri(a,b,c,regs):
    r = regs.copy()
    r[c] = 1 if r[a] > b else 0
    return r

def gtrr(a,b,c,regs):
    r = regs.copy()
    r[c] = 1 if r[a] > r[b] else 0
    return r

def eqir(a,b,c,regs):
    r = regs.copy()
    r[c] = 1 if a == r[b] else 0
    return r

def eqri(a,b,c,regs):
    r = regs.copy()
    r[c] = 1 if r[a] == b else 0
    return r

def eqrr(a,b,c,regs):
    r = regs.copy()
    r[c] = 1 if r[a] == r[b] else 0
    return r

OPERATIONS = [
    addr, addi,
    mulr, muli,
    banr, bani,
    borr, bori,
    setr, seti,
    gtir, gtri, gtrr,
    eqir, eqri, eqrr
]

tests,program = open('day16.input').read().strip().split('\n\n\n')
tests = tests.strip().split('\n')
program = program.strip().split('\n')

matches3 = 0
for i in range(0,len(tests), 4): # 4 lines per test case
    if tests[i].startswith('Before:'):
        before = list(map(int, tests[i].strip().split(":")[-1].split('[')[-1].split(']')[0].split(',')))
        params = list(map(int, tests[i+1].strip().split()[1:]))
        after = list(map(int, tests[i+2].strip().split(":")[-1].split('[')[-1].split(']')[0].split(',')))
        matches = 0
        for op in OPERATIONS:
            if op(*params, before) == after:
                matches += 1
        if matches >= 3:
            matches3 += 1
print(f'part1: {matches3}')

opcodes = {i:[] for i in range(len(OPERATIONS))}
for i in range(0,len(tests), 4): # 4 lines per test case
    if tests[i].startswith('Before:'):
        before = list(map(int, tests[i].strip().split(":")[-1].split('[')[-1].split(']')[0].split(',')))
        params = list(map(int, tests[i+1].strip().split()))
        opcode, params = params[0], params[1:]
        after = list(map(int, tests[i+2].strip().split(":")[-1].split('[')[-1].split(']')[0].split(',')))
        matches = 0
        ops = set()
        for op in OPERATIONS:
            if op(*params, before) == after:
                ops.add(op)
        opcodes[opcode].append(ops)

intersections = {i: set.intersection(*opcodes[i]) for i in opcodes.keys()}
while max([len(i) for i in intersections.values()]) != 1:
    for j in intersections.keys():
        if len(intersections[j]) == 1:
            for k in intersections.keys():
                if k != j:
                    intersections[k] -= intersections[j]
for i in opcodes.keys():
    opcodes[i] = list(intersections[i])[0]

registers = [0,0,0,0]
for line in program:
    line = list(map(int, line.split()))
    op, params = line[0], line[1:]
    registers = opcodes[op](*params, registers)

print(f'part2: {registers[0]}')