class Elf:
    def __init__(self, line):
        line = line.split(" ")
        position = line[2].replace(":", "").split(",")
        dimension = line[3].replace("x", " ").split(" ")
        self.id = int(line[0].replace("#", ""))
        self.position = tuple((int(position[0]), int(position[1])))
        self.dimension = tuple((int(dimension[0]), int(dimension[1])))
        self.craft_set = self.craft()

    def craft(self):
        # Gen a set with all position of fabric
        craft_set = set()
        for tall in range(self.dimension[1]):
            for wide in range(self.dimension[0]):
                x = self.position[0] + 1 + wide
                y = self.position[1] + 1 + tall
                craft_set.add((x, y))
        return craft_set


def get_elves(filename):
    file = open(filename, "r")
    elves_set = set()
    for line in file:
        elves_set.add(Elf(line))
    file.close()
    return elves_set


def elf_overlap(elf1, elf2,  squareset, overlap_elve_set):
    for square in elf1.craft_set:
        if square in elf2.craft_set:
            overlap_elve_set.add(elf1.id)
            overlap_elve_set.add(elf2.id)
            squareset.add(square)


def elf_oversee(elves_set):
    checkset = set()
    squareset = set()
    overlap_elve_set = set()
    answer = None
    for elf1 in elves_set:
        for elf2 in elves_set:
            couple = tuple(sorted((elf1.id, elf2.id)))
            if elf1.id == elf2.id:
                continue
            if couple in checkset:
                continue
            checkset.add(couple)
            elf_overlap(elf1, elf2, squareset, overlap_elve_set)

    for elfs in elves_set:
        if elfs.id not in overlap_elve_set:
            answer = elfs.id
    return str(len(squareset)) + ' square inches and lonely elf is #' + str(answer)


elves = get_elves('Day_3_input')
print(elf_oversee(elves))
