import math as m
import numpy as np

def p1(n):
	root = int(m.sqrt(n)) + 1
	if root % 2 == 0:
		root += 1
	square = pow(root, 2)
	pos = [int((root - 1) / 2), int((root - 1) / 2)]
	move = {
		0: lambda x, y, d: [x+d, y],
		1: lambda x, y, d: [x, y+d],
		2: lambda x, y, d: [x+d, y],
		3: lambda x, y, d: [x, y+d],
	}
	counter, i, step = 0, 0, -1
	while square > n:
		square -= 1
		pos = move[int(i)](pos[0], pos[1], step)
		counter = (counter + 1) % ((root - 1) / 2)
		if counter == 0:
			step = -step
			i += 0.5
	print(pos[0] + pos[1])

def adjacent(g, x, y):
	adj = []
	for i in range(-1, 2):
		for j in range(-1, 2):
			if g[x+i][y+j] != 0:
				adj.append(g[x+i][y+j])
	return adj

def p2(n):
	side = int(m.sqrt(n))
	pos, curr, direction = [side, side], 1, 0
	grid = np.zeros((side*2, side*2))
	grid[side][side] = 1
	move = {
		0: lambda x, y: [x+1, y],
		1: lambda x, y: [x, y-1],
		2: lambda x, y: [x-1, y],
		3: lambda x, y: [x, y+1]
	}
	while curr <= n:
		pos = move[direction](pos[0], pos[1])
		adj = adjacent(grid, pos[0], pos[1])
		curr = sum(adj)
		grid[pos[0]][pos[1]] = sum(adj)
		if len(adj) < 3:
			direction = (direction+1) % 4
	print(int(curr))

with open('input.txt') as f:
	num = int(f.read())

p1(num)
p2(num)