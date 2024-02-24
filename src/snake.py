# Auther : Arathi CK , Arun CS
# https://github.com/Arathhi/Python_Snake_Game

# importing the modules 
import random
import pygame



pygame.init()

# Define Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 102)
GREEN = (0, 255, 0)

# Define Window Size
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

# Define Window
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
# Setting Game Title
pygame.display.set_caption("Snake Game")

clock = pygame.time.Clock()


# Defining snake properties

snake_size = 10
snake_speed = 15



# Defining fonts
font_style = pygame.font.SysFont("comicsansms", 25)
score_font = pygame.font.SysFont("comicsansms", 35)


def Your_score(score):
    value= score_font.render("Your Score:" + str(score), True, YELLOW)
    window.blit(value, [0,0])

def our_snake(snake_size, snake_List):
    for k in snake_List:
        pygame.draw.rect(window, BLACK, [k[0], k[1], snake_size, snake_size])

def message(msg, color):
    mesg = font_style.render(msg, True, color)
    window.blit(mesg, [WINDOW_WIDTH / 2 - 240, WINDOW_HEIGHT / 2 - 50])


def gameLoop():
    game_over = False
    game_close = False

    snake_position_x = 400
    snake_position_y = 300

    snake_position_x_change = 0
    snake_position_y_change = 0

    snake_List = []
    Length_of_snake = 1

    foodx = round(random.randrange(0, WINDOW_WIDTH - snake_size) / 10) * 10
    foody = round(random.randrange(0, WINDOW_WIDTH - snake_size) / 10) * 10

    while not game_over:

        while game_close == True:
            window.fill(BLUE)
            message("You Lost! Press C-Play Again or Q-Quit", RED)
            Your_score(Length_of_snake - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():                    
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:        
                if event.key == pygame.K_LEFT:
                    snake_position_x_change = -snake_size
                    snake_position_y_change = 0
                elif event.key == pygame.K_RIGHT:
                    snake_position_x_change = snake_size
                    snake_position_y_change = 0
                elif event.key == pygame.K_DOWN:
                    snake_position_x_change = 0
                    snake_position_y_change = snake_size
                elif event.key == pygame.K_UP:
                    snake_position_x_change = 0
                    snake_position_y_change = -snake_size

        if snake_position_x >= WINDOW_WIDTH or snake_position_x < 0 or snake_position_y >= WINDOW_HEIGHT or snake_position_y < 0:
            game_close = True
        snake_position_x += snake_position_x_change
        snake_position_y += snake_position_y_change
        window.fill(BLUE)
        pygame.draw.rect(window, GREEN, [foodx, foody, snake_size, snake_size])
        snake_Head = []
        snake_Head.append(snake_position_x)
        snake_Head.append(snake_position_y)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        for k in snake_List[:-1]:
            if k == snake_Head:
                game_close = True

        our_snake(snake_size, snake_List)
        Your_score(Length_of_snake - 1)

        pygame.display.update()

        if snake_position_x == foodx and snake_position_y == foody:
            foodx = round(random.randrange(0, WINDOW_WIDTH - snake_size) / 10.0) * 10.0
            foody = round(random.randrange(0, WINDOW_HEIGHT - snake_size) / 11.0) * 10.0
            Length_of_snake += 1

        clock.tick(snake_speed)

    pygame.quit()
    quit()

gameLoop()