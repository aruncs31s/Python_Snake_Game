import random
import time

import pygame

pygame.init()
white = (255, 255, 255)
red = (255, 0, 0)
black = (0, 0, 0)
blue = (0, 0, 255)
yellow = (255, 255, 102)


WINDOW_WIDTH = 600
WINDOW_HEIGHT = 400

window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Snake Game")


snake_size = 10
snake_speed = 10
snake_List = []
Length_of_snake = 1

# x = 300
# y = 300


clock = pygame.time.Clock()

font_style = pygame.font.SysFont("default", 50)


snake_speed = 30
snake_size = 10


def our_snake(snake_size, snake_list):
    for k in snake_list:
        pygame.draw.rect(window, black, [k[0], k[1], snake_size, snake_size])


def message(msg, color):
    mesg = font_style.render(msg, True, color)
    window.blit(mesg, [WINDOW_WIDTH / 2 - 50, WINDOW_HEIGHT / 2 - 50])


def gameLoop():
    game_over = False
    game_close = False

    x = WINDOW_WIDTH / 2
    y = WINDOW_HEIGHT / 2

    x_change = 0
    y_change = 0

    foodx = round(random.randrange(0, WINDOW_WIDTH - snake_size) / 10) * 10
    foody = round(random.randrange(0, WINDOW_WIDTH - snake_size) / 10) * 10

    while not game_over:
        while game_close == True:
            window.fill(blue)
            message("You Lost", red)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            message("Quiting", red)
            pygame.display.update()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -snake_size
                    y_change = 0
                elif event.key == pygame.K_RIGHT:
                    x_change = snake_size
                    y_change = 0
                elif event.key == pygame.K_DOWN:
                    x_change = 0
                    y_change = snake_size
                elif event.key == pygame.K_UP:
                    x_change = 0
                    y_change = -snake_size

        if x >= WINDOW_WIDTH or x < 0 or y >= WINDOW_HEIGHT or y < 0:
            game_close = True
        x += x_change
        y += y_change
        window.fill(blue)
        snake_Head = []
        snake_Head.append(x)
        snake_Head.append(y)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]
        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True
        our_snake(snake_size, snake_List)
        pygame.display.update()

    # Background

    # window.fill(black)
    # message("Game Over", red)
    # pygame.draw.rect(window, blue, [foodx, foody, snake_size, snake_size])
    # pygame.draw.rect(window, white, [x, y, snake_size, snake_size])
    # pygame.display.update()
    if x == foodx and y == foody:
        foodx = round(random.randrange(0, WINDOW_WIDTH - snake_size) / 10) * 10
        foody = round(random.randrange(0, WINDOW_WIDTH - snake_size) / 10) * 10
        Length_of_snake += 1

        # print("Good")

    clock.tick(snake_speed)


# message("You lost", red)
# pygame.display.update()
# time.sleep(9)
# Control Snake speed
pygame.quit()
quit()
