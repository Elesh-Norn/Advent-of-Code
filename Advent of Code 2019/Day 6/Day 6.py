from collections import deque, defaultdict
from datetime import datetime

def read_input():
    orbits = defaultdict(list)
    backref = defaultdict(list)

    with open('Day_6_input.txt', "r") as file:
        for x in file:
            object = x[:3]
            orbit = x[4:7]
            orbits[object].append(orbit)
            backref[orbit].append(object)

        for k, v in backref.items():
            if k not in orbits:
                orbits[k] = []

    return orbits, backref


def explore_space(orbits, backref):
    galaxy_map = {}

    def chart_space():
        for k in orbits.keys():
            galaxy_map[k] = 0

    def crawl_map(body, count):

        for k in backref[body]:
            if galaxy_map[body] > 0:
                galaxy_map[body] += count
                crawl_map(k, count)
            else:
                galaxy_map[body] += count
                crawl_map(k, count + 1)

    chart_space()
    for x, y in orbits.items():
        if not y:
            crawl_map(x, 0)
    count = 0
    for k in orbits.keys():
        count += len(o[k]) + galaxy_map[k]
    return count


def find_santa(backref, orbits):
    counter = 0
    visited = set()
    level = ["YOU"]  # Baba is
    while level:
        # Level is how far it is from you
        queue = deque(level)
        level = []

        while queue:
            # Simple bfs
            root = queue.popleft()
            if "SAN" in backref[root] or "SAN" in orbits[root]:
                return counter - 1

            for parent in backref[root]:
                if parent not in visited:
                    level.append(parent)

            for child in orbits[root]:
                if child not in visited:
                    level.append(child)

            visited.add(root)

        counter += 1


# Answer
o, b = read_input()
print(explore_space(o, b)) # Part 1
print(find_santa(o, b)) # Part 2

# Runtime of 1000 iterations
avg1 = []
avg2 = []
for x in range(1000):
    now = datetime.now()
    o, b = read_input()
    explore_space(o, b)
    part1 = datetime.now()
    avg1.append((part1 - now).total_seconds())

for x in range(1000):
    now = datetime.now()
    o, b = read_input()
    find_santa(o, b)
    part2 = datetime.now()
    avg2.append((part2 - now).total_seconds())

print(sum(avg1)/1000)
print(sum(avg2)/1000)

