# Source : https://thepythoncode.com/article/make-a-snake-game-with-pygame-in-python#initializing-pygame  -- Got initial Skeleton
# https://doc.rust-lang.org/1.0.0/style/style/naming/README.html -- used to get rust naming conventions


import random  # Used to generate random position for food

import pygame
from setup import *

from config import *

score = 0
pygame.font.init()
pygame.init()
snake_pos = [[GAME_WINDOW_WIDTH // 2, GAME_WINDOW_HEIGHT // 2]]
snake_speed = [0, BLOCK_SIZE]


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


# Initial Position of the food
food_postion = food_generate()


def draw_objects():
    win.fill(BACKGROUND)  # Set BackGround Color
    for pos in snake_pos:
        pygame.draw.rect(win, CYAN, pygame.Rect(pos[0], pos[1], BLOCK_SIZE, BLOCK_SIZE))
        pygame.draw.rect(
            win,
            RED,
            pygame.Rect(food_postion[0], food_postion[1], BLOCK_SIZE, BLOCK_SIZE),
        )

        score_text = score_font.render(f"Score: {score}", True, WHITE)
        win.blit(score_text, (10, 10))
