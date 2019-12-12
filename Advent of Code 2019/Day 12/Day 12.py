
class Moon:

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        self.velx = 0
        self.vely = 0
        self.velz = 0
        self.pot = 0
        self.kin = 0


moons = [Moon(12, 0, -15) , Moon(-8, -5, -10),
         Moon(7, -17, 1), Moon(2, -11, -6)]

test = [Moon(-1, 0, 2) , Moon(2, -10, -7),
         Moon(4, -8, 8), Moon(3, 5, -1)]

test2 = [Moon(-8, -10, 0) , Moon(5, 5, 10),
         Moon(2, -7, 3), Moon(9, -8, -3)]
def gravity(moons):

    for moon in moons:
        moon.pot = 0
        moon.vel = 0


        for other in moons:
            if moon == other: continue

            if moon.x > other.x:
                moon.velx -= 1
            elif moon.x < other.x:
                moon.velx += 1

            if moon.y > other.y:
                moon.vely -= 1
            elif moon.y < other.y:
                moon.vely += 1

            if moon.z > other.z:
                moon.velz -= 1
            elif moon.z < other.z:
                moon.velz += 1

    positions = []
    for moon in moons:

        moon.x += moon.velx
        moon.y += moon.vely
        moon.z += moon.velz

        moon.pot = abs(moon.x) + abs(moon.y) + abs(moon.z)
        moon.kin = abs(moon.velx) + abs(moon.vely) + abs(moon.velz)
        positions.append(str(moon.x))
        positions.append(str(moon.y))
        positions.append(str(moon.z))
        positions.append(str(moon.velx))
        positions.append(str(moon.vely))
        positions.append(str(moon.velz))
    return tuple(positions)

def part1(moons):
    for steps in range(1000):
        gravity(moons)


    total = 0
    for moon in moons:
        total += moon.pot*moon.kin
    print(total)
def gcd(a, b):
    if (a == 0):
        return b
    return gcd(b % a, a)


# function to calculate
# lcm of two numbers.
def lcm(a, b):
    return (a * b) / gcd(a, b)
def part2(moons):
    positions = []
    for moon in moons:
        moon.x += moon.velx
        moon.y += moon.vely
        moon.z += moon.velz

        moon.pot = abs(moon.x) + abs(moon.y) + abs(moon.z)
        moon.kin = abs(moon.velx) + abs(moon.vely) + abs(moon.velz)
        positions.append(str(moon.x))
        positions.append(str(moon.y))
        positions.append(str(moon.z))
        positions.append(str(moon.velx))
        positions.append(str(moon.vely))
        positions.append(str(moon.velz))
    initial = tuple(positions)

    x_indexes = [0,3,6,9,12,15,18,21]
    y_indexes = [1,4,7,10,13,16,19,22]
    z_indexes = [2,5,8,11,14,17,20,23]
    step = 0

    cycle_x = 0
    cycle_y = 0
    cycle_z = 0
    while True:
        step += 1
        now = gravity(moons)

        if cycle_x == 0:
            flag = True
            for x in x_indexes:
                if now[x] != initial[x]:
                    flag = False
                    break
            if flag:
                cycle_x = step

        if cycle_y == 0:
            flag = True
            for y in y_indexes:
                if now[y] != initial[y]:
                    flag = False
                    break
            if flag:
                cycle_y = step

        if cycle_z == 0:
            flag = True
            for z in z_indexes:
                if now[z] != initial[z]:
                    flag = False
                    break
            if flag:
                cycle_z = step

        if cycle_x > 0 and cycle_y > 0 and cycle_z > 0:
            break
    print(cycle_z, cycle_y, cycle_x)

    a = lcm(cycle_z, cycle_y)
    b = lcm(a, cycle_x)
    print(b)





part2(moons)