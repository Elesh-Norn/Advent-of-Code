def read_input():
    intcodes = []
    with open('input_Day_13.txt', "r") as file:
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


arcade = Computer(read_input())
code = 0
paddle_position = (0,0)
ball_position = (0,0)
x = 0
y = 0
block = 0
while code != 99:
    x = arcade.run()
    y = arcade.run()
    code = arcade.run()

    if code == 2:
        block += 1
    if code == 3:
        paddle_position = (x, y)
    elif code == 4:
        ball_position = (x, y)


game_input = read_input()
game_input[0] = 2
code = 0
next_input = 0
playing = Computer(game_input)

while code != 99:
    x = playing.run(next_input)
    y = playing.run(next_input)
    code = playing.run(next_input)
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