import threading
import time


class Knight(threading.Thread):
    counter = 0
    def __init__(self, name, power):
        threading.Thread.__init__(self)
        self.name = name
        self.power = power

    def timer(self, name, power):
        warrior = 100

        while warrior > 0:
            time.sleep(1)
            warrior -= power
            self.counter += 1
            print(f"{self.name} сражается {self.counter} день(дня)..., осталось {warrior} воинов.\n")

    def run(self):
        print(f"{self.name}, на нас напали!")
        self.timer(self.name, self.power)
        print(f'{self.name} одержал победу спустя {self.counter} дней(дня)!')

first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)
first_knight.start()
second_knight.start()
first_knight.join()
second_knight.join()
print('Все битвы закончились!')