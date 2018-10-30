
def main():
    paper = 0
    ribbon = 0
    sides = [0, 0, 0]
    with open('input.txt') as f:
        for line in f:
            print(line)
            i = 0
            largest = 0
            for dimension in line.rstrip().split("x"):
                sides[i] = int(dimension)
                if sides[i] > largest:
                    largest = sides[i]
                i += 1
            paper += calc_paper(sides, largest)
            ribbon += calc_ribbon(sides, largest)
    print("Total area of wrapping paper to order = " + str(int(paper)))
    print("Total length of ribbon to order = " + str(int(ribbon)))


def calc_paper(sides, largest):
    area = 0
    area += sides[0] * sides[1] * 2
    area += sides[1] * sides[2] * 2
    area += sides[0] * sides[2] * 2
    area += sides[0] * sides[1] * sides[2] / largest
    return area


def calc_ribbon(sides, largest):
    area = 0
    area += sides[0] * 2
    area += sides[1] * 2
    area += sides[2] * 2
    area -= largest * 2     # remove the largest side
    area += sides[0] * sides[1] * sides[2]
    return area


if __name__ == "__main__":
    main()
