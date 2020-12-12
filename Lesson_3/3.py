int_list = []
end_list = []
n_1 = int(input('Число: '))
n_2 = int(input('Число: '))
n_3 = int(input('Число: '))
def my_func(n_1, n_2, n_3):
    int_list.append(n_1)
    int_list.append(n_2)
    int_list.append(n_3)
    while True:
        end_list.append(max(int_list))
        int_list.remove(max(int_list))
        if len(end_list) == 2:
            break
    return(sum(end_list))

print(my_func(n_1, n_2, n_3))