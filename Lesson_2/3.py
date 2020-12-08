dict_month = {
    '1': 'зима', '2': 'зима', '3': 'весна', '4': 'весна', '5': 'весна', '6': 'лето', '7': 'лето',
    '8': 'лето', '9': 'осень', '10': 'осень', '11': 'осень', '12': 'зима'
}
user_month = (input('Введите месяц: '))
print(dict_month[user_month])

list_month = ['зима', 'весна', 'лето', 'оcень']
user_month = int(input('Введите месяц: '))
if user_month <= 3 or user_month == 12:
    print(list_month[0])
elif user_month >= 3 or user_month <= 5:
    print(list_month[1])
elif user_month >= 6 or user_month <= 8:
    print(list_month[2])
elif user_month >= 9 or user_month <=11:
    print(list_month[3])