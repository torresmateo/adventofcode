import math

def get_digits(n):
    digits = []
    if n == 0: return [0]
    while n > 0:
        digits.append(n%10)
        n //= 10
    return digits[::-1]

def recipes_string(recipes, elves):
    string = ""
    for i, r in enumerate(recipes):
        string += '(' if i == elves[0] else ' '
        string += '[' if i == elves[1] else ' '
        string += str(r)
        string += ']' if i == elves[1] else ' '
        string += ')' if i == elves[0] else ' '
        string += ' '
    return string

# part 1
n = int(input('enter input for part 1:\n'))
elves = [0,1] # index of the recipe per elve
recipes = [3,7] # score of the recipe
n_10 = n+10
for i in range(n_10):
    # compute new recipe 
    recipe = recipes[elves[0]] + recipes[elves[1]]
    # break the recipe into digits
    recipes.extend(get_digits(recipe))
    # move the elves indices
    elves[0] = (elves[0]+recipes[elves[0]]+1) % len(recipes)
    elves[1] = (elves[1]+recipes[elves[1]]+1) % len(recipes)
    #print(recipes_string(recipes, elves))
print(''.join(map(str,recipes[n:n+10])))

# part 2
n = int(input('enter input for part 2:\n'))
nlist = get_digits(n)
print(nlist)
elves = [0,1] # index of the recipe per elve
recipes = [3,7] # score of the recipe
r = ''.join(map(str,recipes))
while True:
    # compute new recipe 
    recipe = recipes[elves[0]] + recipes[elves[1]]
    # break the recipe into digits
    recipes.extend(get_digits(recipe))
    # move the elves indices
    elves[0] = (elves[0]+recipes[elves[0]]+1) % len(recipes)
    elves[1] = (elves[1]+recipes[elves[1]]+1) % len(recipes)
    if nlist == recipes[-len(nlist):] or nlist == recipes[-len(nlist)-1:-1]:
        break
print(''.join(map(str, recipes)).index(str(n)))