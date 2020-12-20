with open('1_1.txt', 'r', encoding='utf-8') as file_1:
    lines = 0
    for line in file_1:
        lines += 1
        print(f'Слов в {lines}-ой строке: {len(line.split())}')