# Auther : Arun CS
# Time : 21.02.2024
# Github : https://github.com/aruncs31s/aruncs31s

# Most of the basic settings are defined here
import pygame

### Most of the definitions Happen Here So that it would be easier to edit###

# Defining Width and Height of the Game Window
GAME_WINDOW_WIDTH, GAME_WINDOW_HEIGHT = 600, 600
# Defining size of snake and food
BLOCK_SIZE = 20
INITIAL_SNAKE_SIZE, FOOD_SIZE = 20, 20

# score = 0

WHITE = (255, 255, 255)
CYAN = (0, 255, 255)
RED = (255, 0, 0)
BLACK = (8, 8, 8)

BACKGROUND = BLACK

# Used to display score

# Used To enable transpot through walls
teleport_walls = True

score_font = pygame.font.SysFont("consolas", 20)  # or any other font you'd like


win = pygame.display.set_mode((GAME_WINDOW_WIDTH, GAME_WINDOW_HEIGHT))


# Used to control snake speed

clock = pygame.time.Clock()
