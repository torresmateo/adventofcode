import math

def compute_fuel(n):
    total_requirement = required_fuel = math.floor(n/3) - 2
    while required_fuel > 0:
        required_fuel = math.floor(required_fuel/3) - 2
        total_requirement += max(0,required_fuel)
    return total_requirement
# part 1
total_fuel = 0
#requirements = []
inputfile=open('day1.input')
for line in inputfile:
    #requirements.append(math.floor(int(line.strip())/3)
    total_fuel += math.floor(int(line.strip())/3) - 2
print('part 1:', total_fuel)
inputfile.close()
# part 2
total_fuel = 0
inputfile=open('day1.input')
for line in inputfile:
    #requirements.append(math.floor(int(line.strip())/3)
    total_fuel += compute_fuel(int(line.strip()))
print('part 2:', total_fuel)
inputfile.close()
