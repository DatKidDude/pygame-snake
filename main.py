import pygame 
from snake import Snake
import game_functions as gf
        

def main():

    # Constants
    SCREEN_WIDTH = 800
    SCREEN_HEIGHT = 800
    SCREEN_BG = (0, 0, 0) 
    FPS = 240

    # Initialize pygame
    pygame.init()
    # Initialize pygame Clock
    clock = pygame.time.Clock()
    # Number of ms since pygame.init() was called
    start_time = pygame.time.get_ticks()
    
    # Create the screen and set the title
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Snek")

    snake = Snake(screen, start_time)

    # main game loop
    while True:
        # Check mouse and keyboard events
        gf.check_events(snake)
        # Update and display screen content
        gf.update_screen(snake, screen, SCREEN_BG, clock, FPS)


if __name__ == "__main__":
    main()


