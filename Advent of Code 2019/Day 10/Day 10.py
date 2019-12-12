from collections import defaultdict, deque
import math
def read_input():
    asteroids = set()
    with open('test1.txt', "r") as file:
        height = 0
        for y in file:
            width = 0
            list_y = list(y)
            if "\n" in list_y:
                list_y.remove("\n")
            list_y = deque(list_y)
            while list_y:
                asteroid = list_y.popleft()
                if asteroid == "#":
                    asteroids.add((height, width))
                width += 1
            height += 1
    return asteroids

asteroids = read_input()

def get_equation(x1, y1, x2, y2):
    a = round((y2 -y1)/(x2-x1) if (x2-x1) != 0 else 1, 4)
    b = round(y1 -a*x1, 4)
    return a, b

slope_dict = {}

for asteroid in asteroids:
    slope_dict[asteroid] = defaultdict(list)

for asteroid in asteroids:
    for others in asteroids:
        a, b = get_equation(asteroid[1], asteroid[0], others[1], others[0])
        slope_dict[asteroid][(a, b)].append(others)

def line_of_sight():
    max_sight = 0
    max_asteroid = None
    for key, asteroidz in slope_dict.items():
        count = 0
        for slopey in asteroidz.values():

            if len(slopey) == 1:
                count += 1
            else:
                if key[1] == slopey[0][1]:
                    sorted_sl = sorted(slopey +[key], key=lambda x: x[0])
                else:
                    sorted_sl = sorted(slopey + [key], key=lambda x: x[1])

                if sorted_sl.index(key) == 0:
                    count += 1
                elif sorted_sl.index(key) == len(slopey):
                    count += 1
                else:
                    count += 2
        if count > max_sight:
            max_sight = count
            max_asteroid = key

    print(max_asteroid, max_sight)
line_of_sight()
#31,25
def vaporize(couple):
    coordinates = slope_dict[couple[0], couple[1]]
    order = sorted(coordinates.keys(), key= lambda x: x[0], reverse = True)
    new_order = {}
    reversed_order = {}
    clock = {}
    for slope in order:
        if slope[0] != 0:
            new_order[slope] = deque(sorted(coordinates[slope], key= lambda x: x[0]))
            reversed_order[slope] = deque(sorted(coordinates[slope], key=lambda x: x[0], reverse = True))
        else:
            new_order[slope] = deque(sorted(coordinates[slope], key=lambda x: x[1]))
            reversed_order[slope] = deque(sorted(coordinates[slope], key=lambda x: x[1], reverse = True))
        clock[slope] = True

    count = 0
    iterating = 0
    target_bag = set()
    while count < 201:

        target = None
        while target is None:
            iter_slope = order[iterating % len(order)]
            if len(new_order[iter_slope]) > 0:

                if clock[slope]:
                    for element in new_order[iter_slope]:
                        if element == couple:
                            continue
                        if element[1] == couple[1]:
                            if element[0] > couple[0]:
                                target = element
                                break
                        elif element[1] > couple[1]:
                            target = element
                        if target is not None:
                            reversed_order[iter_slope].remove(target)
                            new_order[iter_slope].remove(target)
                        if target in target_bag:
                            target = None
                        else:
                            target_bag.add(target)
                            clock[slope] = False
                            break

                else:
                    for element in reversed_order[iter_slope]:
                        if element == couple:
                            continue
                        if element[1] == couple[1]:
                            if element[0] < couple[0]:
                                target = element
                                break
                        elif element[1] < couple[1]:
                            target = element

                        if target is not None:
                            reversed_order[iter_slope].remove(target)
                            new_order[iter_slope].remove(target)
                        if target in target_bag:
                            target = None
                        else:
                            target_bag.add(target)
                            clock[slope] = True
                            break

            iterating += 1
        print(target, target[1]*100+target[0], count)
        count += 1



vaporize((13,11))