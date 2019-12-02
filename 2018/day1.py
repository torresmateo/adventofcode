# part 1
frequency = 0
changes = []
inputfile=open('day1.input')
for line in inputfile:
	changes.append(int(line.strip()))
	frequency += int(line.strip())
print(frequency)
inputfile.close()
# part 2
frequency = 0
reached_frequencies = {0}
repeat_found = False
repeated = None
while not repeat_found:
	for change in changes:
		frequency += change
		if frequency in reached_frequencies:
			repeat_found = True
			repeated = frequency
			break
		reached_frequencies.add(frequency)
print(repeated)
