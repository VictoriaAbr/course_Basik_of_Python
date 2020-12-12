x = abs(float(input('Число: ')))
y = abs(int(input('Отрицательная степень: ')))

# 1 вариант

def my_func_1(x, y):
    return (1 / (x ** y))

# 2 вариант
def my_func_2(x, y):
    i = 1
    result = 1
    while i <= y:
        result *= x
        i += 1
    end = 1 / result
    print(end)


print(my_func_1(x, y))
print('*' * 50)
my_func_2(x, y)
