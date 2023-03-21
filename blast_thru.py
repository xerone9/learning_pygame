import pygame
import pygame.mixer
import random
import time


pygame.font.init()
pygame.mixer.init()
pygame.init()

pygame.display.set_caption("Snake Game")

# Define constants
WIDTH = 820
HEIGHT = 600
BG_COLOR = (0, 0, 0)

PLAYER_WIDTH = 125
PLAYER_HEIGHT = 15
PLAYER_COLOR = "blue"
PLAYER_VEL = 5

BALL_RADIUS = 10
BALL_COLOR = "green"
BALL_VEL_X = 5
BALL_VEL_Y = 5

BRICK_WIDTH = 25
BRICK_HEIGHT = 15
BRICK_COLOR = "red"

screen = pygame.display.set_mode((WIDTH, HEIGHT))

def create_ball():
    x = WIDTH/2 - BALL_RADIUS/2
    y = HEIGHT - PLAYER_HEIGHT
    circle = pygame.Rect(x - BALL_RADIUS, y - BALL_RADIUS * 2, BALL_RADIUS * 2, BALL_RADIUS * 2), BALL_VEL_X, BALL_VEL_Y
    return circle


def draw(player, ball, start, bricks, color_sequence_of_bricks):
    screen.fill(BG_COLOR)

    for i, (circle, vx, vy) in enumerate(ball):
        if start:
            circle.move_ip(vx, vy)

            if circle.colliderect(player):
                collision_pos = (175 - (player.right - circle.left)) - (BALL_RADIUS * 3)
                if collision_pos < 60:
                    print("bounce left")
                elif collision_pos > 80:
                    print("bounce right")
                vy = -vy
            else:
                if circle.left < 0 or circle.right > WIDTH:
                    vx = -vx
                if circle.top < 0 or circle.bottom > HEIGHT:
                    vy = -vy

            ball[i] = (circle, vx, vy)
        else:
            pygame.draw.circle(screen, BALL_COLOR, circle.center, BALL_RADIUS)

    for circle, _, _ in ball:
        pygame.draw.circle(screen, BALL_COLOR, circle.center, BALL_RADIUS)

    count = 1
    for brick in bricks:
        if count % 2 == 0:
            pygame.draw.rect(screen, BRICK_COLOR, brick)
        else:
            pygame.draw.rect(screen, "pink", brick)
        count += 1

    for i in bricks:
        for j, (circle, vx, vy) in enumerate(ball):
            if circle.colliderect(i):
                vy = -vy
                ball[j] = (circle, vx, vy)

    pygame.draw.rect(screen, PLAYER_COLOR, player)

    pygame.display.update()


def main():
    clock = pygame.time.Clock()

    player = pygame.Rect(WIDTH/2 - PLAYER_WIDTH/2, HEIGHT - PLAYER_HEIGHT, PLAYER_WIDTH, PLAYER_HEIGHT)
    ball = [create_ball()]

    bricks = []
    color_sequence_of_bricks = []

    x = 0
    y = 0
    count = 1
    for i in range(1,493):
        if x >= WIDTH:
            y += BRICK_HEIGHT
            x = 0
        brick = pygame.Rect(x, y, BRICK_WIDTH, BRICK_HEIGHT)
        x += 20
        bricks.append(brick)
        if count % 2 == 0:
            color_sequence_of_bricks.append("pink")
        else:
            color_sequence_of_bricks.append("red")
        count += 1

    color_sequence_of_bricks = bricks.copy()

    running = True
    start = False

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT] and player.x >= 0:
            start = True
            player.x -= PLAYER_VEL
        if keys[pygame.K_RIGHT] and player.x + PLAYER_VEL + player.width <= WIDTH:
            start = True
            player.x += PLAYER_VEL

        for i, (circle, vx, vy) in enumerate(ball):
            if circle.y + PLAYER_HEIGHT >= HEIGHT:
                running = False

        for i in bricks:
            for j, (circle, vx, vy) in enumerate(ball):
                if circle.colliderect(i):
                    bricks.remove(i)


        clock.tick(60)
        draw(player, ball, start, bricks, color_sequence_of_bricks)


if __name__ == "__main__":
    main()
