import pygame
import pygame.mixer
import random
import time


pygame.font.init()
pygame.mixer.init()

pygame.display.set_caption("Snake Game")

# Define constants
WIDTH = 800
HEIGHT = 600
BG_COLOR = (0, 0, 0)

PLAYER_WIDTH = 20
PLAYER_HEIGHT = 20

GROW_RADIUS = 11
GROW_COLOR = (0, 255, 0)
GROW_VX = 20
GROW_VY = 20

START_X = WIDTH / 4
START_Y = HEIGHT / 2

screen = pygame.display.set_mode((WIDTH, HEIGHT))


def create_energy(snake):
    x = random.randint(GROW_RADIUS, WIDTH - GROW_RADIUS)
    y = random.randint(GROW_RADIUS, HEIGHT - GROW_RADIUS)
    for i in snake:
        if i.x == x:
            x = random.randint(GROW_RADIUS, WIDTH - GROW_RADIUS)
        if i.y == y:
            y = random.randint(GROW_RADIUS, HEIGHT - GROW_RADIUS)
    circle = pygame.Rect(x - GROW_RADIUS, y - GROW_RADIUS, GROW_RADIUS * 2, GROW_RADIUS * 2), GROW_VX, GROW_VY
    return circle


def draw(snake, power, power_movement):
    screen.fill(BG_COLOR)

    for i in snake:
        pygame.draw.rect(screen, "blue", i)

    # If you want energy to move uncomment below code

    # for i, (circle, vx, vy) in enumerate(power):
    #     if power_movement == "power_move_up":
    #         circle.move_ip(0, -vy)
    #     if power_movement == "power_move_down":
    #         circle.move_ip(0, vy)
    #     if power_movement == "power_move_left":
    #         circle.move_ip(-vx, 0)
    #     if power_movement == "power_move_right":
    #         circle.move_ip(vx, 0)
    #     if circle.left < 20 or circle.right > WIDTH - 20:
    #         vx = -vx
    #     if circle.top < 20 or circle.bottom > HEIGHT - 20:
    #         vy = -vy
    #     power[i] = (circle, vx, vy)

    for i, (circle, vx, vy) in enumerate(power):
        pygame.draw.circle(screen, GROW_COLOR, circle.center, GROW_RADIUS)


    pygame.display.update()


def main():
    clock = pygame.time.Clock()


    go_right = True
    go_down = True
    go_up = True
    go_left = False

    running = True

    power_movement = "power_move_right"

    count = PLAYER_WIDTH

    snake = []

    energy_movement_time = time.time() + 0.25

    for i in range(1,7):
        player = pygame.Rect(START_X + count, START_Y, PLAYER_WIDTH, PLAYER_HEIGHT)
        snake.append(player)
        count += 20

    power = [create_energy(snake)]
    start = 0


    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        clock.tick(15)

        if not energy_movement_time > time.time():
            power_movement = random.choice(["power_move_up", "power_move_down", "power_move_left", "power_move_right"])
            energy_movement_time = time.time() + 0.25

        keys = pygame.key.get_pressed()
        if go_right:
            if keys[pygame.K_RIGHT]:
                start = 1
                go_left = False
                go_up = True
                go_down = True
                go_right = True

        if go_left:
            if keys[pygame.K_LEFT]:
                go_left = True
                go_up = True
                go_down = True
                go_right = False

        if go_up:
            if keys[pygame.K_UP]:
                start = 1
                go_left = True
                go_up = True
                go_down = False
                go_right = True

        if go_down:
            if keys[pygame.K_DOWN]:
                start = 1
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

                for i, (circle, vx, vy) in enumerate(power):
                    if player.colliderect(circle):
                        power.clear()
                        power = [create_energy(snake)]
                        snake.append(player)
                    else:
                        snake.append(player)
                        check_collision = []
                        for i in snake:
                            if i in check_collision:
                                running = False
                            else:
                                check_collision.append(i)
                        snake.pop(0)

        if start != 0:
            if go_left is False:
                if snake[-1].x + PLAYER_WIDTH >= WIDTH:
                    running = False
                else:
                    player = pygame.Rect(snake[-1].x + PLAYER_WIDTH, snake[-1].y,
                                         PLAYER_WIDTH, PLAYER_HEIGHT)

                    for i, (circle, vx, vy) in enumerate(power):
                        if player.colliderect(circle):
                            power.clear()
                            power = [create_energy(snake)]
                            snake.append(player)
                        else:
                            snake.append(player)
                            check_collision = []
                            for i in snake:
                                if i in check_collision:
                                    running = False
                                else:
                                    check_collision.append(i)
                            snake.pop(0)

        if go_down is False:
            if snake[-1].y <= 0:
                running = False
            else:
                player = pygame.Rect(snake[-1].x, snake[-1].y - PLAYER_HEIGHT,
                                     PLAYER_WIDTH, PLAYER_HEIGHT)

                for i, (circle, vx, vy) in enumerate(power):
                    if player.colliderect(circle):
                        power.clear()
                        power = [create_energy(snake)]
                        snake.append(player)
                    else:
                        snake.append(player)
                        check_collision = []
                        for i in snake:
                            if i in check_collision:
                                running = False
                            else:
                                check_collision.append(i)
                        snake.pop(0)

        if go_up is False:
            if snake[-1].y + PLAYER_HEIGHT >= HEIGHT:
                running = False
            else:
                player = pygame.Rect(snake[-1].x, snake[-1].y + PLAYER_HEIGHT,
                                     PLAYER_WIDTH, PLAYER_HEIGHT)

                for i, (circle, vx, vy) in enumerate(power):
                    if player.colliderect(circle):
                        power.clear()
                        power = [create_energy(snake)]
                        snake.append(player)
                    else:
                        snake.append(player)
                        check_collision = []
                        for i in snake:
                            if i in check_collision:
                                running = False
                            else:
                                check_collision.append(i)
                        snake.pop(0)

        draw(snake, power, power_movement)


if __name__ == "__main__":
    main()
