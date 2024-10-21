import pygame

class Snake:
    """A snake that eats food on the screen"""

    def __init__(self, screen, start_time, size):
        """Initialize snake and screen instance"""
        # Get the screen rect
        self.screen = screen
        self.screen_rect = screen.get_rect()

        # Snake size
        self.snake_size = size # 20

        # Set starting position
        self.snake_head = [400, 400]
        self.snake_body = [
                        [400, 400],
                        [380, 400],
                        [360, 400],
                        [340, 400],
                        # [320, 400],
                        # [300, 400],
                        # [280, 400],
                        # [260, 400],
                        # [240, 400],
                        # [220, 400],
                        # [200, 400],
                        # [180, 400],
                        # [160, 400],
                        # [140, 400],
                        ]
        # Set the (x,y) direction of the snake 
        self.direction = pygame.math.Vector2(1, 0)

        self.last_time = start_time  
        self.current_time = 0

    
    def draw_snake(self):
        """Draw the snake on the screen"""
        for pos in self.snake_body:
            pygame.draw.rect(self.screen, "green", pygame.Rect(pos[0], pos[1], self.snake_size, self.snake_size))

    
    def move_snake(self):
        """Update the snakes (x,y) position"""
        self.current_time = pygame.time.get_ticks()
        if self.current_time - self.last_time > 50:
            # Create a copy of snake_head and pass it to snake_body
            self.snake_body.insert(0, list(self.snake_head))

            self.snake_head[0] += self.direction.x * self.snake_size
            self.snake_head[1] += self.direction.y * self.snake_size
            self.snake_body.pop()
            self.last_time = self.current_time


    def check_boundaries(self):
        """Check if the snake is touching the edge of the screen"""
        if self.snake_head[0] > self.screen_rect.right - self.snake_size or self.snake_head[0] < 0:
            return True
        if self.snake_head[1] > self.screen_rect.bottom - self.snake_size or self.snake_head[1] < 0:
            return True
    

    def grow(self):
        """Have the snake grow in size"""
        self.snake_body.append(list(self.snake_body[-1]))
        

    def update(self):
        """Update the snakes (x,y) position on the grid"""
        self.move_snake()
        self.check_boundaries()
        self.draw_snake()