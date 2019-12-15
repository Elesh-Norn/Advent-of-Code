from collections import deque
def read_input():
    intcodes = []
    with open('input_Day_15.txt', "r") as file:
        for x in file:
            s = x.split(",")
            for ints in s:
                intcodes.append(int(ints))
    return intcodes


class Outcode:

    def __init__(self, intcodes, pointer, base):
        outcode = str(intcodes[pointer])
        self.opcode = int(outcode[-2:])
        self.mode1 = int(outcode[-3]) if len(outcode) > 2 else 0
        self.mode2 = int(outcode[-4]) if len(outcode) > 3 else 0
        self.mode3 = int(outcode[-5]) if len(outcode) > 4 else 0
        if self.opcode < 3 or 99 > self.opcode > 4:

            if self.mode1 == 0:
                adress = intcodes[pointer + 1]
            elif self.mode1 == 1:
                adress = pointer + 1
            elif self.mode1 == 2:
                adress = intcodes[pointer + 1] + base

            intcodes = self.memory_check(adress, intcodes)
            self.input_1 = intcodes[adress]

            if self.opcode != 9:
                if self.mode2 == 0:
                    adress = intcodes[pointer + 2]
                elif self.mode2 == 1:
                    adress = pointer + 2
                elif self.mode2 == 2:
                    adress = intcodes[pointer + 2] + base

                intcodes = self.memory_check(adress, intcodes)
                self.input_2 = intcodes[adress]

    def add(self, intcodes: list, pointer: int, base: int)->int:
        adress = intcodes[pointer + 3] + base if self.mode3 == 2 else intcodes[pointer + 3]
        intcodes = self.memory_check(adress, intcodes)
        intcodes[adress] = self.input_1 + self.input_2

        return pointer + 4

    def mul(self, intcodes: list, pointer: int, base: int)->int:
        adress = intcodes[pointer + 3] + base if self.mode3 == 2 else intcodes[pointer + 3]
        intcodes = self.memory_check(adress, intcodes)
        intcodes[adress] = self.input_1 * self.input_2

        return pointer + 4

    def read_input(self, intcodes: list, pointer: int, base: int, robocode:int)->int:
        adress = intcodes[pointer + 1] + base if self.mode1 == 2 else intcodes[pointer + 1]

        intcodes = self.memory_check(adress, intcodes)
        intcodes.append(0)
        intcodes[adress] = robocode
        return pointer + 2

    def print_output(self, intcodes: list, pointer: int, base: int)->int:
        if self.mode1 == 0:
            adress = intcodes[pointer + 1]
        elif self.mode1 == 1:
            adress = pointer + 1
        else:
            adress = intcodes[pointer + 1] + base

        intcodes = self.memory_check(adress, intcodes)
        self.output = intcodes[adress]
        return pointer + 2

    def is_less_than(self, intcodes: list, pointer: int, base: int)->int:
        if self.mode3 == 0:
            adress = intcodes[pointer + 3]
        else:
            adress = intcodes[pointer + 3] + base

        intcodes = self.memory_check(adress, intcodes)
        intcodes[adress] = 1 if self.input_1 < self.input_2 else 0
        return pointer + 4

    def is_equal_to(self, intcodes: list, pointer: int, base: int)->int:
        if self.mode3 == 0:
            adress = intcodes[pointer + 3]
        else:
            adress = intcodes[pointer + 3] + base

        intcodes = self.memory_check(adress, intcodes)
        intcodes[adress] = 1 if self.input_1 == self.input_2 else 0
        return pointer + 4


    def jump_if_false(self, intcodes, pointer: int, base: int)->int:

        if self.input_1 != 0:
            return self.input_2
        else:
            return pointer + 3

    def jump_if_true(self, intcodes, pointer: int, base: int)->int:
        if self.input_1 == 0:
            return self.input_2
        else:
            return pointer + 3

    def ofset_base(self, intcodes, pointer: int, base: int)->(int, int):
        base += self.input_1
        return pointer + 2, base

    def memory_check(self, adress, intcodes):
        if adress >= len(intcodes):
            for x in range(adress - len(intcodes)):
                intcodes.append(0)
            intcodes.append(0)
            return intcodes
        return intcodes

class Computer:

    def __init__(self, intcode:list):

        self.intcodes = intcode
        self.pointer = 0
        self.output = 0
        self.phase = False
        self.base = 0
        self.function_dico = {
            1: Outcode.add,
            2: Outcode.mul,
            3: Outcode.read_input,
            4: Outcode.print_output,
            5: Outcode.jump_if_false,
            6: Outcode.jump_if_true,
            7: Outcode.is_less_than,
            8: Outcode.is_equal_to,
            9: Outcode.ofset_base
        }

    def run(self, robotcode=None)->(int, bool):

        while True:
            outcode = Outcode(self.intcodes, self.pointer, self.base)
            if outcode.opcode == 99:
                return 99

            elif 0 < outcode.opcode < 10:
                if outcode.opcode == 3:
                    self.pointer = self.function_dico[outcode.opcode](outcode,
                                                                      self.intcodes,
                                                                      self.pointer,
                                                                      self.base, robotcode)

                elif outcode.opcode == 4:
                    self.pointer = self.function_dico[outcode.opcode](outcode,
                                                                      self.intcodes,
                                                                      self.pointer,
                                                                      self.base)
                    self.output = outcode.output
                    return self.output

                elif outcode.opcode == 9:
                    self.pointer, self.base = self.function_dico[outcode.opcode](outcode,
                                                                  self.intcodes,
                                                                  self.pointer,
                                                                  self.base)
                else:
                    self.pointer = self.function_dico[outcode.opcode](outcode,
                                                                      self.intcodes,
                                                                      self.pointer,
                                                                      self.base)

            else:
                print("Something went wrong!")
                return 99


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
    print("_____________________________________________")
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
    #haut, droite, bas, gauche
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
    queue.append((0,0))
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

