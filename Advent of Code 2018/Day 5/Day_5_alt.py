import sys

test = 'dabAcCaCBAcCcaDA'
count = 0

def get_input(filename):
    file = open(filename, "r")
    word = None
    for line in file:
        word = line
    file.close()
    return line

def check(letter, top):
    if letter.islower() and top.isupper() and letter == top.lower():
        return True
    if letter.isupper() and top.islower() and letter == top.upper():
        return True

def remove_doubles(list):
    global count
    d_list = []

    for letter in list:
        if d_list == []:
            d_list.append(letter)
            continue
        if check(letter, d_list[-1]):
            d_list.pop()
        else:
            d_list.append(letter)

    return "".join(d_list)

print(len(remove_doubles(list(test))))

a = remove_doubles(list(get_input('Day_5_input')))
print(len(a))

# PART 2

def remove_doubles2(list, letter):
    global count
    d_list = []
    for x in list:

        if x == letter.upper():
            continue
        if x == letter.lower():
            continue
        else:
            d_list.append(x)

    d_list = remove_doubles(d_list)

    return "".join(d_list)

def part_2(list):
    answer_dic = {}

    for letter in ['a','z','e','r','t','y','u','i','o','p','q','s','d','f','g','h','j','k','l','m','w','x','c','v','b','n']:
        answer_dic[letter] = len(remove_doubles2(list, letter))

    return min(zip(answer_dic.values(), answer_dic.keys()))

print(part_2(list(get_input('Day_5_input'))))