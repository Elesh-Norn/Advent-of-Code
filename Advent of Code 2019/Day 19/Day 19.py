from Intcode import Computer


def read_input(path: str)->list:
    """
    Convert text file into intcode list
    """
    intcodes = []
    with open(path, "r") as file:
        for x in file:
            s = x.split(",")
            for ints in s:
                intcodes.append(int(ints))
    return intcodes


def setup_screen(screen: dict, height: int, width: int)-> None:
    """
    Print a representation of a dict.
    """
    count = 0
    for y in range(0, height):
        line = []
        for x in range(0, width):
            if screen[x, y] == 1:
                count += 1
                line.append("#")
            else :
                line.append(".")
        print("".join(line)+str(y))
    print(count)

class Solve:

    def __init__(self, path):
        self.path = path

    def part1(self, height, width):

        screen = {}
        for i in range(height):
            for j in range(width):
                explorebot = Computer(read_input(self.path))
                code = explorebot.run((j, i))
                if code == 99:
                    return screen
                elif code == 1:
                    screen[(i, j)] = 1
                else:
                    screen[(i, j)] = 0
        setup_screen(screen, height, width)

    def part2(self):

        ship_size = 100
        min_y = self.explore_binary(500, 1000, 1200, ship_size * 2)

        while True:
            loop = False
            first_x = self.get_first_x(min_y + ship_size - 1, 1200)

            for y in range(ship_size):
                itera = min_y + ship_size - 1 - y
                explorebot = Computer(read_input(self.path))
                code = explorebot.run((first_x, itera))
                check = self.check_y(itera, first_x, ship_size)
                if not check or code != 1:
                    print(min_y, "not good", y)
                    min_y += 1
                    loop = True
                    break

            if not loop:
                print(first_x, min_y)
                print((first_x) * 10000 + (min_y))
                break


    def explore_binary(self, start, end, max_point, goal):
        """
        Approximative binary search to find where you have a certain amount of beams
        """
        if start == end:
            return start

        point = start + (end - start) // 2

        count_x = 0
        for j in range(max_point):
            explorebot = Computer(read_input(self.path))
            code = explorebot.run((j, point))
            if code == 1:
                count_x += 1

        if count_x < goal:
            return self.explore_binary(point +1, end, max_point, goal)
        elif count_x > goal:
            return self.explore_binary(start, point, max_point, goal)
        else:
            return point

    def get_first_x(self, y: int, max_point: int)->int:
        """
        Return the first beam found in line y in between 0 max_point
        """
        for x in range(max_point):
            explorebot = Computer(read_input(self.path))
            code = explorebot.run((x, y))
            if code == 1:
                return x

    def check_y(self, y: int, start: int, ship_size: int)->bool:
        """

        Check if a line y, is in the beam at start position
        and start position + size of the ship
        """
        explorebot = Computer(read_input(self.path))
        code = explorebot.run((start, y))
        if code != 1:
            return False
        explorebot = Computer(read_input(self.path))
        code = explorebot.run((start+ship_size-1, y))
        if code != 1:
            return False

        return True


solve = Solve("input_Day_19_.txt")
solve.part1(50, 50)
solve.part2()
