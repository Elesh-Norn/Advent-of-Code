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

class Room:

    def __init__(self, name, pos, children):
        self.name = name
        self.pos = pos
        self.children = children

class Solve:
    def __init__(self, intcode):
        self.intcode = intcode
        self.ship_map = {}

        self.forbidden_items = []

        self.dir_dict = {"east": (0, 1),
                    "west": (0, -1),
                    "north": (1, 0),
                    "south": (-1, 0)
                    }

    def dfs_unvisited(self, visited, dfs_visit,  pos):
        dfs_visit.add(pos)
        if pos not in visited:
            return []

        for key, value in self.dir_dict.items():
            if key in self.ship_map[pos].children:
                new_pos = (pos[0] + value[0], pos[1] + value[1])
                if new_pos not in dfs_visit:
                    result = self.dfs_unvisited(visited, dfs_visit, new_pos)
                    if result is not None:
                        result.append(key)
                        return result
        return None

    def insert_credit(self):
        visited = set()
        route = []
        robot_pos = (0, 0)
        next_input = ""
        game = Computer(read_input(self.intcode))

        while True:
            state = game.run(next_input)
            next_input = "Iddle"

            print(state)

            if game == "Game over":
                break

            direction = []
            for line in state.split('\n'):
                if "==" in line:
                    name = line
                for key in self.dir_dict.keys():
                    if key in line:
                        direction.append(key)

            if robot_pos not in self.ship_map:
                self.ship_map[robot_pos] = Room(name, robot_pos, set(direction))
                visited.add(robot_pos)

            if not route:
                route = self.dfs_unvisited(visited, set(), robot_pos)
            if route is None:
                print(visited)
                print("all visited")
                print("Game over")
                break
            next_input = route.pop()
            robot_pos = (robot_pos[0] + self.dir_dict[next_input][0] , robot_pos[1] + self.dir_dict[next_input][1])

solve = Solve("input_Day_25.txt")
solve.insert_credit()