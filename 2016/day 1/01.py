def check_repeat(path, curr_line):
    for p in path:
        if p.static == curr_line.static:
            continue
        elif p.static == 'x':
            if p.a[1] >= curr_line.a[1] >= p.b[1] or \
                    p.a[1] <= curr_line.a[1] <= p.b[1]:
                return [p.a[0], curr_line.a[1]]
        elif p.static == 'y':
            if p.a[0] >= curr_line.a[0] >= p.b[0] or \
                    p.a[0] <= curr_line.a[0] <= p.b[0]:
                return [p.a[1], curr_line.a[0]]


class Line:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.static = 'x' if self.a[0] == self.b[0] else 'y'

    def move(self, point):
        self.a = self.b
        self.b = point
        self.static = 'x' if self.a[0] == self.b[0] else 'y'


with open('input.txt') as f:
    moves = f.read().split(', ')
compass = 0
curr_path = Line([0, 0], [0, 0])
position = [0, 0]
path = []
path_repeats = False
intersect = []
move = {
    0: lambda d: [0, d],
    1: lambda d: [d, 0],
    2: lambda d: [0, -d],
    3: lambda d: [-d, 0]
}
for i in moves:
    compass = (compass+1) % 4 if i[0] == 'R' else (compass+3) % 4
    position = [sum(x) for x in zip(position, move[compass](int(i[1:])))]
    curr_path.move(position)
    path.append(curr_path)
    if not path_repeats:
        intersect = check_repeat(path, curr_path)
        if intersect:
            path_repeats = True
distance = abs(position[0]) + abs(position[1])
distance_intersect = abs(intersect[0]) + abs(intersect[1])
print("Destination is " + str(distance) + " blocks away")
print("Distance from intersect is " + str(distance_intersect))
