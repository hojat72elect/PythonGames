"""
Iterates over each pixel in the screen, setting its color according to its coordinates.
Going from left to right, the red channel of the color increases.
And going from top to bottom, green increases.
"""

import pygame

pygame.init()
screen_width: int = 1000
screen_height: int = 800
screen: pygame.Surface | pygame.SurfaceType = pygame.display.set_mode((screen_width, screen_height))

done: bool = False
while not done:
    for game_event in pygame.event.get():
        if game_event.type == pygame.QUIT:
            done = True

    for y in range(screen_height):
        for x in range(screen_width):
            screen.set_at((x, y), pygame.Color(int(x / screen_width * 255), int(y / screen_height * 255), 255))

    pygame.display.update()

pygame.quit()
