class MyException(Exception):
    def __init__(self, txt):
        self.txt = txt

try:
    n = int(input('Введите число: '))
    if n == 0:
        raise MyException('Делить на 0 нельзя!')
    res = 2 / n
except MyException as err:
    print(err)
else:
    print(res)
