from random import randint

class Warrior():

    def __init__(self, name, hp, damage, life, strength):
        self.name = name
        self.hp = hp
        self.damage = damage
        self.life = life
        self.strength = strength

    def take_damage(self, power):
        self.hp -= power

    def eat(self, food):
        self.hp += food

    def up(self, lvl):
        self.damage += lvl


class Archer(Warrior):
    def __init__(self, name, hp, damage, life, bow):
        super().__init__(name, hp, damage, life, bow)
        self.bow = bow

    def shoot(self):
        print("shooting")


snaiper = Archer("Snaiper", 100, randint(5, 15), True, randint(10, 50))
karl = Warrior("Karl", 100, randint(5, 15), True, randint(10, 50))
gerakl = Warrior("Gerakl", 100, randint(5, 15), True, randint(10, 50))

print(karl.name, "hp =", karl.hp, "damage =", karl.damage, "life =", karl.life, "strength =", karl.strength)
print(gerakl.name, "hp =", gerakl.hp, "damage =", gerakl.damage, "life =", gerakl.life, "strength =", gerakl.strength)
print(snaiper.name, "hp =", snaiper.hp, "damage =", snaiper.damage, "life =", snaiper.life, "bows =", snaiper.bow)
while karl.life and gerakl.life and snaiper.life:

    # сражение

    if gerakl.strength and snaiper.bow >= 1:
        karl.take_damage(gerakl.damage + snaiper.damage)
        print("Karl hp =", karl.hp)
        gerakl.strength -= 1
        snaiper.bow -= 1

    if karl.strength and snaiper.bow >= 1:
        gerakl.take_damage(karl.damage + snaiper.damage)
        print("Geracl hp =", gerakl.hp)
        karl.strength -= 1
        snaiper.bow -= 1

    if karl.strength and gerakl.strength >= 1:
        snaiper.take_damage(karl.damage + gerakl.damage)
        print("Snaiper hp =", snaiper.hp)
        karl.strength -= 1
        gerakl.strength -= 1

    # плюс хп за покушать
    karl.hp += randint(2, 5)
    print("Karl hp =", karl.hp)

    gerakl.hp += randint(2, 5)
    print("Geracl hp =", gerakl.hp)

    snaiper.hp += randint(2, 5)
    print("Snaiper hp =", snaiper.hp)

    # проверка кто проиграл
    if karl.hp <= 0:
        karl.life = False
        print("Karl lost")

    if gerakl.hp <= 0:
        gerakl.life = False
        print("Geracl lost")

    if snaiper.hp <= 0:
        gerakl.hp = False
        print("Snaiper lost")

    print("*" * 20)
    print(karl.name, "hp =", karl.hp, "damage =", karl.damage, "life =", karl.life, "strength =", karl.strength)
    print(gerakl.name, "hp =", gerakl.hp, "damage =", gerakl.damage, "life =", gerakl.life, "strength =",
          gerakl.strength)
    print(snaiper.name, "hp =", snaiper.hp, "damage =", snaiper.damage, "life =", snaiper.life, "bows =", snaiper.bow)
    print("*" * 20)
