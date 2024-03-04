import random

import pygame

pygame.init()

# Setting Up The Display
window = pygame.display.set_mode((300, 400))


white = (255, 255, 255)
pygame.display.set_caption("Snake Game")
game_over = False
# while not game_over:
#     for event in pygame.event.get():
#         print(event)  # prints out all the actions that take place on the screen
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

    pygame.draw.rect(window, white, [200, 150, 10, 10])
    pygame.display.update()
pygame.quit()
quit()
