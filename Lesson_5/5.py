import re
with open('5_1.txt', 'w', encoding='utf-8') as file_5:
    list_n = str(input('Числа ч/з пробел: ').split(' '))
    file_5.write(list_n)
    print(list_n)
    int_l = []
    for i in list_n:
        nums = re.findall(r'\d+', list_n)
        nums = [int(i) for i in nums]
    print(sum(nums))