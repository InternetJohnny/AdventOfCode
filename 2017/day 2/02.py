import sys

def div_nums(l):
	i = 0
	while i < len(l) - 1:
		j = i + 1
		while j < len(l):
			if l[i] % l[j] == 0:
				return l[i] / l[j]
			elif l[j] % l[i] == 0:
				return l[j] / l[i]
			j += 1
		i += 1
	print("didnt find dividers")

def p1(d):
	checksum = 0
	for line in d:
		large, small = -sys.maxsize - 1, sys.maxsize
		for n in line.split():
			i = int(n)
			if i > large:
				large = i
			if i < small:
				small = i
		checksum += large - small
	print(checksum)

def p2(d):
	sum = 0
	for line in d:
		num_list = []
		for n in line.split():
			num_list.append(int(n))
		sum += div_nums(num_list)
	print(sum)

with open('input.txt') as f:
	data = f.readlines()
p1(data)
p2(data)
