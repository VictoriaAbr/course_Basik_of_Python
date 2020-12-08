my_list = [
    2, 'hello', [2, 3], 4.5, ('one', 'two'), {'1': 'one', '2': 'two'}, set('trampapam'), (b'digit'), bytearray(b'digits'), (None), #(1/0)
]

for i in my_list:
    print(type(i))