# Задача - 1
# Вам необходимо создать завод по производству мягких игрушек для детей.
# Вам надо продумать структуру классов,
# чтобы у вас был класс, который создает игрушки на основании:
#  Названия, Цвета, Типа (животное, персонаж мультфильма)
# Опишите процедуры создания игрушки в трех методах:
# -- Закупка сырья, пошив, окраска
# Не усложняйте пусть методы просто выводят текст о том, что делают.
# В итоге ваш класс по производству игрушек должен вернуть объект нового класса Игрушка.

# Задача - 2
# Доработайте нашу фабрику, создайте по одному классу на каждый тип, теперь надо в классе фабрика
# исходя из типа игрушки отдавать конкретный объект класса, который наследуется от базового - Игрушка

class Toy():
    def __init__(self, name, color, type=None):

        if name not in ['\n', '', ' ']:
            self.name = name
        else:
            self.name = 'без имени'
        if color not in ['\n', '', ' ']:
            self.color = color
        else:
            self.color = "белый"
        self.type = type

    def materials(self):
        print('Закупка сырья ')

    def sewing(self):
        print('Пошив ' + self.name + ' игрушки свободного покроя')

    def coloring(self):
        print('Окраска игрушки ' + self.name + ' игрушки свободного покроя в ' + self.color + ' цвет.  ')


class ToyAnimal(Toy):
    def materials(self):
        print('Закупка сырья для игрушки типа "Животное" ')

    def sewing(self):
        print('Пошив игрушки ' + self.name + ' типа "Животное" ')

    def coloring(self):
        print('Окраска игрушки ' + self.name + ' типа "Животное" в ' + self.color + ' цвет.  ')


class ToyAnimation(Toy):
    def materials(self):
        print('Закупка сырья для игрушки типа "Персонаж мультфильма" ')

    def sewing(self):
        print('Пошив игрушки ' + self.name + ' типа "Персонаж мультфильма" ')

    def coloring(self):
        print('Окраска игрушки ' + self.name + ' типа "Персонаж мультфильма" в ' + self.color + ' цвет.  ')


class Production():
    def process(self, type):
        do = {
            '1': ToyAnimal,
            '2': ToyAnimation
        }
        if do.get(type):
            name = input("Имя игрушки:  ")
            color = input("Цвет игрушки: ")
            toy_maker = do[type](name, color, type)
            toy_maker.materials()
            toy_maker.sewing()
            toy_maker.coloring()
            print('Игрушка создана')
        else:
            print("Введены некорректные данные")


type = input('Введите тип игрушки для выпуска: \n'
             'для типа игрушки "Животное" = 1\n'
             'для типа игрушки "персонаж мультфильма" = 2\n')

ty = Production()
ty.process(type)

