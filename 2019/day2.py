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

def halt():
    print('halt')

OPERATIONS = {
    1: addr, 
    2: mulr, 
    99: halt
}

# part 1
total_fuel = 0

def reset_program(a, b):
    program = [int(i) for i in open('day2.input').read().strip().split(',')]
    program[1] = a
    program[2] = b
    ptr = 0
    return ptr, program

ptr, p = reset_program(12, 2)
while p[ptr] != 99:
    op, a, b, c = p[ptr:ptr+4]
    p = OPERATIONS[op](a,b,c, p)
    ptr += 4

print('part 1:', p[0])

for i in range(100):
    for j in range(100):
        ptr, p = reset_program(i, j)
        #print(i, j, p[0])
        while p[ptr] != 99:
            op, a, b, c = p[ptr:ptr+4]
            p = OPERATIONS[op](a,b,c, p)
            ptr += 4
        if p[0] == 19690720:
            print('part 2:', i, j, 100 * i + j)
            break
#requirements = []
