class Cell:

    def __init__(self, cell):
        self.cell = cell

    def __add__(self, other):
        return self.cell + other.cell

    def __sub__(self, other):
        sub = self.cell - other.cell
        if sub > 0:
            return sub
        else:
            return 'Разница меньше 0'

    def __mul__(self, other):
        return self.cell * other.cell

    def __floordiv__(self, other):
        return self.cell // other.cell

    def make_order(self, n):
        c_len = self.cell
        while True:
            if c_len >= n:
                c_len -= n
                print(('*') * n)
            else:
                print(('*') * c_len)
                break


cell_1 = Cell(12)
cell_2 = Cell(13)
print(cell_1 // cell_2)
cell_1.make_order(5)
