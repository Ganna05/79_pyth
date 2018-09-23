# Задача - 1
# Опишите несколько классов TownCar, SportCar, WorkCar, PoliceCar
# У каждого класса должны быть следующие аттрибуты:
# speed, color, name, is_police - Булево значение.
# А так же несколько методов: go, stop, turn(direction) - которые должны сообщать,
#  о том что машина поехала, остановилась, повернула(куда)

# Задача - 2
# Посмотрите на задачу-1 подумайте как выделить общие признаки классов
# в родительский и остальные просто наследовать от него.

class Car():
    def __init__(self, speed=0, color='Black', name='Noname', is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self._is_police = is_police

    def go(self):
        print('Машина поехала')

    def stop(self):
        print('Остановилась')

    def turn(self, direction):
        if direction == '6':
            print('Повернула направо')
        elif direction == '4':
            print('Повернула налево')


class TownCar(Car):
    pass


class SportCar(Car):
    pass


class WorkCar(Car):
    pass


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police=True):
        super(PoliceCar, self).__init__(speed, color, name, is_police=True)


town_car = TownCar(100, 'red', '1051f')
print(town_car.name)
police_car1 = PoliceCar(100, 'red', '101F')
print(police_car1._is_police)
car1 = Car(200, 'black', '15d')

#
# do = {
#     '8': car1.go,
#     '2': car1.stop,
#     '6': car1.turn,
#     '4': car1.turn
# }
#
# while True:
#     action = input('Задайте действие: ')
#     if action == '6' or action == '4':
#         do[action](action)
#     elif do.get(action):
#         do[action]()
#     elif action == 'q':
#         print('Выход из игры.')
#         break
#     else:
#         print('Задано некорректное действие, машина остановлена. \n')
