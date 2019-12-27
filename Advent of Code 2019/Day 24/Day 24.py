def print_Eris(set_bugs, width, height):
    result = []
    line = []
    for y in range(height):
        for x in range(width):
            if (y, x) in set_bugs:
                line.append("#")
            else:
                line.append(".")
        print("".join(line))
        result.append("".join(line))
        line = []
    print("_____________________")
    return "".join(result)


def generation(n:int, set_bugs):
    width = 5
    height = 5

    past_layout = set()

    for gen in range(n):
        eris = print_Eris(set_bugs, width, height)
        if eris in past_layout:
            return eris
        past_layout.add(eris)
        infestation = set()
        empty_space = set()


        for bug in set_bugs:
            bug_count = 0

            for adj in [(1, 0), (0, 1), (-1, 0), (0,-1)]:
                current = (bug[0] + adj[0], (bug[1] + adj[1]))
                if 0 <= current[0] < width and 0 <= current[1] < height:
                        if current in set_bugs:
                            bug_count += 1
                        else:
                            empty_space.add(current)
            if bug_count == 1:
                infestation.add(bug)

        for space in empty_space:
            bug_count = 0

            for adj in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                current = (space[0] + adj[0], (space[1] + adj[1]))
                if 0 <= current[0] < width and 0 <= current[1] < height:
                    if current in set_bugs:
                        bug_count += 1
            if 0 < bug_count < 3:
                infestation.add(space)

        set_bugs = infestation

def calculate_point( layout):
    count = 0
    for i, element in enumerate(list(layout)):
        if element == "#":
            count+= 2**(i)
    return count

test_bugs = [(0, 4), (1, 0), (1, 3), (2, 0),
                (2, 3), (2, 4), (3, 2), (4, 0)]
print(calculate_point(generation(100, test_bugs)))

input_bugs = [(0, 0), (0, 1), (0, 3),
              (1, 1), (1, 2),
              (2, 0), (2, 1), (2, 3),
              (3, 1), (3, 2),  (3, 3), (3, 4),
              (4, 0), (4, 1), (4, 2)]
print(calculate_point(generation(1000, input_bugs)))
