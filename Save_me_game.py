import pygame
import random
import time

pygame.font.init()
pygame.display.set_caption("Save Me")

# Define constants

WIDTH = 800
HEIGHT = 600
BG_COLOR = (0, 0, 0)

POWER_RADIUS = 11
POWER_SIZE = 11
RESPAWN_POWER = 14
POWER_DURATION = 7

INVULNERABLE_POWER_COLOR = (128,0,128)
DESTROY_ALL_POWER_COLOR = (255,255,0)
DONT_TOUCH_POWER_COLOR = (255,255,255)

CIRCLE_RADIUS = 11
CIRCLE_COLOR = (255, 140, 0)
CIRCLE_VELOCITY = 5
RESPAWN_CIRCLE = 5

PLAYER_WIDTH = 20
PLAYER_HEIGHT = 20
PLAYER_VEL = 5

screen = pygame.display.set_mode((WIDTH, HEIGHT))
FONT = pygame.font.SysFont("comicsans", 30)


def create_power_up():
    x = random.randint(CIRCLE_RADIUS, WIDTH - CIRCLE_RADIUS)
    y = random.randint(CIRCLE_RADIUS, HEIGHT - CIRCLE_RADIUS)
    circle = pygame.Rect(x - CIRCLE_RADIUS, y - CIRCLE_RADIUS, CIRCLE_RADIUS * 2, CIRCLE_RADIUS * 2)
    return circle


def create_circle():
    x = random.randint(CIRCLE_RADIUS, WIDTH - CIRCLE_RADIUS)
    y = CIRCLE_RADIUS
    vx = random.choice([-CIRCLE_VELOCITY, CIRCLE_VELOCITY])
    vy = random.choice([-CIRCLE_VELOCITY, CIRCLE_VELOCITY])
    circle = pygame.Rect(x - CIRCLE_RADIUS, y - CIRCLE_RADIUS, CIRCLE_RADIUS * 2, CIRCLE_RADIUS * 2), vx, vy
    return circle


def create_player():
    player = pygame.Rect((WIDTH / 2) - PLAYER_WIDTH, (HEIGHT / 2) - PLAYER_HEIGHT,
                         PLAYER_WIDTH, PLAYER_HEIGHT)
    return player


def draw(player, circles, powers, elapsed_time, POWER_COLOR, rune_spawned):

    # Draw the circles
    screen.fill(BG_COLOR)

    for power in powers:
        pygame.draw.circle(screen, POWER_COLOR, power.center, POWER_RADIUS)


    pygame.draw.rect(screen, "red", player)



    # Move the circles
    for i, (circle, vx, vy) in enumerate(circles):
        circle.move_ip(vx, vy)

        # Bounce off the walls
        if circle.left < 0 or circle.right > WIDTH:
            vx = -vx
        if circle.top < 0 or circle.bottom > HEIGHT:
            vy = -vy

        # Update the circle's velocity
        circles[i] = (circle, vx, vy)

    for circle, _, _ in circles:
        pygame.draw.circle(screen, CIRCLE_COLOR, circle.center, CIRCLE_RADIUS)

    time_text = FONT.render(f"Time: {round(elapsed_time)}s", 1, "white")
    screen.blit(time_text, (10, 10))

    for i in rune_spawned:
        power_text = FONT.render(i, 1, "green")
        screen.blit(power_text, ((WIDTH - power_text.get_width()) - 15, power_text.get_height() - 25))

    pygame.display.update()


def main():
    player = create_player()

    clock = pygame.time.Clock()

    # Keep track of the circles
    circles = []
    next_circle_time = time.time() + 2

    powers = []
    POWER_COLOR = (0, 255, 0)
    next_power_time = time.time() + 7

    rune_spawned = []

    start_time = time.time()

    # Game loop
    running = True
    hit = False
    power_collected = True
    invulnerable = False
    dont_touch_me = False

    power_duration = time.time() + 5.0

    while running:
        elapsed_time = time.time() - start_time
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Create a new circle if it's time
        if time.time() >= next_circle_time:
            circle, vx, vy = create_circle()
            circles.append((circle, vx, vy))
            next_circle_time = time.time() + RESPAWN_CIRCLE

        if time.time() >= next_power_time:
            power_runes = ["INVULNERABLE", "DESTROY_ALL", "DONT_TOUCH"]
            RUNE_SPAWNED = random.sample(power_runes, 1)[0]

            if RUNE_SPAWNED == "INVULNERABLE":
                POWER_COLOR = INVULNERABLE_POWER_COLOR
            elif RUNE_SPAWNED == "DESTROY_ALL":
                POWER_COLOR = DESTROY_ALL_POWER_COLOR
            elif RUNE_SPAWNED == "DONT_TOUCH":
                POWER_COLOR = DONT_TOUCH_POWER_COLOR

            powers.append(create_power_up())
            next_power_time = time.time() + RESPAWN_POWER
            power_duration = time.time() + POWER_DURATION

        drones = circles.copy()
        for i, (circle, vx, vy) in enumerate(drones):
            if circle.colliderect(player):
                if dont_touch_me:
                    circles.remove((circle, vx, vy))
                else:
                    hit = True


        for power in powers:
            if power.colliderect(player):
                powers.pop()
                power_collected = True
                next_power_time = time.time() + RESPAWN_POWER
                power_duration = time.time() + 5.0
            elif time.time() >= power_duration:
                powers.pop()

        if time.time() <= power_duration and power_collected and time.time() > start_time + 7:
            rune_spawned.append(RUNE_SPAWNED)

            if RUNE_SPAWNED == "INVULNERABLE":
                invulnerable = True
                hit = False

            if RUNE_SPAWNED == "DONT_TOUCH":
                dont_touch_me = True
                hit = False

            if RUNE_SPAWNED == "DESTROY_ALL":
                circles.clear()
        else:
            invulnerable = False
            dont_touch_me = False
            power_collected = False
            rune_spawned.clear()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player.x - PLAYER_VEL >= 0:
            player.x -= PLAYER_VEL
        if keys[pygame.K_RIGHT] and player.x + PLAYER_VEL + player.width <= WIDTH:
            player.x += PLAYER_VEL

        if keys[pygame.K_UP] and player.y - PLAYER_VEL >= 0:
            player.y -= PLAYER_VEL
        if keys[pygame.K_DOWN] and player.y + PLAYER_VEL + player.height <= HEIGHT:
            player.y += PLAYER_VEL


        if hit is True and invulnerable is False:
            lost_text = FONT.render("You Lost!", 1, "white")
            screen.blit(lost_text, (WIDTH/2 - lost_text.get_width()/2, HEIGHT/2 - lost_text.get_height()/2))
            pygame.display.update()
            pygame.time.delay(4000)
            break

        draw(player, circles, powers, elapsed_time, POWER_COLOR, rune_spawned)
        clock.tick(60)

    pygame.quit()


if __name__ == "__main__":
    main()
