import pygame 
import sys

class Snake:
    """A snake that eats food on the screen"""

    def __init__(self, screen, start_time):
        """Initialize snake and screen instance"""
        # Get the screen rect
        self.screen = screen
        self.screen_rect = screen.get_rect()

        # Set starting position
        self.snake_head = [400, 400]
        self.snake_body = [
                        [400, 400],
                        [380, 400],
                        [360, 400]
                        ]
        # Set the (x,y) direction of the snake 
        self.direction = pygame.math.Vector2(1, 0)

        self.last_time = start_time  
        self.current_time = 0

    
    def draw_snake(self):
        """Draw the snake on the screen"""
        for pos in self.snake_body:
            pygame.draw.rect(self.screen, "green", pygame.Rect(pos[0], pos[1], 20, 20))

    
    def move_snake(self):
        """Update the snakes (x,y) position"""
        self.current_time = pygame.time.get_ticks()
        if self.current_time - self.last_time > 50:
            # Create a copy of snake_head and pass it to snake_body
            self.snake_body.insert(0, list(self.snake_head))

            self.snake_head[0] += self.direction.x * 20
            self.snake_head[1] += self.direction.y * 20
            self.snake_body.pop()
            self.last_time = self.current_time


    def check_boundaries(self):
        """Check if the snake is touching the edge of the screen"""
        if self.snake_head[0] > self.screen_rect.right - 20 or self.snake_head[0] < 0:
            return True
        if self.snake_head[1] > self.screen_rect.bottom - 20 or self.snake_head[1] < 0:
            return True
        

    def update(self):
        """Update the snakes (x,y) position on the grid"""
        self.check_boundaries()
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

    # Prevent snake from moving backwards into itself
    if snake.direction == snake_directions["up"] and event.key == pygame.K_DOWN:
        return 
    if snake.direction == snake_directions["down"] and event.key == pygame.K_UP:
        return 
    if snake.direction == snake_directions["right"] and event.key == pygame.K_LEFT:
        return 
    if snake.direction == snake_directions["left"] and event.key == pygame.K_RIGHT:
        return 

    if event.key == pygame.K_UP:
        snake.direction[:] = snake_directions["up"]
    elif event.key == pygame.K_DOWN:
        snake.direction[:] = snake_directions["down"]
    elif event.key == pygame.K_RIGHT:
        snake.direction[:] = snake_directions["right"]
    elif event.key == pygame.K_LEFT:
        snake.direction[:] = snake_directions["left"]
        

def game_over(snake):
    """Check for game over events"""
    if snake.check_boundaries():
        pygame.quit()
        sys.exit()


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

        # check for end of game
        game_over(snake)

        # Create the grid
        draw_grid(screen)

        snake.update()

        # Update screen
        pygame.display.flip()


        # Set framerate to 60 fps
        clock.tick(FPS)

if __name__ == "__main__":
    main()


