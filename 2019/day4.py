from collections import defaultdict
passrange = [387638,919123]

valid_options= []

countp1 = 0
countp2 = 0
for i in range(passrange[0], passrange[1] + 1):
    number = '0' + str(i)
    has_double = False
    not_valid = False
    c = defaultdict(int)
    for j in range(1,len(number)):
        if int(number[j]) < int(number[j-1]):
            not_valid = True
        c[number[j]] += 1
        if int(number[j]) == int(number[j-1]):
            has_double = True
    if has_double and not not_valid:
        countp1 += 1
    if has_double and not not_valid and 2 in c.values():
        countp2 += 1

print('part 1', countp1)
print('part 2', countp2)

