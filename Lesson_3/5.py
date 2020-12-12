summa = []
print('Если хотите завершить, введите q: ')
while True:
    user_list = input('Введите числа ч/з пробел: ').split(' ')
    if 'q' in user_list:
        user_list.remove('q')
        int_list = [int(i) for i in user_list]
        summa.append(sum(int_list))
        print(sum(summa))
        break
    int_list = [int(i) for i in user_list]
    summa.append(sum(int_list))
    print(sum(summa))
