my_list = [7, 5, 3, 3, 2]
new_el = int(input('Введите число: '))

for i in my_list:
    if new_el > i:
        my_list.insert(my_list.index(i), new_el)
        break
    if new_el == i:
        my_list.insert(my_list.index(i)+1, new_el)
        break
    if new_el < i:
        my_list.append(new_el)
        break
print(my_list)