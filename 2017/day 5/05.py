with open('input.txt') as f:
	data = f.readlines()

ins = []
for n in data:
	ins.append(int(n))

pos, counter, step = 0, 0, 1
while pos < len(ins):
	step = -1 if ins[pos] >= 3 else 1
	ins[pos] += step
	pos += ins[pos] - step
	counter += 1
print(counter)