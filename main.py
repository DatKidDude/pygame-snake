import pygame 
import sys

            
def draw_grid(screen):
    """Draws the game grid to the screen"""
    TILE_SIZE = 20
    for row in range(0, screen.get_width(), TILE_SIZE): 
        for col in range(0, screen.get_height(), TILE_SIZE):
            pygame.draw.rect(
                screen, 
                (51, 51, 51), 
                pygame.Rect(row, col, TILE_SIZE, TILE_SIZE), 
                1
            )


def main():

    # Constants
    SCREEN_WIDTH = 800
    SCREEN_HEIGHT = 800
    SCREEN_BG = (0, 0, 0) 
    FPS = 60

    # Initialize pygame
    pygame.init()
    # Initialize pygame Clock
    clock = pygame.time.Clock()
    
    # Create the screen and set the title
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Snek")


    # main game loop
    while True:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill(SCREEN_BG)

        # Create the grid
        draw_grid(screen)

        # Update screen
        pygame.display.flip()

        # Set framerate to 60 fps
        clock.tick(FPS)

if __name__ == "__main__":
    main()
