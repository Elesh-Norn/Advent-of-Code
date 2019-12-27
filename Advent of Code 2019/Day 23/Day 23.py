from Intcode import Computer
from collections import defaultdict, deque


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

network = {}
first = {}
for computer in range(50):

    intcode = read_input("input_Day_23.txt")
    network[computer] = Computer(intcode)
    first[computer] = True


def run_network(network):
    queue = defaultdict(deque)

    while True:

        for adress, computer in network.items():
            paquet = None

            if first[adress]:
                first[adress] = False
                paquet = computer.run([adress])

            elif len(queue[adress]) == 0:
                paquet = network[adress].run()

            else:
                instruction = queue[adress].popleft()
                paquet = computer.run(instruction)

            if paquet is not None:
                if paquet == 99:
                    return "Problem in intcode"
                elif paquet[0] == 255:
                    return paquet[2]
                elif paquet[0] in network.keys():
                    queue[paquet[0]].append((paquet[1], paquet[2]))
                else:
                    return "Problem!"


def run_nat(network):
    queue = defaultdict(deque)
    nat = None
    is_idle = {}
    y_values = []

    while True:
        for adress, computer in network.items():

            if first[adress]:
                first[adress] = False
                paquet = computer.run([adress])

            elif adress == 0 and all(is_idle.values()) and nat is not None:
                if nat in y_values:
                    return nat[1]
                y_values.append(nat)
                paquet = computer.run(nat)


            elif len(queue[adress]) == 0:
                paquet = network[adress].run()

            else:
                instruction = queue[adress].popleft()
                paquet = computer.run(instruction)

            is_idle[adress] = computer.idle

            if type(paquet) is not bool:
                if paquet == 99:
                    return "Problem in intcode"

                elif paquet[0] == 255:

                    nat = (paquet[1], paquet[2])
                    print(nat)

                elif paquet[0] in network.keys():
                    queue[paquet[0]].append((paquet[1], paquet[2]))

                else:
                    return "Problem!"

print(run_nat(network))
