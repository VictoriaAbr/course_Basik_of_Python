class MyException(Exception):
    def __init__(self, txt):
        self.txt = txt

numb = []
while True:
    n = input('Данные: ')
    if n == 'q':
        print(numb)
        break
    try:
        if n.isdigit() == False:
            raise MyException('Это не число')
        else:
            numb.append(n)
    except MyException as err:
        print(err)
