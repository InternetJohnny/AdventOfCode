def parse_line(string):
    extra = 2
    char_1 = string[0]
    i = 1
    while i < len(string):
        char_2 = string[i]
        if char_1 == '\\':
            if char_2 == '\\' or char_2 == '"':
                extra += 1
                i += 1
            if char_2 == 'x':
                extra += 3
                i += 3
            char_1 = string[i]
        else:
            char_1 = char_2
        i += 1
    return extra


with open('input.txt') as f:
    lines = f.readlines()
counter = 0
for line in lines:
    line = line[1:-1]
    counter += parse_line(line)
print("Number of extraneous characters is " + str(counter))
