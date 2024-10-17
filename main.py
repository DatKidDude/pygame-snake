import pygame 
import sys


class Snake:
    """A snake that eats food on the screen"""

    def __init__(self, screen, start_time):
        """Initialize snake and screen instance"""
        # Get the screen rect
        self.screen = screen
        self.screen_rect = screen.get_rect()

        # Create snake
        self.snake = pygame.Rect(400, 400, 20, 20) 
        # Set direction of the snake 
        self.direction = pygame.math.Vector2(1, 0)

        self.last_time = start_time  
        self.current_time = 0

    
    def draw_snake(self):
        """Draw snake on the screen"""
        pygame.draw.rect(self.screen, "green", self.snake)
    

    def move_snake(self):
        """Move the snake across the screen every 100 milliseconds"""
        self.current_time = pygame.time.get_ticks()
        if self.current_time - self.last_time > 100:
            self.snake.x += self.direction.x * 20
            self.snake.y += self.direction.y * 20
            self.last_time = self.current_time


    def update(self):
        """Update the snakes (x, y) position on the grid"""
        self.move_snake()
        self.draw_snake()
        
    
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


def check_keydown_events(event, snake):
    """Check keypresses"""
    # Storing all 4 directions 
    snake_directions = {
        "up": (0, -1),
        "down": (0, 1),
        "right": (1, 0),
        "left": (-1, 0)
    }

    if event.key == pygame.K_UP:
        snake.direction[:] = snake_directions["up"]
    elif event.key == pygame.K_DOWN:
        snake.direction[:] = snake_directions["down"]
    elif event.key == pygame.K_RIGHT:
        snake.direction[:] = snake_directions["right"]
    elif event.key == pygame.K_LEFT:
        snake.direction[:] = snake_directions["left"]
        
        
def main():

    # Constants
    SCREEN_WIDTH = 800
    SCREEN_HEIGHT = 800
    SCREEN_BG = (0, 0, 0) 
    FPS = 144

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
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                check_keydown_events(event, snake)

        screen.fill(SCREEN_BG)

        # Create the grid
        draw_grid(screen)

        snake.update()

        # Update screen
        pygame.display.flip()

        # Set framerate to 60 fps
        clock.tick(FPS)

if __name__ == "__main__":
    main()
