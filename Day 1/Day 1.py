import sys
frequency_list = []
file = open('Frequency Day 1', "r")
for x in file : frequency_list.append(x)
file.close()

def find_frequency(list):
    counter = 0
    counter_list = [0]
    while True:
        for x in list:
            counter += int(x)
            if counter in counter_list:
                print('Freq twice is:' + str(counter))
                return counter
            counter_list.append(counter)

print(find_frequency(frequency_list))




