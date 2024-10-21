import pygame
import sys


def check_events(snake):
    """Respond to keypresses and mouse events"""
    # Watch for keyboard and mouse events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, snake)


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
        

def game_over(snake):
    """Check for game over events"""
    if snake.check_boundaries():
        pygame.quit()
        sys.exit()


def update_screen(snake, screen, SCREEN_BG, clock, FPS):
    """Update screen contents"""
    screen.fill(SCREEN_BG)

    # Check for end of game
    game_over(snake)

    # Create the grid
    draw_grid(screen)

    # Update snake position
    snake.update()

    # Update screen
    pygame.display.flip()

    # Set framerate to 60 fps
    clock.tick(FPS)
    