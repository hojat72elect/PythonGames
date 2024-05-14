import pygame
from pygame import Surface, SurfaceType

"""
Just draws a circle on the screen where mouse is clicked.
"""

window_size: tuple[int, int] = (500, 400)
screen: Surface | SurfaceType = pygame.display.set_mode(window_size)
run: bool = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONUP:
            position: tuple[int, int] = pygame.mouse.get_pos()
            color: tuple[int, int, int] = (255, 255, 255)
            pygame.draw.circle(screen, color, position, 10, 3)
            pygame.display.update()

        if event.type == pygame.QUIT:
            run = False

pygame.quit()
