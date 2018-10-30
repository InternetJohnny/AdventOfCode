import numpy


def main():
    dimension = 1000
    houses = numpy.zeros((dimension, dimension))
    counter = 1
    dim_x, dim_y, start = 2, 2, int(dimension/2);
    coordinates = [[start for i in range(dim_x)] for j in range(dim_y)]
    robot_santa = False
    houses[start][start] += 2
    with open('input.txt') as f:
        for char in f.read():
            counter += move_santa(char, robot_santa, coordinates, houses)
            # Comment next line for answer without Robot-Santa
            robot_santa = not robot_santa
    print(str(counter) + " houses received at least one present")


def move_santa(char, robot_santa, coords, houses):
    i = 0
    add = 0
    if robot_santa is True:
        i += 1
    if char is ">":
        coords[i][0] += 1
    elif char is "<":
        coords[i][0] -= 1
    elif char is "^":
        coords[i][1] += 1
    elif char is "v":
        coords[i][1] -= 1
    x, y = coords[i][0], coords[i][1]
    if houses[x][y] == 0:
        add = 1
    houses[x][y] += 1
    return add


if __name__ == "__main__":
    main()
