def delenie_na_null(n_1, n_2):
    try:
        n_1 / n_2
        print(n_1 / n_2)
    except ZeroDivisionError as err:
        print(err)

delenie_na_null(int(input('1: ')), int(input('2: ')))