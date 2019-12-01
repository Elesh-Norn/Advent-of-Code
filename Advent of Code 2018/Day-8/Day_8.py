def get_input(filename, l=[]):
    file = open(filename, "r")
    input = None
    for line in file:
        input = line.split(" ")
    file.close()
    dummy_list = []
    for element in input:
        dummy_list.append(int(element))
    return dummy_list

test_list = [2, 3, 0, 3, 10, 11, 12, 1, 1, 0, 1, 99, 2, 1, 1, 2]
meta_list = []


def tree(index, the_list):
    child = the_list[index]
    metadata = the_list[index+1]
    index += 2
    while child > 0:
        index = tree(index, the_list)
        child -= 1
    for meta in range(metadata):
        meta_list.append(the_list[meta+index])
    return index + metadata

tree(0, test_list)
print(sum(meta_list))

meta_list = []
tree(0, get_input("Day_8_test"))
print(sum(meta_list))
