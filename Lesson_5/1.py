with open('1_1.txt', 'w', encoding='utf-8') as file_1:
    while True:
        data = (input('Введите данные: '))
        if data == '':
            break
        file_1.write(data + '\n')

