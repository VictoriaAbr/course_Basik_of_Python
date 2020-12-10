# 1 вариант
# user_list = []
# n = int(input('Введите количество элементов в списке: '))
# for i in range(n):
#     i = int(input('введите число: '))
#     user_list.append(i)
#     n += 1
# print(user_list)
# if len(user_list)%2 == 0:
#     user_list[::2], user_list[1::2] = user_list[1::2], user_list[::2]
# if len(user_list) % 2 != 0:
#     user_list[:-1:2], user_list[1:-1:2] = user_list[1:-1:2], user_list[:-1:2]
#
# print(user_list)

# 2 вариант
# user_list = list(input('Введите элементы без пробелов: '))
# for i in range(1, len(user_list), 2):
#     user_list[i - 1], user_list[i] = user_list[i], user_list[i - 1]
#
# print(user_list)

# 3 вариант
# user_list = input('Введите элементы с пробелами: ').split()
# print(user_list)
#
# idx = len(user_list) if len(user_list)%2 == 0 else len(user_list) - 1
# user_list[:idx:2], user_list[1:idx:2] = user_list[1:idx:2], user_list[:idx:2]
# print(user_list)

# 4 вариант
user_list = input('Введите элементы с пробелами: ').split()

for i in range(1, len(user_list), 2):
    user_list.insert(i - 1, user_list.pop(i))
print(user_list)
