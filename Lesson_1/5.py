proceeds = int(input('Значение выручки: '))
costs = int(input('Значение издержек: '))

if proceeds > costs:
    print('вы в прибыли')
    profit = proceeds - costs
    print(f'вы заработали {profit}')
    print(f'рентабельность: {proceeds / profit:.2f}')
    numb_empl = int(input('Сколько у вас сотрудников? '))
    profit_per_empl = profit / numb_empl
    print(f'прибыль на 1 сотрудника: {profit_per_empl:.2f}')
elif proceeds == costs:
    print('вы отрабртали в 0')
else:
    lesion = costs - proceeds
    print(f'вы в убытке на {lesion:.2f}')