
def main():
    nice_words = 0
    with open('input.txt') as f:
        for line in f:
            vowels = 0
            repeat_letter = False
            conseq_letters = False
            char_1 = line[0]
            for char_2 in line[1:]:
                if is_conseq(char_1, char_2):
                    conseq_letters = True
                    break
                if is_vowel(char_1):
                    vowels += 1
                if char_1 == char_2:
                    repeat_letter = True
                char_1 = char_2
            if not conseq_letters and repeat_letter and vowels > 2:
                nice_words += 1
    print("Nice words = " + str(nice_words))


def is_vowel(char):
    if char in ['a', 'e', 'i', 'o', 'u']:
        return True
    return False


def is_conseq(char_1, char_2):
    if char_1+char_2 in ['ab', 'cd', 'pq', 'xy']:
        return True
    return False


if __name__ == "__main__":
    main()
