my_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
# 1 вариант
new_list_1 = []
new_list = [new_list_1.append(n) for n in my_list if n not in new_list_1]

# 2 вариант, по сути тоже самое
def sort_list():
    new_list_2 = []
    for i in my_list:
        if i not in new_list_2:
            new_list_2.append(i)
    return new_list_2

print(new_list_1)
print(sort_list())
