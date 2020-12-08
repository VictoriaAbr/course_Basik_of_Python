user_list = []
n = int(input('Введите количество элементов в списке: '))
for i in range(n):
    i = int(input('введите число: '))
    user_list.append(i)
    n += 1
print(user_list)
if len(user_list)%2 == 0:
    user_list[::2], user_list[1::2] = user_list[1::2], user_list[::2]
if len(user_list) % 2 != 0:
    user_list[:-1:2], user_list[1:-1:2] = user_list[1:-1:2], user_list[:-1:2]

print(user_list)
