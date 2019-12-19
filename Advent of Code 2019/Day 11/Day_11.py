from Intcode import Computer


def read_input():
    intcodes = []
    with open('input_Day_11.txt', "r") as file:
        for x in file:
            s = x.split(",")
            for ints in s:
                intcodes.append(int(ints))
    return intcodes


class Paint_square:

    __slots__ = ['pos', 'color']

    def __init__(self, color, pos):
        self.color = color
        self.pos = pos


def robot_grid(input, first):
    """
    Take care of robot errance
    """
    robot_computer = Computer(input)
    robotdir = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    pointer_position = 0
    max_y = 0
    max_x = 0
    robotpos = (0, 0)
    ship = {(0,0):Paint_square(first,(0,0))}

    while True:

        if robotpos in ship:
            see = ship[robotpos].color
        else:
            see = 0
        color_to_paint = robot_computer.run(see)
        facing = robot_computer.run()
        if color_to_paint == 99:
            break

        if robotpos not in ship:
            ship[robotpos] = Paint_square(color_to_paint, robotpos)
        else:
            ship[robotpos].color = color_to_paint

        if facing == 0:
            pointer_position += -1
        else:
            pointer_position += 1
        direction = pointer_position % 4

        y = robotpos[0] + robotdir[direction][0]
        x = robotpos[1] + robotdir[direction][1]
        if y > max_y:
            max_y = y
        if x > max_x:
            max_x = x

        robotpos = (y, x)

    return ship, max_y, max_x
ship, y, x = robot_grid(read_input(), 0)
print(len(ship))
ship, y, x = robot_grid(read_input(), 1)

layer = {}
for pos, element in ship.items():
    layer[pos] = element.color


def print_message(last_layer, HEIGHT, WIDTH):

    for y in range(HEIGHT+1, -6, -1):
        line = ""
        for x in range(0, WIDTH+1):
            if (y,x) in last_layer:
                line += "##" if last_layer[(y, x)] == 1 else "  "
            else:
                line += "  "

        print(line)

print_message(layer, y, x)
