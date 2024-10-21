import pygame
import random

class Food:
    """Creates food the snake can eat to grow longer"""

    def __init__(self, screen, size):
        """Initialize snake instance"""
        # Inittialize screen surface and get it's rect values
        self.screen = screen
        self.screen_rect = screen.get_rect()

        # Food color
        self.color = "red"
        
        # Snake size
        self.snake_size = size # 20

        # Food position on grid
        self.food_pos = [None, None]
        # Food flag
        self.eaten = False
    

    def randomize_food_position(self):
        """Generate random (x,y) position for the food"""
        # If the food is on the screen don't reposition
        if not self.eaten:
            self.food_pos[0] = random.randrange(0, 800, self.snake_size) 
            self.food_pos[1] = random.randrange(0, 800, self.snake_size)
            self.eaten = True
    

    def draw_food(self):
        """Display food on the grid"""
        pygame.draw.rect(self.screen, self.color, pygame.Rect(self.food_pos[0], self.food_pos[1], self.snake_size, self.snake_size))
    

    def update(self):
        """Update food state"""
        self.randomize_food_position()
        self.draw_food()
