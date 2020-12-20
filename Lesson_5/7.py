import re
import json
all_profit = []
dict_pr = {}
with open('7_1.txt', 'r', encoding='utf-8') as file_7:
    for line in file_7:
        for i in line:
            nums = re.findall(r'[ ]\d+', line)
            nums = [int(i) for i in nums]
            profit = nums[0] - nums[1]
            word = re.compile(r'\w+')
            x = {word.findall(line)[0]: profit}
            if profit > 0:
                all_profit.append(profit)
        print(f'Прибыль компании: {profit}')
        dict_pr.update(x)
    avg_profit = sum(all_profit) / len(all_profit)
    print(f'Средняя прибыль: {avg_profit}')
print([dict_pr])
with open('7_2.json', 'w') as file_7_2:
    json.dump([dict_pr], file_7_2)
