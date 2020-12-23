class Road:

    def __init__(self, l, w):
        self._lenght = l
        self._width = w
    def massa_a(self):
        print(self._lenght * self._width * 25 * 0.005)


r_1 = Road(20, 5000)
r_1.massa_a()


