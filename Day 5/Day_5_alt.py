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


print(list(test))
print(remove_doubles(list(test)))
print(len(remove_doubles(list(test))))

a = remove_doubles(list(get_input('Day_5_input')))
a = remove_doubles(list(get_input('Day_5_input')))
print(len(a))

