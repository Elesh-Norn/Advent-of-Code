input_range = 746325 - 264360
good_password = 0
password = 264360
for x in range(input_range):
    password += 1
    good = True
    passlist = []
    dico_occurence = {}
    first = False
    for i, z in enumerate(list(str(password))):
        passlist.append(int(z))
        if int(z) not in dico_occurence:
            dico_occurence[int(z)] = 1
        else:
            dico_occurence[int(z)] += 1
        if first:
            if int(z) < passlist[i - 1]:
                good = False
                break
        else:
            first = True

    if good:
        # Part 2 line
        if 2 in dico_occurence.values():
            good_password += 1

print(good_password)