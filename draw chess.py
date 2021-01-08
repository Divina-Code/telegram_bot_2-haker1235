import pygame as pg

gamedisplay = pg.display.set_mode((500, 500))
pg.display.set_caption("Snowmens.py")
gamedisplay.fill((0, 0, 0))

radius = 17

# colors
WHITE = (255, 255, 255)
RED = (200, 10, 10)


fonte = pg.font.Font(None, 39)
text_img = fonte.render("Hello its label!", True, WHITE)

def draw_chess(x, y):
    s_x = 100
    s_y = 100
    SIZE = 19

    for g in range(x):
        if g % 2:
            pg.draw.rect(gamedisplay, WHITE, ((s_x + g * SIZE, s_y, SIZE, SIZE)))
        else:
            pg.draw.rect(gamedisplay, RED, ((s_x + g * SIZE, s_y, SIZE, SIZE)))

game = True
while game:
    for g in pg.event.get():
        if g.type == pg.QUIT:
            game = False

    gamedisplay.blit(text_img)
    draw_chess(9, 9)

    pg.display.update()

pg.quit()
