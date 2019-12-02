# part 1
ids = []
vocabs = []
for line in open('day2.input'):
	ids.append(line.strip())
	vocabs.append(list(set(ids[-1])))

repeats2 = 0
repeats3 = 0
for i in range(len(ids)):
	r2 = False
	r3 = False
	for c in vocabs[i]:
		count = ids[i].count(c)
		if count == 2:
			r2 = True
		if count == 3:
			r3 = True
	repeats2 += 1 if r2 else 0
	repeats3 += 1 if r3 else 0
print(repeats2 * repeats3)

# part 2
import itertools
import difflib

for id1, id2 in itertools.combinations(ids, 2):
	if len(id1) != len(id2):
		continue
	diff = 0
	idx = []
	for i, s in enumerate(difflib.ndiff(id1, id2)):
		if s[0] == '-':
			diff += 1
			idx.append(i)

	if diff == 1: # we've found the matching ids:
		print('marthing ids: \n')
		print(id1, ' -> ', id2, diff, idx) 
		print('common characters')
		print(id1[0:idx[0]]+id1[idx[0]+1:])
	
	#for a in diff:
	#	print(a, end=' | ')
	#input()
	#for i in range(len(id1)):
