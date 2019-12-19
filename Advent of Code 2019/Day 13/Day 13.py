from Intcode import Computer


def read_input():
    intcodes = []
    with open('input_Day_13.txt', "r") as file:
        for x in file:
            s = x.split(",")
            for ints in s:
                intcodes.append(int(ints))
    return intcodes


def setup_screen(screen):
    for y in range(20):
        line = []
        for x in range(40):
            if (x, y) not in screen:
                screen[(x, y)] = " "
            else:
                line.append(screen[x, y])
        print("".join(line))


arcade = Computer(read_input())
code = 0
paddle_position = (0,0)
ball_position = (0,0)
x = 0
y = 0
block = 0
screen = {}
max_x = float('-inf')
max_y = float('-inf')
while code != 99:
    x = arcade.run()
    y = arcade.run()
    code = arcade.run()

    if code == 0:
        screen[(x, y)] = " "
    elif code == 1:
        screen[(x, y)] = "#"
    elif code == 2:
        screen[(x, y)] = "X"
    elif code == 3:
        screen[(x, y)] = "-"
    else:
        screen[(x, y)] = "o"

    if code == 2:
        block += 1
    if code == 3:
        paddle_position = (x, y)
    elif code == 4:
        ball_position = (x, y)

setup_screen(screen)
game_input = read_input()
game_input[0] = 2
code = 0
next_input = 0
playing = Computer(game_input)


while code != 99:
    x = playing.run(next_input)
    y = playing.run(next_input)
    code = playing.run(next_input)
    if code == 0:
        screen[(x, y)] = " "
    elif code == 1:
        screen[(x, y)] = "#"
    elif code == 2:
        screen[(x, y)] = "X"
    elif code == 3:
        screen[(x, y)] = "-"
    else:
        screen[(x, y)] = "o"
    print('')
    print('')
    print('')
    print('')
    print('')
    print('')
    setup_screen(screen)
    if x == -1 and y == 0:
        print(code)
    else:
        if code == 3:
            paddle_position = (x, y)
        elif code == 4:
            ball_position = (x, y)


    if ball_position[0] > paddle_position[0]:
        next_input = 1
    elif ball_position[0] < paddle_position[0]:
        next_input = -1
    else:
        next_input = 0


