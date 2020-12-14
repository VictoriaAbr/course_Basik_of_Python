from itertools import count
from itertools import cycle
from itertools import islice

# а ****************

# for n in count(int(input('Число: '))):
#     if n > 10:
#         break
#     print(n)
# print(('*') * 10)

# б.1 ****************

# c = 0
# for n in cycle('123'):
#     if c >= 3:
#         break
#     c += 1
#     print(n)
# print(('*') * 10)

# б.2 ****************

# iter = cycle(('1', '2', '3'))
# print(next(iter))
# print(next(iter))
# print(next(iter))

# а.1 без break ****************

# def func_count():
#     while True:
#         for n in count(9):
#             if n <= 10:
#                 print(n)
#         return
# print(func_count())

# а.2 без break ****************

# for n in islice(count(5), 6):
#         print(n)

# б без break ****************

# def func_cycle():
#     c = 0
#     while True:
#         for n in cycle(('1', '2', '3')):
#             if c < 4:
#                 print(n)
#                 c += 1
#         return
# print(func_cycle())

# а, б без break ****************

def f_is():
    list_ = []
    for n in islice(count(5), 6):
            list_.append(n)
    return(list_)

def func_c_c():
    c = 0
    while True:
        for i in cycle(f_is()):
            if c < 10:
                print(i)
                c += 1
        return
print(func_c_c())

# Также, думаю, можно использовать конструкцию try except