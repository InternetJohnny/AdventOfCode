
def main():
    nice_words = 0
    with open('input.txt') as f:
        for line in f:
            repeat_letter = False
            repeat_sequence = False
            gone = ''
            subsequence = []
            temp_subsequence = ''
            char_1 = line[0]
            for char_2 in line[1:]:
                if gone == char_2:
                    repeat_letter = True
                if repeat_sequence or char_1+char_2 in subsequence:
                    repeat_sequence = True
                else:
                    subsequence.append(temp_subsequence)
                    temp_subsequence = char_1+char_2
                gone = char_1
                char_1 = char_2
            if repeat_letter and repeat_sequence:
                nice_words += 1
    print("Nice words = " + str(nice_words))


if __name__ == "__main__":
    main()
