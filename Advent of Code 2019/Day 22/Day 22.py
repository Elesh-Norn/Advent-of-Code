from collections import deque
from sklearn.linear_model import LinearRegression
import numpy as np

def cut(deck: list, n:int)->list:
    return deck[n:]+deck[:n]


def deal_increment(deck: list, n:int)->list:
    deck = deque(deck)
    length = len(deck)
    pointer = 0
    place = {}

    while deck:
        place[pointer % length] = deck.popleft()
        pointer += n

    result = []
    for k in sorted(place.keys()):
        result.append(place[k])

    return result


def read_input(deck):
    with open('input_Day_22.txt', "r") as file:
        for x in file:
            y = x.split()
            if y[0] == "cut":
                deck = cut(deck, int(y[-1]))
            elif y[-2] == "increment":
                deck = deal_increment(deck, int(y[-1]))
            else:
                deck.reverse()
    return deck

deck = [x for x in range(10007)]
deck = read_input(deck)
print(deck.index(2019))

input_list = []

with open('input_Day_22.txt', "r") as file:
    for x in file:
        y = x.split()
        input_list.append((y[-2], y[-1]))
_y = []
x = []
def read_mega_input(position, size, looptime):
    position = position
    for z in range(looptime):
        for y in input_list:
            if y[0] == "cut":
                if int(y[1]) > 0:
                    if position > int(y[1]):
                        position = position - int(y[1])
                    else:
                        position = size - int(y[1]) + position
                else:
                    if position < size - abs(int(y[1])):
                        position = position + abs(int(y[1]))

                    else:
                        position = abs(size - position - abs(int(y[1])))

            elif y[-2] == "increment":
                position = position * int(y[-1]) % size
            else:
                position = size - 1 - position
        if z % 141582076661 == 0:
            print(z//141582076661)

    return position

print(read_mega_input(2019, 10007, 1))
print(read_mega_input(2020, 119315717514047, 101741582076661))
