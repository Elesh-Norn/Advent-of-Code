from collections import deque

class Node:

    def __init__(self, id, exit_pos):
        self.id = id
        self.exit = exit_pos
        self.children = {}

    def __repr__(self):

        line = "".join([str(self.id) + " with exit " + str(self.exit) +" with children:\n"])
        for children, distance in self.children.items():

            line += "".join([children, " distance: ", str(distance), "\n"])
        return line

def parse_maze(path:str)->tuple:
    maze = {}
    max_x = 0
    with open(path) as file:
        y = 0
        for lines in file:
            s = list(lines)
            for x, element in enumerate(s):
                maze[(x, y)] = element
                if x > max_x:
                    max_x = x

            y += 1
    return maze, y, max_x

def find_exit(maze, pos)->tuple:
    adjacent = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    for adj in adjacent:
        current = (pos[0] + adj[0], pos[1] + adj[1])
        if current in maze:
            if maze[current] == ".":
                return current
    return None

def find_other_letter(maze:dict, pos:tuple)->tuple:
    adjacent = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    for adj in adjacent:
        current = (pos[0] + adj[0], pos[1] + adj[1])
        if find_exit(maze, pos) is None:
            if find_exit(maze, current) is not None and maze[current].isupper():
                return current
        else:
            if find_exit(maze, current) is None and maze[current].isupper():
                return current
    return None

def change_letters(maze):
    ref = set()
    replace_dict = {}

    for key, element in maze.items():
        if element.isupper():
            if element not in ref:
                ref.add(element)
            else:
                replace_dict[key] = element

    for key, element in replace_dict.items():
        maze[key] = element.lower()

    return maze

def draw_paths(maze, height, width):
    path_ref = {}
    count = 0
    for key, element in maze.items():
        if element.isupper():
            path_ref[count] = bfs_find_distances(maze, key)
            count += 1

    dict_outer = {}
    dict_inner = {}
    for key, item in path_ref.items():

        if item.exit[1] == 2 or item.exit[0] == 2 \
            or item.exit[1] == height - 3 or item.exit[0] == width - 3:
            dict_outer[item.id] = item

        else:
            dict_inner[item.id] = item
    return dict_outer, dict_inner


def bfs_find_distances(maze, start):
    screen = dict(maze)
    exit_pos = find_exit(maze, start)
    other_letter = find_other_letter(maze, start)
    if exit_pos is None:
        exit_pos = find_exit(maze, other_letter)
    portal_id = sorted(screen[start] + screen[other_letter])
    node = Node("".join(portal_id), exit_pos)

    queue = deque()
    queue.append(node.exit)


    screen[node.exit] = 0
    adjacent = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    visited = set()

    while queue:
        pos = queue.popleft()
        for adj in adjacent:
            current = (pos[0] + adj[0], pos[1] + adj[1])
            if current not in visited and current in screen:

                if screen[current] == ".":
                    screen[current] = screen[pos] + 1
                    queue.append(current)
                    visited.add(current)

                elif screen[current].isupper():
                    node_id = sorted(maze[current] + maze[find_other_letter(maze, current)])
                    node_id = "".join(node_id)
                    if node_id != node.id:
                        node.children[node_id] = screen[pos]
                    visited.add(current)

                else:
                    visited.add(current)

        visited.add(pos)

    return node


maze, y, x = parse_maze("input_Day_20.txt")

outer_dict, inner_dict = draw_paths(maze, y, x)
print(outer_dict.keys())
print(inner_dict.keys())
def solve(outer_dict, inner_dict, height, width):

    def traverse(start: Node, visited: set, count: int):
        visit = set(visited)
        visit.add(start.id)
        print(visit, count)


        result = []
        for key, item in start.children.items():
            if key in visited:
                continue
            if key == "ZZ":
                return item + count

            if key in inner_dict:
                if start.id in inner_dict[key].children:
                    if inner_dict[key].children[start.id] == item:
                        result.append(traverse(outer_dict[key], visit, count + item +1))
                    else:
                        result.append(traverse(inner_dict[key], visit, count + item + 1))
                else:
                    result.append(traverse(inner_dict[key], visit, count + item + 1))
            else:
                result.append(traverse(inner_dict[key], visit, count + item + 1))

        return min(result) if result != [] else float('inf')

    return traverse(outer_dict["AA"], set(), 0)

print(solve(outer_dict, inner_dict, y, x))