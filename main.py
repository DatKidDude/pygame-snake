import pygame 
from snake import Snake
from food import Food
import game_functions as gf


def main():

    # Constants
    SCREEN_WIDTH = 800
    SCREEN_HEIGHT = 800
    SCREEN_BG = (0, 0, 0) 
    FPS = 144
    SNAKE_SIZE = 20

    # Initialize pygame
    pygame.init()
    # Initialize pygame Clock
    clock = pygame.time.Clock()
    # Number of ms since pygame.init() was called
    start_time = pygame.time.get_ticks()
    
    # Create the screen and set the title
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Snek")

    # Initialize snake instance
    snake = Snake(screen, start_time, SNAKE_SIZE)

    # Initialize food instance
    apple = Food(screen, SNAKE_SIZE)

    # main game loop
    while not gf.game_over(snake):
        # Check mouse and keyboard events
        gf.check_events(snake)
        # Check gameplay events like game over or if the snake collided with the food   
        gf.check_gameplay_events(snake, apple)
        # Update and display screen content
        gf.update_screen(snake, apple, screen, SCREEN_BG, clock, FPS)

if __name__ == "__main__":
    main()


