import pygame


# Create the window
pygame.init()
screen_width: int = 1_000
screen_height: int = 800
screen: pygame.Surface | pygame.SurfaceType = pygame.display.set_mode((screen_width, screen_height))

is_finished: bool = False
white: pygame.Color = pygame.Color(255, 255, 255)

while not is_finished:
    for game_event in pygame.event.get():
        # Will close the window by clicking the close button
        if game_event.type == pygame.QUIT:
            is_finished = True
    # Sets a specific pixel to white
    screen.set_at((100, 400), white)
    # Updates the display screen
    pygame.display.update()

pygame.quit()
