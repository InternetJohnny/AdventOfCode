def large_index(block):
	large, index, i = 0, 0, 0
	while i < len(block):
		if block[i] > large:
			large = block[i]
			index = i
		i += 1
	return index

def shuffle(block, index):
	mem = block[index]
	block[index] = 0
	while mem > 0:
		index += 1
		block[index % len(block)] += 1
		mem -= 1
	return block

def cycles(block):
	counter, conf = 0, []
	conf.append(str(block))
	while True:
		i = large_index(block)
		block = shuffle(block, i)
		counter += 1
		for i in range(0, len(conf)):
			if conf[i] == str(block):
				print(counter)
				print(counter - i)
				return
		conf.append(str(block))

with open('input.txt') as f:
	data = f.read().split()

membank = []
for num in data:
	membank.append(int(num))
cycles(membank)


