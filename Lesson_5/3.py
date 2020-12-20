with open('3_1.txt', 'r', encoding='utf-8') as file_3:
    poor = [line.split()[0] for line in file_3 if int(line.split()[1]) < 20000]
    print(f'Оклад менее 20 тыс.: {", ".join(poor)}')
    file_3.seek(0)
    avg_income = [int(line.split()[1]) for line in file_3]
    print(f'Средний доход: {sum(avg_income)}')
