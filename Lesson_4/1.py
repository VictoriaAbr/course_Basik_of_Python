from sys import argv

script, production, rate, prize = argv

print('Выработка в часах: ', production)
print('Ставка в час: ', rate)
print('Премия: ', prize)

wage = int(production) * int(rate) + int(prize)
print('Заработная плата: ', wage)