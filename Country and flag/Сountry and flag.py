import pygame
from random import choice

pygame.init()

gamedisplay = pygame.display.set_mode((800, 600))  # Создаём экран размером 800 на 600
pygame.display.set_caption("Guess the flag")  #Меняем заголовок окна
gamedisplay.fill((100, 100, 100))

def make_flag(image):
    img = pygame.image.load(image)  ##Загружаем картинку в програму
    img = pygame.transform.scale(img, (250, 180)) ##меняем размер картинки
    return img


countries = {
    "Russia": make_flag("img/Russia.png"),  #Слева от : находятся КЛЮЧИ(названия стран), справа - ЗНАЧЕНИЯ(картинки флагов)

    "Ukraine": make_flag("img/ukraine.jpg"),


}




game = True  # Продолжается игра или нет
while game:

    for e in pygame.event.get():  # берём события по одному
        if e.type == pygame.QUIT:
            game = False

    random_country = choice(list(countries.keys()))
    random_flag = countries[random_country]

    gamedisplay.blit(random_flag, (275, 210))
    pygame.display.update()
    user_answer = input("Name of country:\t")
    if user_answer == random_country:
        print("Correct")
    else:
        print("Incorrect")



pygame.quit()
