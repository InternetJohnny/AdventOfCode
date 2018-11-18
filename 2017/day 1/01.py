with open('input.txt') as f:
	data = f.read().strip()
captcha, i = 0, 0
while i < len(data):
	# if data[i] == data[(i+1)%len(data)]:
	if data[i] == data[(i + int(len(data)/2)) % len(data)]:
		captcha += int(data[i])
	i += 1
print(captcha)
