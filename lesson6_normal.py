# Задача - 1
# Ранее мы с вами уже писали игру, используя словари в качестве
# структур данных для нашего игрока и врага, давайте сделаем новую, но уже с ООП
# Опишите базовый класс Person, подумайте какие общие данные есть и у врага и у игрока
# Не забудьте, что у них есть помимо общих аттрибутов и общие методы.
# Теперь наследуясь от Person создайте 2 класса Player, Enemy.
# У каждой сущности должы быть аттрибуты health, damage, armor
# У каждой сущности должно быть 2 метода, один для подсчета урона, с учетом брони противника,
# второй для атаки противника.
# Функция подсчета урона должна быть инкапсулирована
# Вам надо описать игровой цикл так же через класс.
# Создайте экземпляры классов, проведите бой. Кто будет атаковать первым оставляю на ваше усмотрение.
import random


class Person:
    def __init__(self, name, health=100, damage=50, armor=0.7):
        self.name = name
        self.health = health
        self.damage = damage
        self.armor = armor

    # Функция для подсчета урона
    def _calculate_damage(self, damage, armor):
        return damage // armor

    # Функция атаки, принимает на вход 2 структуры
    def attack(self, who_attack, who_defend):
        damage = self._calculate_damage(who_attack.damage, who_defend.armor)
        who_defend.health -= damage
        print('{} нанес {} урона {}, у того осталось {} жизней.'.format(who_attack.name, who_defend.name, damage,
                                                                        who_defend.health))


class Player(Person):
    pass


class Enemy(Person):
    pass


class Battle():
    def start_game(self, player, enemy):
        print('Вступили в бой: ' + player.name + ' против ' + enemy.name)
        battle_list = [player, enemy] # для выбора того, кто нанесет первый удар
        print(player.name, player.health, player.damage, player.armor)
        print(enemy.name, enemy.health, enemy.damage, enemy.armor)
        # Запоминаем кто последний атаковал
        last_attacker = random.choice(battle_list)
        # print(last_attacker.name)

        while player.health > 0 and enemy.health > 0:
            if last_attacker == player:
                enemy.attack(enemy, player)
                last_attacker = enemy
            else:
                player.attack(player, enemy)
                last_attacker = player
            last_attacker = random.choice(battle_list)  # для элемента случайности нанесения удара - можно удалить, для получения поочередных ударов
        if player.health > 0:
            print('Игрок победил!')
        else:
            print('Враг победил!')


# получаем наши структуры, через вышеописанную функцию
count_pl = 10
player_list = [Player("P-"+str(i+1), random.randrange(10, 100, 10), random.randrange(10, 50, 10)) for i in range(count_pl)]
for player in player_list:
    print(player.name, player.health, player.damage, player.armor)

count_en = 10
enemy_list = [Enemy("E-"+str(i+1), random.randrange(10, 100, 10), random.randrange(10, 50, 10)) for i in range(count_en)]
for enemy in enemy_list:
    print(enemy.name, enemy.health, enemy.damage, enemy.armor)

player = random.choice(player_list)
enemy = random.choice(enemy_list)

battle1 = Battle()
battle1.start_game(player, enemy)
