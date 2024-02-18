# Auther : Arun CS

# Github : https://github.com/aruncs31s/aruncs31s
# Source : https://thepythoncode.com/article/make-a-snake-game-with-pygame-in-python#initializing-pygame  -- Got initial Skeleton
# https://doc.rust-lang.org/1.0.0/style/style/naming/README.html -- used to get rust naming conventions


import random  # Used to generate random position for food

import pygame

### Most of the definitions Happen Here###
# Defining Width and Height of the Game Window
GAME_WINDOW_WIDTH, GAME_WINDOW_HEIGHT = 600, 600
# Defining size of snake and food
BLOCK_SIZE = 20
INITIAL_SNAKE_SIZE, FOOD_SIZE = 20, 20

INITIAL_SCORE = 0
score = 0

WHITE = (255, 255, 255)
CYAN = (0, 255, 255)
RED = (255, 0, 0)
BLACK = (8, 8, 8)
pygame.font.init()

# Used to displat score
score_font = pygame.font.SysFont("consolas", 20)  # or any other font you'd like
# score = 0


pygame.init()

win = pygame.display.set_mode((GAME_WINDOW_WIDTH, GAME_WINDOW_HEIGHT))

clock = pygame.time.Clock()

snake_pos = [[GAME_WINDOW_WIDTH // 2, GAME_WINDOW_HEIGHT // 2]]
snake_speed = [0, BLOCK_SIZE]

teleport_walls = True


### Food Generation
def food_generate():
    while True:
        x = (
            random.randint(0, (GAME_WINDOW_WIDTH - BLOCK_SIZE) // BLOCK_SIZE)
            * BLOCK_SIZE
        )
        y = random.randint(0, (GAME_WINDOW_HEIGHT - BLOCK_SIZE) // BLOCK_SIZE)

        food_postion = [x, y]
        if food_postion not in snake_pos:
            return food_postion


food_postion = food_generate()


def draw_objects():
    win.fill(BLACK)  # Set BackGround Color
    for pos in snake_pos:
        pygame.draw.rect(win, CYAN, pygame.Rect(pos[0], pos[1], BLOCK_SIZE, BLOCK_SIZE))
        pygame.draw.rect(
            win,
            RED,
            pygame.Rect(food_postion[0], food_postion[1], BLOCK_SIZE, BLOCK_SIZE),
        )

        score_text = score_font.render(f"Score: {score}", True, WHITE)
        win.blit(score_text, (10, 10))
