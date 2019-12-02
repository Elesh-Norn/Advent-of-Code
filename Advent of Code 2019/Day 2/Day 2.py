def read_input():
    intcodes = []
    with open('Day_2_input', "r") as file:
        for x in file:
            s = x.split(",")
            for ints in s:
                intcodes.append(int(ints))
    return intcodes


def read_intcodes(intcodes):
    pointer = 0
    loop = True
    while loop:
        if intcodes[pointer] == 99:
            loop = False

        elif intcodes[pointer] == 1:
            one = intcodes[pointer + 1]
            two = intcodes[pointer + 2]
            three = intcodes[pointer + 3]

            intcodes[three] = intcodes[one] + intcodes[two]
        elif intcodes[pointer] == 2:
            one = intcodes[pointer + 1]
            two = intcodes[pointer + 2]
            three = intcodes[pointer + 3]

            intcodes[three] = intcodes[one] * intcodes[two]

        else:
            print("Something went wrong!")
            loop = False

        pointer += 4

    return intcodes


# Part 1
testcodes = [1, 9, 10, 3, 2, 3, 11, 0, 99, 30, 40, 50]
print(read_intcodes(testcodes))

part1=read_input()
part1[1] = 12
part1[2] = 2
print(read_intcodes(part1)[0])


# Part 2
def guess_the_noun_verb(guess):
    noun = 0
    verb = 0
    while True:
        intcodes = read_input()
        intcodes[1] = noun
        intcodes[2] = verb
        if read_intcodes(intcodes)[0] == guess:
            print(verb, noun)
            print(verb + noun *100)
            return True
        noun += 1
        if noun > 99:
            noun = 0
            verb += 1
        if verb > 99:
            print("Big Problem")
            return False


# Test Part 2
guess_the_noun_verb(2692315)

# Part 2 answer
guess_the_noun_verb(19690720)
