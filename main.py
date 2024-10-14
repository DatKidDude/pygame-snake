import pygame 
import sys


def main():

    # Screen constants
    SCREEN_WIDTH = 800
    SCREEN_HEIGHT = 800
    SCREEN_BG = (51, 51, 51) 
    
    # Initialize pygame
    pygame.init()

    # Create the screen and set the title
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Snek")
    screen.fill(SCREEN_BG)

    # Initialize pygame Clock
    clock = pygame.time.Clock()

    # main game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        # Update screen
        pygame.display.flip()

        # Set FPS to 144
        clock.tick(144)


if __name__ == "__main__":
    main()
