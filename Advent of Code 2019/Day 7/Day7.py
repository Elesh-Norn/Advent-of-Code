def read_input():
    intcodes = []
    with open('Day_7_input.txt', "r") as file:
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
                self.input_1 = intcodes[intcodes[pointer + 1]]
            elif self.mode1 == 1:
                self.input_1 = intcodes[pointer + 1]
            elif self.mode1 == 2:
                self.input_1 = intcodes[base]

            if self.mode2 == 0:
                self.input_2 = intcodes[intcodes[pointer + 2]]
            elif self.mode2 == 1:
                self.input_2 = intcodes[pointer + 2]
            elif self.mode2 == 2:
                self.input_2 = intcodes[base]

    def add(self, intcodes: list, pointer: int, base: int)->int:
        if self.mode3 == 2:
            intcodes[base] = self.input_1 + self.input2
        else:
            intcodes[intcodes[pointer + 3]] = self.input_1 + self.input_2
        return pointer + 4

    def mul(self, intcodes: list, pointer: int, base: int)->int:
        if self.mode3 == 2:
            intcodes[base] = self.input_1 * self.input2
        else:
            intcodes[intcodes[pointer + 3]] = self.input_1 * self.input_2
        return pointer + 4

    def read_input(self, intcodes: list, pointer: int, base: int, code: int)->int:
        if self.mode1 == 0:
            intcodes[intcodes[pointer + 1]] = code
        elif self.mode1 == 1:
            intcodes[pointer + 1] = code
        else:
            intcodes[base] = code
        return pointer + 2

    def print_output(self, intcodes: list, pointer: int, base: int)->int:
        if self.mode1 == 0:
            self.output = intcodes[intcodes[pointer + 1]]
        elif self.mode1==1:
            self.output =intcodes[pointer + 1]
        else:
            self.output = intcodes[base]
        return pointer + 2

    def is_less_than(self, intcodes: list, pointer: int, base: int)->int:
        if self.mode3 == 0:
            intcodes[intcodes[pointer + 3]] = 1 if self.input_1 < self.input_2 else 0
        else:
            intcodes[base] = 1 if self.input_1 < self.input_2 else 0
        return pointer + 4

    def is_equal_to(self, intcodes: list, pointer: int, base: int)->int:
        if self.mode3 == 0:
            intcodes[intcodes[pointer + 3]] = 1 if self.input_1 == self.input_2 else 0
        else:
            intcodes[base] = 1 if self.input_1 == self.input_2 else 0
        return pointer + 4


    def jump_if_false(self, intcodes, pointer: int)->int:

        if self.input_1 != 0:
            return self.input_2
        else:
            return pointer + 3

    def jump_if_true(self, intcodes, pointer: int)->int:
        if self.input_1 == 0:
            return self.input_2
        else:
            return pointer + 3

    def ofset_base(self, intcodes, pointer: int, base: int)->(int, int):
        base += self.input_1
        return pointer + 2, base

class Amplifier:

    def __init__(self, intcode:list):

        self.intcodes = intcode
        self.pointer = 0
        self.output = 0
        self.phase = False
        self.function_dico = {
            1: Outcode.add,
            2: Outcode.mul,
            3: Outcode.read_input,
            4: Outcode.print_output,
            5: Outcode.jump_if_false,
            6: Outcode.jump_if_true,
            7: Outcode.is_less_than,
            8: Outcode.is_equal_to,
        }

    def run(self, input_code: int)->(int, bool):

        while True:
            outcode = Outcode(self.intcodes, self.pointer)
            if outcode.opcode == 99:
                return self.output, False

            elif 0 < outcode.opcode < 9:
                if outcode.opcode == 3:
                    self.pointer = self.function_dico[outcode.opcode](outcode,
                                                                      self.intcodes,
                                                                      self.pointer,
                                                                      input_code)
                    if self.phase is False:
                        self.phase = input_code
                        return

                elif outcode.opcode == 4:
                    self.pointer = self.function_dico[outcode.opcode](outcode,
                                                                      self.intcodes,
                                                                      self.pointer)
                    self.output = outcode.output
                    return self.output, True

                else:
                    self.pointer = self.function_dico[outcode.opcode](outcode,
                                                                      self.intcodes,
                                                                      self.pointer)


            else:
                print("Something went wrong!")
                return None, False


def ampli():
    maxi = float('-inf')
    for x in range(0, 44445):
        output = 0
        digiset = set()
        phase = str(x)

        while len(phase) <5:
            phase = '0' + phase

        for digit in phase:
            if output is None:
                break
            if digit in digiset or int(digit) > 4:
                output = None
                break
            digiset.add(digit)

            amp = Amplifier(read_input())
            amp.run(int(digit))
            output, _ = amp.run(output)

        if output is not None:
            if output > maxi:
                maxi = output

    print(maxi)


def feedback_loop():
    maxi = float('-inf')
    for x in range(56789, 100000):

        digiset = set()
        phases = []
        for digit in str(x):
            if digit in digiset or int(digit) < 5:
                break
            digiset.add(digit)
            phases.append(int(digit))

        if len(phases) == 5:
            AmpliChain = []
            for phase in phases:
                amp = Amplifier(read_input())
                amp.run(phase)
                AmpliChain.append(amp)

            loop = True
            counter = 0
            output = 0

            # Loop become false when it hit a 99
            while loop:
                amp = AmpliChain[counter % 5]
                output, loop = amp.run(output)
                counter += 1

            # Look at last input from E
            if AmpliChain[4].output > maxi:
                maxi = AmpliChain[4].output

    print(maxi)

def resolve():

    ampli()
    feedback_loop()
