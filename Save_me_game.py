import pygame
import pygame.mixer
import random
import math
import time


pygame.font.init()
pygame.mixer.init()
pygame.init()

pygame.display.set_caption("Save Me")

# Define constants
WIDTH = 800
HEIGHT = 600
BG_COLOR = (0, 0, 0)

BALL_RADIUS = 20
BALL_COLOR = "dark orange"
BALL_VEL_X = 2
BALL_VEL_Y = 2

NO_OF_BALLS = 41 # Odd Number Only (Still dont know whats the bug)

PLAYER_WIDTH = BALL_RADIUS / 2
PLAYER_HEIGHT = PLAYER_WIDTH
PLAYER_VEL = 5
PLAYER_COLOR = "white"

CORDS = []
CIRCLES = []

screen = pygame.display.set_mode((WIDTH, HEIGHT))
FONT = pygame.font.SysFont("comicsans", 30)


def create_ball(x, y):
    vx = random.choice([-BALL_VEL_X, BALL_VEL_X])
    vy = random.choice([-BALL_VEL_Y, BALL_VEL_Y])
    circle = pygame.Rect(x - BALL_RADIUS, y - BALL_RADIUS * 2, BALL_RADIUS, BALL_RADIUS), vx, vy
    return circle


def draw(circles, player, elapsed_time, start):
    screen.fill(BG_COLOR)

    pygame.draw.rect(screen, PLAYER_COLOR, player)

    for i, (circle, vx, vy) in enumerate(circles):
        if start:
            circle.move_ip(vx, vy)

        # Thats causing error if balls are even
        for j, (other_circle, other_vx, other_vy) in enumerate(circles):
            if i != j:
                distance = math.sqrt((circle.x - other_circle.x) ** 2 + (circle.y - other_circle.y) ** 2)
                if distance < 2 * BALL_RADIUS:
                    vx = -vx
                    vy = -vy
                    break

                    # if circle.top < other_circle.top or circle.bottom > other_circle.bottom:
                    #     vy = -vy
                    #     vx = vx
                    # elif circle.left < other_circle.left or circle.right > other_circle.right:
                    #     vx = -vx
                    #     vy = vy
                    # elif other_circle.top - (BALL_RADIUS / 2) < circle.top or other_circle.bottom + (BALL_RADIUS / 2) > circle.bottom:
                    #     vy = -vy
                    #     vx = vx
                    # elif other_circle.left - (BALL_RADIUS / 2) < circle.left or other_circle.right + (BALL_RADIUS / 2) > circle.right:
                    #     vx = -vx
                    #     vy = vy

            if circle.left - (BALL_RADIUS / 2) < 0 or circle.right + (BALL_RADIUS / 2) > WIDTH:
                vx = -vx
            if circle.top - (BALL_RADIUS / 2) < 0 or circle.bottom + (BALL_RADIUS / 2) > HEIGHT:
                vy = -vy

        circles[i] = (circle, vx, vy)

    for circle, _, _ in circles:
        pygame.draw.circle(screen, BALL_COLOR, circle.center, BALL_RADIUS)

    time_text = FONT.render(f"Time: {round(elapsed_time)}s", 1, "white")
    screen.blit(time_text, (10, 10))

    pygame.display.update()


def main():
    clock = pygame.time.Clock()

    elapsed_time = 0

    start = False
    hit = False

    circles = []
    player = pygame.Rect((WIDTH / 2) - PLAYER_WIDTH / 2, (HEIGHT / 2) - PLAYER_HEIGHT / 2, PLAYER_WIDTH, PLAYER_HEIGHT)

    for x in range(player.x, int(player.x + PLAYER_WIDTH + 50)):
        for y in range(player.y, int(player.y + PLAYER_HEIGHT + 50)):
            CORDS.append((x, y))

    for i in range(NO_OF_BALLS):
        x = random.randint(BALL_RADIUS * 2, WIDTH - BALL_RADIUS * 2)
        y = random.randint(BALL_RADIUS * 2, HEIGHT - BALL_RADIUS * 2)
        while (x, y) in CORDS:
            x = random.randint(BALL_RADIUS * 2, WIDTH - BALL_RADIUS * 2)
            y = random.randint(BALL_RADIUS * 2, HEIGHT - BALL_RADIUS * 2)
        circle, vx, vy = create_ball(x, y)
        circles.append((circle, vx, vy))
        CORDS.append((x, y))
        for x in range(circle.center[0] - BALL_RADIUS, circle.center[0] + (BALL_RADIUS * 4)):
            for y in range(circle.center[1] - BALL_RADIUS, circle.center[1] + (BALL_RADIUS * 4)):
                CORDS.append((x, y))

    running = True
    while running:
        if start:
            elapsed_time += 1/60
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player.x - PLAYER_VEL >= 0:
            start = True
            player.x -= PLAYER_VEL
        if keys[pygame.K_RIGHT] and player.x + PLAYER_VEL + player.width <= WIDTH:
            start = True
            player.x += PLAYER_VEL

        if keys[pygame.K_UP] and player.y - PLAYER_VEL >= 0:
            start = True
            player.y -= PLAYER_VEL
        if keys[pygame.K_DOWN] and player.y + PLAYER_VEL + player.height <= HEIGHT:
            start = True
            player.y += PLAYER_VEL

        for i, (circle, vx, vy) in enumerate(circles):
            if player.colliderect(circle):
                hit = True

        if hit:
            lost_text = FONT.render("You Lost!", 1, "white")
            screen.blit(lost_text, (WIDTH / 2 - lost_text.get_width() / 2, HEIGHT / 2 - lost_text.get_height() / 2))
            pygame.display.update()
            pygame.time.delay(5000)
            break

        clock.tick(60)
        draw(circles, player, elapsed_time, start)


if __name__ == "__main__":
    main()
