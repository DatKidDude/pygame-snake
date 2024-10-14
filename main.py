import pygame 
import sys


def main():

    # Screen constants
    SCREEN_WIDTH = 800
    SCREEN_HEIGHT = 800
    SCREEN_BG = (51, 51, 51) 
    TILE_SIZE = 20
    
    # Initialize pygame
    pygame.init()

    # Create the screen and set the title
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Snek")
    screen.fill(SCREEN_BG)

    # Initialize pygame Clock
    clock = pygame.time.Clock()

    # Create the game grid (may change in the future)
    for row in range(SCREEN_HEIGHT // TILE_SIZE):
        for col in range(SCREEN_WIDTH // TILE_SIZE):
            pygame.draw.rect(
                screen,
                (178,34,34,250),
                pygame.Rect(col * TILE_SIZE, row * TILE_SIZE, TILE_SIZE, TILE_SIZE),
                1
            )

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
