def get_file(name):
    file_list = []
    file = open(name, "r")
    for x in file:file_list.append(x)
    file.close()
    return file_list

input = get_file('Day_2_input')

def repeat(word):
    answer_dic = {'3': 0, '2': 0}
    for letter1 in word:
        count = 0
        for letter2 in word:
            if letter1 == letter2:
                count += 1
        if count >= 3:
            answer_dic['3'] += 1
        if count == 2:
            answer_dic['2'] += 1
    return answer_dic['3'], answer_dic['2']

def get_repeat_list(input):
    two_and_3_list = []
    for words in input:
        a, b = repeat(words)
        if a >= 1: two_and_3_list.append(3)
        if b >= 1: two_and_3_list.append(2)
    return two_and_3_list

def checksum(list):
    count_of_2 = 0
    count_of_3 = 0
    for item in list:
        if item == 2: count_of_2 += 1
        if item == 3: count_of_3 += 1
    print(str(count_of_2)+'*'+str(count_of_3)+'='+str(count_of_2*count_of_3))

test_list = ['abcdef','bababc', 'abbcde','abcccd', 'aabcdd','abcdee' ,'ababab']
checksum(get_repeat_list(test_list))
checksum(get_repeat_list(input))

#Part 2

def common_letter(word1, word2):
    count = 0
    for idx, letter in enumerate(word1):
        if letter != word2[idx]:
            count += 1
            if count > 1: break
    if count == 1:
        return word1, word2
    return 'none'
def check_whole_input(input):
    for words in input:
        for word in input:
            a = common_letter(words, word)
            if a != 'none':
                return(words, word)
def answer(word1, word2):
    answer = []
    for idx, letter in enumerate(word1):
        if letter == word2[idx]:
            answer.append(letter)
    print(''.join(answer))
a, b = check_whole_input(input)

answer(a, b)