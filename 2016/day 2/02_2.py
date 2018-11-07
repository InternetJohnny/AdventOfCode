with open('input.txt') as f:
	moves = f.read().strip().splitlines()
password, position = '', [2, 0]
keypad = [  ['', '', '1', '', ''],
			['', '2', '3', '4', ''],
			['5', '6', '7', '8', '9'],
			['', 'A', 'B', 'C', ''],
			['', '', 'D', '', '']]
move = {
	'U': lambda x, y: [x, y] if keypad[x][y] == '1' or keypad[x-1][y] == '' else [x-1, y],
	'D': lambda x, y: [x, y] if keypad[x][y] == 'D' or keypad[x+1][y] == '' else [x+1, y],
	'L': lambda x, y: [x, y] if keypad[x][y] == '5' or keypad[x][y-1] == '' else [x, y-1],
	'R': lambda x, y: [x, y] if keypad[x][y] == '9' or keypad[x][y+1] == '' else [x, y+1]
}
for line in moves:
	for c in line:
		position = move[c](position[0], position[1])
	password += str(keypad[position[0]][position[1]])
print("Bathroom password is " + str(password))
