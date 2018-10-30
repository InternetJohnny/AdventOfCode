def main():
    floor = 0
    counter = 0
    entered_basement = False
    f = open("input.txt", "r")
    if f.mode == 'r':
        contents = f.read()
        for letter in contents:
            if letter is "(":
                floor += 1
            elif letter is ")":
                floor -= 1
            if not entered_basement:
                counter += 1
                if floor is -1:
                    entered_basement = True

        print("Santa ended up on floor #" + str(floor))
        print("Santa entered floor -1 at character #" + str(counter))


if __name__ == "__main__":
    main()
