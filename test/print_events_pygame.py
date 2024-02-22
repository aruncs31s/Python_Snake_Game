import pygame

pygame.init()


game_over = False

while not game_over:
    for event in pygame.event.get():
        print(event)
