user_str = input('Напишите несколько слов, разделенных пробелом: ')
new_list = user_str.split(' ')
for i in new_list:
    print(new_list.index(i) + 1, i[:10])

# ИЛИ

for ind, i in enumerate(new_list):
    print(ind + 1, i[:10])
