from collections import deque

class Solution():
    def __init__(self):
        self.dir = {"R": (0, 1),
                    "D": (1, 0),
                    "U": (-1, 0),
                    "L": (0, -1)}
        self.min_distance = float('inf')
        self.fewest_steps = float('inf')
        self.last_position = [0, 0]
        self.bag_of_wires = set()
        self.last_wire = set()
        self.counter = 0
        self.intersection = {}

    def reset_position(self):
        self.last_position = [0, 0]
        self.last_wire = set()
        self.counter = 0

    def read_input(self, input_deque):
        one = input_deque.popleft()
        direction = one[0]
        how_much = int(one[1:])
        self.put_wire(direction, how_much)

    def manhattan(self):
        return abs(self.last_position[0]) + abs(self.last_position[1])

    def put_wire(self, direction, how_much):

        for _ in range(how_much):
            self.counter += 1
            self.last_position[0] += self.dir[direction][0]
            self.last_position[1] += self.dir[direction][1]
            position = (self.last_position[0], self.last_position[1])
            if position in self.bag_of_wires and position not in self.last_wire:

                if self.intersection[position] + self.counter < self.fewest_steps:
                    self.fewest_steps = self.intersection[position] + self.counter

                if self.manhattan() < self.min_distance:
                    self.min_distance = self.manhattan()
            else:
                self.bag_of_wires.add(position)
                self.last_wire.add(position)

            if position not in self.intersection:
                self.intersection[position] = self.counter

            elif self.intersection[position] < self.counter:
                self.intersection[position] = self.counter


test1 = Solution()
wires = [deque(["R8","U5","L5","D3"]),
         deque(["U7","R6","D4","L4"])]
for wire in wires:
    test1.reset_position()
    while wire:
        test1.read_input(wire)

print(test1.min_distance)
print(test1.fewest_steps)


test2 = Solution()
wires = [deque(["R75","D30","R83","U83","L12","D49","R71","U7","L72"]),
         deque(["U62", "R66", "U55", "R34", "D71", "R55", "D58", "R83"])]

for wire in wires:
    test2.reset_position()
    while wire:
        test2.read_input(wire)

print(test2.min_distance)
print(test2.fewest_steps)

test3= Solution()
wires = [deque(["R98","U47","R26","D63","R33","U87","L62","D20","R33","U53","R51"]),
         deque(["U98","R91","D20","R16","D67","R40","U7","R15","U6","R7"])]

for wire in wires:
    test3.reset_position()
    while wire:
        test3.read_input(wire)

print(test3.min_distance)
print(test3.fewest_steps)

part1 = Solution()
wires_string = []
with open('input_Day_3', "r") as file:
    for x in file:
        wires_string.append(x)
wires = []
for wire in wires_string:
    wires.append(deque(wire.split(",")))

for wire in wires:
    part1.reset_position()
    while wire:
        part1.read_input(wire)


print(part1.min_distance)
print(part1.fewest_steps)
