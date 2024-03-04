# Auther : Arun CS
# Time : 3:29 PM 21.02.2024
# project name : Snake Game


import random

import pygame

from config import *

pygame.init()
white = (255, 255, 255)

# Setting Up The Display
# window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
window = pygame.display.set_mode((300, 400))

pygame.display.set_caption("Snake Game")
game_over = False
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
pygame.draw.rect(window, white, [200, 150, 10, 10])
pygame.display.update()
pygame.quit()
quit()
