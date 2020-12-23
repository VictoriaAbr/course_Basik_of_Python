class Car:
    def __init__(self, s, c, n, i_p):
        self.speed = s
        self.color = c
        self.name = n
        self.is_police = i_p

    def go(self):
        print('Поехала!')

    def stop(self):
        print('Остановилась!')

    def turn(self, direction):
        print(f'Повернула на {direction}')

    def show_speed(self):
        print(f'Скорость - {self.speed}')


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print(f'{self.speed} - cкорость превышена!')


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print(f'{self.speed} - cкорость превышена!')


class PoliceCar(Car):
    pass


print(('*') * 50)

print('Town Car')
t_c = TownCar(55, 'black', 'Mazda', False)
t_c.go()
t_c.turn('право')
t_c.stop()
t_c.show_speed()
print(('*') * 50)

print('Sport Car')
s_c = SportCar(150, 'red', 'Porsche', False)
s_c.go()
s_c.turn('лево')
s_c.stop()
s_c.show_speed()
print(('*') * 50)

print('Work Car')
w_c = WorkCar(45, 'grey', 'Volvo', False)
w_c.go()
w_c.turn('право')
w_c.stop()
w_c.show_speed()
print(('*') * 50)

print('Police Car')
p_c = PoliceCar(60, 'white', 'Lada', True)
p_c.go()
p_c.turn('право')
p_c.stop()
p_c.show_speed()