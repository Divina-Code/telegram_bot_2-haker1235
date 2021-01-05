import pygame
from random import randint

pygame.init()

gamedisplay = pygame.display.set_mode((800, 600) )

gamedisplay.fill((255, 255, 255))

radius = 5
color = (255, 0, 0)
game = True  #Продолжается игра или нет
while game:

    events = pygame.event.get() #Запрашиваем СОБЫТИЯ, произошедшие в игре

    for e in events:   #берём события по одному
        if e.type == pygame.QUIT:
            game = False



        if e.type == pygame.MOUSEBUTTONDOWN:
            if e.button == 4:
                radius += 1
            if e.button == 5:
                radius -= 1

            if e.button == 2:
                color = (randint(0, 255), randint(0, 255), randint(0, 255))


    if pygame.mouse.get_pressed()[0]:
        mousepose = pygame.mouse.get_pos()
        pygame.draw.circle(gamedisplay, color, mousepose, radius)

    if pygame.mouse.get_pressed()[2]:
        mousepose = pygame.mouse.get_pos()
        pygame.draw.circle(gamedisplay, (255, 255, 255), mousepose, radius)

    pygame.display.update()
pygame.quit()
