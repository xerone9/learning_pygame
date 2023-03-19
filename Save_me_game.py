import pygame
import pygame.mixer
import random
import time
from PIL import Image

pygame.font.init()
pygame.mixer.init()

pygame.display.set_caption("Snake Game")

# Define constants

WIDTH = 800
HEIGHT = 600
BG_COLOR = (0, 0, 0)

PLAYER_WIDTH = 20
PLAYER_HEIGHT = 20
PLAYER_VEL = 5

START_X = WIDTH / 4
START_Y = HEIGHT / 1.7

screen = pygame.display.set_mode((WIDTH, HEIGHT))




def draw(snake):
    screen.fill(BG_COLOR)

    for i in snake:
        pygame.draw.rect(screen, "red", i)



    pygame.display.update()


def main():
    clock = pygame.time.Clock()

    go_right = True
    go_down = True
    go_up = True
    go_left = True


    running = True

    count = 20

    snake = []

    for i in range(1,7):
        player = pygame.Rect(START_X + count, START_Y, PLAYER_WIDTH, PLAYER_HEIGHT)
        snake.append(player)
        count += 20



    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        clock.tick(15)
        keys = pygame.key.get_pressed()

        if keys[pygame.K_RIGHT]:
            go_left = False
            go_up = True
            go_down = True
            go_right = True

        if keys[pygame.K_LEFT]:
            go_left = True
            go_up = True
            go_down = True
            go_right = False

        if keys[pygame.K_UP]:
            go_left = True
            go_up = True
            go_down = False
            go_right = True

        if keys[pygame.K_DOWN]:
            go_left = True
            go_up = False
            go_down = True
            go_right = True



        if go_right is False:
            if snake[-1].x <= 0:
                running = False
            else:
                player = pygame.Rect(snake[-1].x - PLAYER_WIDTH, snake[-1].y,
                                     PLAYER_WIDTH, PLAYER_HEIGHT)
                snake.append(player)
                snake.pop(0)

        if go_left is False:
            if snake[-1].x + PLAYER_WIDTH >= WIDTH:
                running = False
            else:
                player = pygame.Rect(snake[-1].x + PLAYER_WIDTH, snake[-1].y,
                                     PLAYER_WIDTH, PLAYER_HEIGHT)
                snake.append(player)
                snake.pop(0)


        if go_down is False:
            if snake[-1].y - PLAYER_HEIGHT < 0:
                running = False
            else:
                player = pygame.Rect(snake[-1].x, snake[-1].y - PLAYER_HEIGHT,
                                     PLAYER_WIDTH, PLAYER_HEIGHT)
                snake.append(player)
                snake.pop(0)

        if go_up is False:
            if snake[-1].y + PLAYER_HEIGHT >= HEIGHT:
                running = False
            else:
                player = pygame.Rect(snake[-1].x, snake[-1].y + PLAYER_HEIGHT,
                                     PLAYER_WIDTH, PLAYER_HEIGHT)
                snake.append(player)
                snake.pop(0)


        draw(snake)



if __name__ == "__main__":
    main()
