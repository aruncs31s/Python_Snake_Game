# Time = 2:33 AM 24.02.2024
import random
import time

import pygame

from snake_temp_5 import WINDOW_HEIGHT, WINDOW_WIDTH

pygame.init()
# Define Window Size
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

# Define Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 102)

# Defining snake properties

snake_size = 10
snake_speed = 30


window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Snake Game")
clock = pygame.time.Clock()

# Defining fonts
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)


def message(msg, color):
    mesg = font_style.render(msg, True, color)
    window.blit(mesg, [WINDOW_WIDTH / 2 - 50, WINDOW_HEIGHT / 2 - 50])


def gameLoop():
    game_over = False
    game_close = False

    snake_List = []
    Length_of_snake = 1
    x = WINDOW_WIDTH / 2
    y = WINDOW_HEIGHT / 2
    x_change = 0
    y_change = 0

    foodx = round(random.randrange(0, WINDOW_WIDTH - snake_size) / 10) * 10
    foody = round(random.randrange(0, WINDOW_WIDTH - snake_size) / 10) * 10

    while not game_over:
        while game_close == True:
            window.fill(BLUE)
            message("close", RED)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()
