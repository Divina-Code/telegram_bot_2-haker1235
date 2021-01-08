from random import randint


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


class Archer(Warrior):
    def __init__(self, name, hp, damage, life, bow):
        super().__init__(name, hp, damage, life)
        self.bow = bow

    def shoot(self):
        print("shooting")


snaiper = Archer("Snaiper", 100, randint(5, 15), True, 56)
karl = Warrior("Karl", 100, randint(5, 15), True)
gerakl = Warrior("Gerakl", 100, randint(5, 15), True)

print(karl.name, "hp =", karl.hp, "damage =", karl.damage, "life =", karl.life)
print(gerakl.name, "hp =", gerakl.hp, "damage =", gerakl.damage, "life =", gerakl.life)
print(snaiper.name, "hp =", snaiper.hp, "damage =", snaiper.damage, "life =", snaiper.life, "bows =", snaiper.bow)
# while karl.life and gerakl.life:

# сражение
# karl.take_damage(gerakl.damage)
# print("Karl hp =", karl.hp)
# gerakl.take_damage(karl.damage)
# print("Geracl hp =", gerakl.hp)

# плюс хп за покушать
# karl.hp += randint(2, 5)
# print("Karl hp =", karl.hp)

# gerakl.hp += randint(2, 5)
# print("Geracl hp =", gerakl.hp)

# баф урона

# karl.damage += randint(2, 5)
# print("Karl damage =", karl.damage)

# gerakl.damage += randint(2, 5)
# print("Karl damage =", karl.damage)

# проверка кто проиграл
# if karl.hp <= 0:
# karl.life = False
# print("Karl lost")

# if gerakl.hp <= 0:
# gerakl.life = False
# print("Geracl lost")
