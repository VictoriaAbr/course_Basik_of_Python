dict_n = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
def replace_f(target_n, dict_n):
    for i, j in dict_n.items():
        target_n = target_n.replace(i, j)
    return target_n
with open('4_1.txt', 'r', encoding='utf-8') as file_4:
    with open('4_2.txt', 'w', encoding='utf-8') as file_4_2:
        for line in file_4:
            file_4_2.writelines(replace_f(line, dict_n))
