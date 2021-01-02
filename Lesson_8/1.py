class Data:
    def __init__(self, date, month, year):
        self.date = date
        self.month = month
        self.year = year

    @classmethod
    def set_numb(cls, data):
        d, m, y = map(int, data)
        return cls(d, m, y)

    @staticmethod
    def validation_n(obj):
        if obj.date > 31 or obj.date <= 1:
            print('Введите корректную дату')
        elif obj.month > 13 or obj.date < 1:
            print('Введите корректную дату')
        if obj.year > 2020:
            print('Введите корректную дату')



my_date = '29-12-2020'
my_list = (my_date.split('-'))

my_1 = Data.set_numb(my_list)
Data.validation_n(my_1)
