my_list = [7, 5, 3, 3, 2]
new_el = float(input('Введите число: '))

i = 0
for n in my_list:
    if new_el <= n:
        i += 1
my_list.insert(i, float(new_el))
print(my_list)
