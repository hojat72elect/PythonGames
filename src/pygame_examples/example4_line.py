"""
First gets the position of cursor on the screen, then draws a line between the two points.
"""

import pygame

pygame.init()
screen_width: int = 1000
screen_height: int = 800
screen: pygame.Surface | pygame.SurfaceType = pygame.display.set_mode((screen_width, screen_height))

is_finished: bool = False
white = pygame.Color(255, 255, 255)
times_clicked: int = 0
point1: tuple[int, int] | None = None
point2: tuple[int, int] | None = None

while not is_finished:
    for game_event in pygame.event.get():
        if game_event.type == pygame.QUIT:
            is_finished = True
        elif game_event.type == pygame.constants.MOUSEBUTTONDOWN:
            if times_clicked == 0:
                point1 = pygame.mouse.get_pos()
            else:
                point2 = pygame.mouse.get_pos()
            times_clicked += 1
            if times_clicked > 1:
                pygame.draw.line(screen, white, point1, point2, 1)
                times_clicked = 0
    pygame.display.update()

pygame.quit()
