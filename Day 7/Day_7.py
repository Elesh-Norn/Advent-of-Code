class Step:
    def __init__(self, name):
        self.name = name
        self.step = set()

    def add_step(self, step):
        self.step.add(step)

def get_input(filename):
    file = open(filename, "r")
    step_dic = {}

    for line in file:
        line = line.split(" ")
        after = line[-3]
        before = line[1]
        if after in step_dic.keys():
            step_dic[after].add_step(before)
        else:
            step_dic[after] = Step(after)
            step_dic[after].add_step(before)
    file.close()
    file = open(filename, "r")
    for line in file:
        line = line.split(" ")
        before = line[1]
        if before not in step_dic.keys():
            step_dic[before] = Step(before)
            step_dic[before].add_step('Start')
    file.close()
    return step_dic


class Elf:

    def __init__(self, id):
        self.id = id
        self.time = None
        self.step = None

    def work(self, step, worktime):
        self.step = step
        self.time = worktime + ord(step.lower()) - 96

    def done(self):
        self.time = None
        self.step = None

class resolve_attempt:

    def __init__(self, dic):
        self.dic = dic
        self.step_list = []
        self.possibles = []
        self.total_time = 0

    def check_before(self, step):
        # if already in the list
        if step.name in self.step_list:
            return
        # Pick the start since it have no requirements
        if 'Start' in step.step:
            self.possibles.append(step.name)
        # Check if all requirements are met
        else:
            dummy_list = []
            for thing in step.step:
                if thing in self.step_list:
                    dummy_list.append(True)
                else:
                    dummy_list.append(False)
            # If all requirements are met, then it's possible
            if all(dummy_list) and dummy_list != []:
                self.possibles.append(step.name)


    def pick_possibles(self):
        return(min(self.possibles))


    def check_all(self):
        while len(self.step_list) < len(self.dic.keys()):
            # Check all values to see if requirement are met
            for keys, values in self.dic.items():
                self.check_before(values)
            # Select the minimum possible amongst all the possible step
            self.step_list.append(self.pick_possibles())
            # Reset possible list
            self.possibles = []

        return self.step_list, len(self.step_list)

    # Part 2
    def elf_times(self, elf_number, worktime):
        elf_set = set()
        for elf in range(elf_number):
            elf_set.add(Elf(elf))

        while len(self.step_list) < len(self.dic.keys()):
            # Check all values to see if requirement are met
            for keys, values in self.dic.items():
                self.check_before(values)
            # Check for work
            for elf in elf_set:
                if elf.step in self.possibles:
                    self.possibles.remove(elf.step)
            for elf in elf_set:
                if self.possibles != [] and elf.step == None:
                    elf.work(self.possibles.pop(0), worktime)
            # Working time
            flag = True
            while flag:
                self.total_time += 1
                for elf in elf_set:
                    if elf.step != None:
                        elf.time -= 1
                for elf in elf_set:
                    if elf.time == 0:
                        flag = False

            for elf in elf_set:
                if elf.time == 0:
                    self.step_list.append(elf.step)
                    elf.done()
            self.possibles = []

        return self.step_list, self.total_time


step_dic = get_input("Day_7_test")
answer = resolve_attempt(step_dic)
a, b = answer.check_all()
print("".join(a))

answer = resolve_attempt(step_dic)
print(answer.elf_times(2, 0))

step_dic = get_input("Day_7_input")
answer = resolve_attempt(step_dic)
a, b = answer.check_all()
print("".join(a))

answer = resolve_attempt(step_dic)
print(answer.elf_times(4, 60))