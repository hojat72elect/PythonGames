"""
Draws several squares on the screen.
"""
from pygame import init, display, Color, draw, event, QUIT, SurfaceType, Surface

init()
screen_width: int = 900
screen_height: int = 500
screen: Surface | SurfaceType = display.set_mode((screen_width, screen_height))

is_finished: bool = False
white: Color = Color(255, 255, 255)


def draw_square(x: int, y: int, size: int):
    draw.rect(screen, white, (x, y, size, size))


while not is_finished:
    for game_event in event.get():
        if game_event.type == QUIT:
            is_finished = True

    draw_square(100, 100, 10)
    draw_square(121, 320, 20)
    draw_square(327, 324, 30)
    draw_square(691, 431, 40)
    draw_square(697, 317, 50)
    draw_square(626, 246, 60)
    draw_square(343, 212, 50)
    draw_square(653, 165, 40)
    draw_square(773, 102, 20)
    draw_square(822, 153, 30)
    display.update()

quit()
