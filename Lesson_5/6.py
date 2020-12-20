import re

with open('6_1.txt', 'r', encoding='utf-8') as file_6:
    dict_l = {}
    for line in file_6:
        for i in line:
            nums = re.findall(r'\d+', line)
            nums = [int(i) for i in nums]
            word = re.compile(r'\w+')
            x = {word.findall(line)[0]: sum(nums)}
        dict_l.update(x)
    print(dict_l)