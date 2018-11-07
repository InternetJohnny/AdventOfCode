with open('input.txt') as f:
	moves = f.read().strip().splitlines()
password, position = '', [1, 1]
keypad = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
move = {
	'U': lambda x, y: [0, y] if x == 0 else [x-1, y],
	'D': lambda x, y: [2, y] if x == 2 else [x+1, y],
	'L': lambda x, y: [x, 0] if y == 0 else [x, y-1],
	'R': lambda x, y: [x, 2] if y == 2 else [x, y+1]
}
for line in moves:
	for c in line:
		position = move[c](position[0], position[1])
	password += str(keypad[position[0]][position[1]])
print("Bathroom password is " + str(password))
