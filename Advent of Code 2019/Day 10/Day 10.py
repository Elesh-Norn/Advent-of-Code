from collections import defaultdict, deque
import math
def read_input():
    asteroids = set()
    with open('input_Day_10.txt', "r") as file:
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
        if asteroid == others:
            continue
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
    upright = defaultdict(deque)
    downright = defaultdict(deque)
    upleft = defaultdict(deque)
    downleft = defaultdict(deque)

    for slope in order:
        if slope[1] >= 0:

            for rock in sorted(coordinates[slope], key= lambda x: x[1]):
                if rock[1] >= couple[1]:
                    upright[slope[1]].append(rock)
                else:
                    downleft[slope[1]].appendleft(rock)
        else:
            for rock in sorted(coordinates[slope], key= lambda x: x[1]):
                if rock[1] < couple[1]:
                    upleft[slope[1]].append(rock)
                else:
                    downright[slope[1]].appendleft(rock)
    county = 0
    iterating = 0
    upr_keys = sorted(upright.keys(), reverse=True)
    dwr_keys = sorted(downright.keys(), reverse=True)
    dwl_keys = sorted(downleft.keys(), reverse=True)
    print(dwl_keys)
    upl_keys = sorted(upleft.keys(), reverse=True)
    while county < 201:
        dictionaries = [upright, downright, downleft, upleft][iterating %4]
        dic_keys = [upr_keys, dwr_keys, dwl_keys, upl_keys][iterating %4]


        for slopey in dic_keys:
            if len(dictionaries[slopey])> 0:
                target = dictionaries[slopey].popleft()
                county += 1
                print(target, county)
        iterating += 1



vaporize((31,25))
