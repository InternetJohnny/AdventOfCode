def parse_line(string):
    extra, i = 0, 0
    while i < len(string):
        char = string[i]
        if char == '\\' or char == '"':
            extra += 1
        i += 1
    return extra+2  # Adds 2 for the quotation marks


with open('input.txt') as f:
    lines = f.read().strip().splitlines()
counter = 0
for line in lines:
    counter += parse_line(line)
print("Number of extraneous characters is " + str(counter))
