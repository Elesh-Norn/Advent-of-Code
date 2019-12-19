from Intcode import Computer
from collections import deque
def read_input():
    intcodes = []
    with open('input_Day_15.txt', "r") as file:
        for x in file:
            s = x.split(",")
            for ints in s:
                intcodes.append(int(ints))
    return intcodes


def normal_next(robotpos, robotdir, obstructed, next):
    right = (robotpos[0] + robotdir[(next + 1) % 4][0], robotpos[1] + robotdir[(next + 1) % 4][1])
    forward = (robotpos[0] + robotdir[next][0], robotpos[1] + robotdir[next][1])
    left = (robotpos[0] + robotdir[(next + 3) % 4][0], robotpos[1] + robotdir[(next + 3) % 4][1])
    if right not in obstructed:
        return (next + 1) % 4

    elif forward not in obstructed:
        return next

    elif left not in obstructed:
        return (next + 3) % 4

    else:
        return (next + 2) % 4


def setup_screen(screen):
    for y in range(-21, 25):
        line = []
        for x in range(-30, 25):
            if (y, x) not in screen:
                screen[(y, x)] = "  "
            else:
                if isinstance(screen[y, x], int):
                    if len(str(screen[y, x])) == 2:
                        line.append("."+str(screen[y, x]))
                    elif len(str(screen[y, x])) == 1:
                        line.append(".."+str(screen[y, x]))
                    else:
                        line.append(str(screen[y, x]))
                else:
                    line.append(screen[y, x])
        print("".join(line))


def robot_grid(input):
    """
    Take care of robot errance
    """
    robot_computer = Computer(input)
    screen = {}
    # haut, droite, bas, gauche
    robotdir = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    robot_translate = {(0, 1): 4, (-1, 0): 2,
                       (0, -1): 3,  (1, 0): 1}
    max_y = 0
    max_x = 0
    robotpos = (0, 0)
    obstructed = set()
    next = 0
    count = 0
    while count < 5001:
        prev_next = next
        next = normal_next(robotpos, robotdir, obstructed, next)
        code = robot_computer.run(robot_translate[robotdir[next]])
        y = robotpos[0] + robotdir[next][0]
        x = robotpos[1] + robotdir[next][1]

        if y > max_y:
            max_y = y
        if x > max_x:
            max_x = x

        if code == 0:
            obstructed.add((y, x))
            screen[(y, x)] = "###"
            next = prev_next
        else:
            if robotpos in screen:
                if screen[robotpos] != "  X":
                    screen[robotpos] = "   "
            else:
                screen[robotpos] = "   "

            robotpos = (y, x)
            if code == 2:
                print(robotpos)
                screen[robotpos] = "  X"
            else:
                screen[robotpos] = "  D"
        count += 1
    return screen


def bfs_find_shortest(screen):
    queue = deque()
    queue.append((0, 0))
    adjacent = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    visited = set()
    while queue:
        pos = queue.popleft()

        for adj in adjacent:
            current = (pos[0] + adj[0], pos[1] + adj[1])

            if current not in visited:
                if screen[current] == '  X':
                    setup_screen(screen)
                    return screen[pos] + 1

                elif screen[current] == '###':
                    visited.add(current)

                elif screen[current] == '   ' or screen[current] == '  D':
                    screen[current] = screen[pos] + 1
                    queue.append(current)

        visited.add(pos)


def bfs_fill_room(screen, start):
    queue = deque()
    queue.append(start)
    screen[start] = 0
    adjacent = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    visited = set()
    count = 0
    while queue:
        pos = queue.popleft()

        for adj in adjacent:
            current = (pos[0] + adj[0], pos[1] + adj[1])

            if current not in visited:
                if screen[current] == '  X':
                    setup_screen(screen)

                elif screen[current] == '###':
                    visited.add(current)

                elif screen[current] == '   ' or screen[current] == '  D':
                    screen[current] = screen[pos] + 1
                    queue.append(current)
        count = screen[pos]
        visited.add(pos)
    return count


fill = robot_grid(read_input())
setup_screen(fill)
setup_screen(fill)
print(bfs_fill_room(fill, (-14, -16)))
setup_screen(fill)

