# user_str = input('Напишите несколько слов, разделенных пробелом: ')
# new_list = user_str.split(' ')
# for i in new_list:
#     print(new_list.index(i) + 1, i[:10])
#
# # ИЛИ
#
# for ind, i in enumerate(new_list):
#     print(ind + 1, i[:10])

# user_str = input('Напишите несколько слов, разделенных пробелом: ').split()
#
# for n, i in enumerate(user_str, 1):
#     print(n, i) if len(i) <= 10 else print(n, (i[:10]))

user_str = input('Напишите несколько слов, разделенных пробелом: ').split()

for i, word in enumerate(user_str, 1):
    print(f'{i} {word[:10]}')