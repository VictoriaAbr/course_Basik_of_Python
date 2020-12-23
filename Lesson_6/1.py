import time

class TrafficLight:
    __color = 0

    def running(self):
        while True:
            print("\033[41m\033[30m RED")
            time.sleep(7)
            print('\033[43m\033[31m YELLOW')
            time.sleep(2)
            print('\033[42m\033[30m GREEN')
            time.sleep(5)
            print('\033[43m\033[30m YELLOW')
            time.sleep(2)


tl = TrafficLight()
tl.running()
