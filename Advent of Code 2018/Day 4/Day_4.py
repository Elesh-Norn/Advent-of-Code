
def get_input(filename):
    file = open(filename, "r")
    guard_set = set()
    for line in file:
        guard_set.add(line)
    file.close()
    return guard_set


def guard_logs(line_list):
    guard = None
    id_set = set()
    guard_dic = {}
    sleep_start = int()
    sleep = True

    for line in line_list:
        if line.split(" ")[2] == 'Guard':
            guard = line.split(" ")[3].replace("#", "")

            if guard not in id_set:
                id_set.add(guard)
                guard_dic[guard] = {'sleep_log': {}, 'sleep_total': 0}

            if sleep:
                sleep = False
                sleep_time = int(line.split(" ")[1][3:5]) - sleep_start
                guard_dic[guard]['sleep_total'] += sleep_time

                for minutes in range(sleep_start, int(line.split(" ")[1][3:5])):
                    if minutes in guard_dic[guard]['sleep_log']:
                        guard_dic[guard]['sleep_log'][minutes] += 1
                    else:
                        guard_dic[guard]['sleep_log'][minutes] = 1

        if line.split(" ")[2] == 'falls':
            sleep = True
            sleep_start = int(line.split(" ")[1][3:5])

        if line.split(" ")[2] == 'wakes':
            sleep = False
            sleep_time = int(line.split(" ")[1][3:5]) - sleep_start
            guard_dic[guard]['sleep_total'] += sleep_time
            for minutes in range(sleep_start, (int(line.split(" ")[1][3:5]))):
                if minutes in guard_dic[guard]['sleep_log']:
                    guard_dic[guard]['sleep_log'][minutes] += 1
                else:
                    guard_dic[guard]['sleep_log'][minutes] = 1
    return guard_dic


def find_guard_sleeping_the_most(guard_dictionary):
    guard_list = []
    guard_sleep = []

    for key, values in guard_dictionary.items():
        guard_list.append(key)
        guard_sleep.append(values['sleep_total'])

    return guard_list[guard_sleep.index(max(guard_sleep))]


def find_most_slept_min(dic):
    return max(zip(dic.values(), dic.keys()))


logs = sorted(get_input("Day_4_input"))
logs = guard_logs(logs)


# Part 1
answer_guard = find_guard_sleeping_the_most(logs)
answer_minute = find_most_slept_min(logs[answer_guard]['sleep_log'])
print('Guard is', answer_guard, 'Minute is', answer_minute[1])
print('Part 1 answer is:', int(answer_guard) * answer_minute[1])

# Part 2
def find_the_lazy_min(guard_dic):
    lazy_dic = {}
    guard = 0
    minute = 0
    time_slept = 0
    for key, values in guard_dic.items():
        if guard_dic[key]['sleep_log'] != {}:
            lazy_dic[key] = find_most_slept_min(guard_dic[key]['sleep_log'])

    for key, values in lazy_dic.items():
        if values[0] > time_slept:
            guard = key
            minute = values[1]
            time_slept = values[0]

    return [guard, minute, time_slept]


lazy = find_the_lazy_min(logs)

print("")
print('Guard is ', lazy[0], 'Minute is', lazy[1], 'for', lazy[2])
print('Answer is', int(lazy[0])*lazy[1])
