import pygame
import pygame.mixer
import random
import time


pygame.font.init()
pygame.mixer.init()

pygame.display.set_caption("Tetris")

# Define constants
WIDTH = 500
HEIGHT = 800
BG_COLOR = (0, 0, 0)

L_1 = pygame.image.load("assets\pics\\L_shape.png")
L_2 = pygame.transform.flip(L_1, True, False)
S_1 = pygame.image.load("assets\pics\\S_shape.png")
S_2 = pygame.transform.flip(S_1, True, False)
T = pygame.image.load("assets\pics\\T_shape.png")
Bar = pygame.image.load("assets\pics\\Bar_shape.png")
Box = pygame.image.load("assets\pics\\Box_shape.png")

PLAYER_VEL = 20

screen = pygame.display.set_mode((WIDTH, HEIGHT))


def draw(mask1, x1,y1, x2, y2):
    screen.fill(BG_COLOR)
    screen.blit(S_1, (x1, y1))
    screen.blit(Box, (x2, y2))
    pygame.display.update()


def main():
    clock = pygame.time.Clock()

    x1, y1 = 100, (HEIGHT / 2) - L_2.get_height()
    x2, y2 = 100, HEIGHT - 100

    mask1 = pygame.mask.from_surface(S_1)
    mask2 = pygame.mask.from_surface(Box)



    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        if mask1.overlap(mask2, (x2 - x1, y2 - y1)) is not None:
            print("Collision detected!")

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and x2 >= 0:
            x2 -= PLAYER_VEL

        if keys[pygame.K_RIGHT] and x2 <= WIDTH:
            x2 += PLAYER_VEL

        if keys[pygame.K_UP] and y2 >= 0:
            y2 -= PLAYER_VEL

        if keys[pygame.K_DOWN] and y2 <= HEIGHT:
            y2 += PLAYER_VEL

        clock.tick(10)
        draw(mask1, x1, y1, x2, y2)


if __name__ == "__main__":
    main()
