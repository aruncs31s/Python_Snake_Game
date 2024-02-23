import pygame

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 500
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Snake Game")
game_over = False
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
    pygame.draw.rect(window, WHITE, [200, 150, 10, 10])
    pygame.display.update()
pygame.quit()
quit()
