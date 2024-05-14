import pygame
from pygame import Surface, SurfaceType, Rect
from pygame.key import ScancodeWrapper
from pygame.rect import RectType

"""
Our player is a square that moves around the screen with the arrow keys.
"""

pygame.init()
SCREEN_WIDTH: int = 800
SCREEN_HEIGHT: int = 600

screen: Surface | SurfaceType = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
player: Rect | RectType = pygame.Rect((300, 250, 50, 50))
run: bool = True
while run:
    screen.fill((0, 0, 0)) # refreshes the screen with color black
    pygame.draw.rect(screen, (255, 0, 0), player)
    key: ScancodeWrapper = pygame.key.get_pressed()
    if key[pygame.K_LEFT]:
        player.move_ip(-2, 0)
    if key[pygame.K_RIGHT]:
        player.move_ip(2, 0)
    if key[pygame.K_UP]:
        player.move_ip(0, -2)
    if key[pygame.K_DOWN]:
        player.move_ip(0, 2)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()
