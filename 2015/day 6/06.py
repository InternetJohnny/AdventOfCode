
def main():
    with open('input.txt') as f:
        input = f.readlines()
    size = 1000
    lights = [[0 for x in range(size)] for y in range(size)]
    for line in input:
        command = line.split()
        execute(command, lights)
    counter = count_lights(lights)
    print("There are " + str(counter) + " ligths on.")


def execute(command, lights):
    if command[0] == 'turn':
        x1, y1 = get_coords(command[2].split(','))
        x2, y2 = get_coords(command[4].split(','))
        if command[1] == 'on':
            switch_val(x1, y1, x2, y2, lights, 1)
        elif command[1] == 'off':
            switch_val(x1, y1, x2, y2, lights, 0)
    elif command[0] == 'toggle':
        x1, y1 = get_coords(command[1].split(','))
        x2, y2 = get_coords(command[3].split(','))
        toggle(x1, y1, x2, y2, lights)


def get_coords(coords):
    x, y = int(coords[0]), int(coords[1])
    return x, y


def switch_val(x1, y1, x2, y2, lights, val):
    for x in range(x1, x2+1):
        for y in range(y1, y2+1):
            # lights[x][y] += val
            lights[x][y] = lights[x][y]+1 if val == 1 else lights[x][y]-1
            if lights[x][y] < 0:
                lights[x][y] = 0


def toggle(x1, y1, x2, y2, lights):
    for x in range(x1, x2+1):
        for y in range(y1, y2+1):
            # lights[x][y] = 1 if lights[x][y] == 0 else 0
            lights[x][y] += 2


def count_lights(lights):
    counter = 0
    for x in range(1000):
        for y in range(1000):
            counter += lights[x][y]
    return counter


if __name__ == "__main__":
    main()