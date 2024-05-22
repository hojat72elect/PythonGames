import pygame
from pygame import Surface, SurfaceType, Color, display, quit, event, QUIT

# Create the window
pygame.init()
screen_width: int = 1_000
screen_height: int = 800
screen: Surface | SurfaceType = display.set_mode((screen_width, screen_height))

is_finished: bool = False
white: Color = Color(255, 255, 255)

while not is_finished:
    for game_event in event.get():
        # Will close the window by clicking the close button
        if game_event.type == QUIT:
            is_finished = True
    # Sets a specific pixel to white
    screen.set_at((100, 400), white)
    # Updates the display screen
    display.update()

quit()
