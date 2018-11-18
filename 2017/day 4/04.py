def is_valid(line):
	passphrase = line.split()
	if len(passphrase) < 2:
		return 0
	i = 0
	while i < len(passphrase) - 1:
		j = i + 1
		while j < len(passphrase):
			# if passphrase[i] == passphrase[j]:
			if sorted(passphrase[i]) == sorted(passphrase[j]):
				return 0
			j += 1
		i += 1
	return 1

with open('input.txt') as f:
	data = f.readlines()
counter = 0
for l in data:
	counter += is_valid(l)
print(counter)