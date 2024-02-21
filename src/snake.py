# Auther : Arun CS
# Time : 3:29 PM 21.02.2024
# project name : Snake Game


import random

import pygame

from config import *
from config import WHITE

pygame.init()

# Setting Up The Display
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

pygame.display.update()
pygame.display.set_caption("Snake Game")
game_over = False
# while not game_over:
#     for event in pygame.event.get():
#         print(event)  # prints out all the actions that take place on the screen
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

pygame.draw.rect(window, WHITE, [200, 150, 10, 10])


pygame.quit()
quit()
