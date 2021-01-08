from random import randint, choice


class Warrior():
    def __init__(self, name, hp, damage, life):
        self.name = name
        self.hp = hp
        self.damage = damage
        self.life = life

    def take_damage(self, power):
        self.hp -= power

    def eat(self, food):
        self.hp += food

    def up(self, lvl):
        self.damage += lvl


karl = Warrior("Karl", 100, randint(5, 15), True)
gerakl = Warrior("Gerakl", 100, randint(5, 15), True)
print(karl)
print(gerakl)


