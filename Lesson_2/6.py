pr_list = []
all_dict = {}
end_dict = {'название': [], 'цена': [], 'количество': [], 'ед': []}
n = 0
i = None
while True:
    n += 1
    close = input('Если выход - Y: ')
    if close == 'Y':
        break
    pr_name = input('Название: ')
    pr_price = input('Введите цену товара: ')
    pr_quantity = input('Введите количество товара: ')
    pr_unit = input('Введите единицу измерения товара: ')
    pr_dict = {'название': pr_name, 'цена': pr_price, 'количество': pr_quantity, 'ед': pr_unit}
    pr_trt = (n, {'название': pr_name, 'цена': pr_price, 'количество': pr_quantity, 'ед': pr_unit})
    pr_list.append(pr_trt)
    all_dict[n] = pr_dict
    for key in end_dict:
        end_dict[key].append(pr_dict.get(key))
print(pr_list)
print(all_dict)
print(end_dict)

# for key in all_dict.keys():
#     print(key, ':', all_dict[key])
