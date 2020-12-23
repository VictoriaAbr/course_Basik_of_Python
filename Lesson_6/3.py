class Worker:
    def __init__(self, n, s, wage, bonus, p='director'):
        self.data = [n, s, p]
        self.income = {"wage": wage, "bonus": bonus}


class Position(Worker):

    def get_full_name(self):
        self.data[0] = input('Имя: ')
        self.data[1] = input('Фамилия: ')

    def get_total_income(self):
        self.income['wage'] = input('Зарплата: ')
        self.income['bonus'] = input('Премия: ')
        print(self.income['wage'] + self.income['bonus'])


p_1 = Position('Alex', 'Smith', '50', '100')
print(p_1.data[0], p_1.data[1], p_1.income['wage'], p_1.income['bonus'])

p_1.get_full_name()
p_1.get_total_income()

print(p_1.data[0], p_1.data[1], p_1.income['wage'], p_1.income['bonus'])
print(income['wage'] + income['bonus'])
