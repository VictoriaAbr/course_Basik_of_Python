def f_fact(n):
    per = 1
    for i in range(1, n + 1):
        per = per * i
        yield f'{i}! = {per}'

for el in f_fact(4):
    print(el)
