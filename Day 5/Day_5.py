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

def check(list, idx):
    if list[idx].islower() and list[idx - 1].isupper() and list[idx] == list[idx-1].lower():
        return True
    if list[idx].isupper() and list[idx - 1].islower() and list[idx] == list[idx-1].upper():
        return True

def remove_doubles(list):
    global count
    d_list = list.copy()
    for idx in range(1, len(list)):

        if check(list, idx):
            d_list.pop(idx)
            d_list.pop(idx-1)
            count +=1
            if count > 900:
                count = 0
                print(len(d_list))
                return "".join(d_list)
            d_list = remove_doubles(d_list)
            break

    return "".join(d_list)


print(list(test))
print(remove_doubles(list(test)))
print(len(remove_doubles(list(test))))

a = remove_doubles(list(get_input('Day_5_input')))

print(len(a))
for _ in range(50):
    a = remove_doubles(list(a))

print(len(a))
