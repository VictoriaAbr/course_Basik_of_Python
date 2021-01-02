class AllStuff:
    all_store_full = []


class Warehouse(AllStuff):
    def __init__(self, *args):
        try:
            self.name = input(f'Имя: ')
            self.color = input('Цвет: ')
            self.price = int(input('Цена: '))
            self.all_store = []
            self.all_units = {'имя': self.name, 'цвет': self.color, 'цена': self.price}
        except:
            print('Ошибка ввода данных цена')

    def __str__(self):
        try:
            return f'{self.name}: цвет - {self.color}, цена - {self.price}'
        except:
            pass

    def stuff(self):
        try:
            units = {'имя': self.name, 'цвет': self.color, 'цена': self.price}
            self.all_units.update(units)
            self.all_store.append(self.all_units)
            self.all_store_full.append(self.all_store)
            print(self.all_store_full)
        except:
            pass


class Printer(Warehouse):
    country_of_prod = 'China'
    def to_print(self):
        return 'print it'


class Scanner(Warehouse):
    year_of_birth = 2010
    def to_scan(self):
        return 'scan it'


class Xerox(Warehouse):
    place_for_stay = 'Table'
    def to_copy(self):
        return 'copy it'

unit_1 = Printer()
unit_1.stuff()
try:
    print(unit_1)
except:
    pass
unit_2 = Scanner()
unit_2.stuff()
print(unit_2.to_scan())