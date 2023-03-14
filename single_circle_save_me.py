import pygame
import random
import time

pygame.font.init()
pygame.display.set_caption("Save Me")

# Define constants

WIDTH = 800
HEIGHT = 600
BG_COLOR = (0, 0, 0)

CIRCLE_RADIUS = 11
CIRCLE_COLOR = (255, 140, 0)
CIRCLE_VELOCITY = 5

PLAYER_WIDTH = 20
PLAYER_HEIGHT = 20
PLAYER_VEL = 5

screen = pygame.display.set_mode((WIDTH, HEIGHT))
FONT = pygame.font.SysFont("comicsans", 30)


def create_circle():
    x = random.randint(CIRCLE_RADIUS, WIDTH - CIRCLE_RADIUS)
    y = CIRCLE_RADIUS
    vx = random.choice([-CIRCLE_VELOCITY, CIRCLE_VELOCITY])
    vy = random.choice([-CIRCLE_VELOCITY, CIRCLE_VELOCITY])
    circle = pygame.Rect(x - CIRCLE_RADIUS, y - CIRCLE_RADIUS, CIRCLE_RADIUS * 2, CIRCLE_RADIUS * 2), vx, vy
    return circle


def draw_circle(surface, color, position, radius):
    pygame.draw.circle(surface, color, position, radius)


def create_player():
    player = pygame.Rect((WIDTH / 2) - PLAYER_WIDTH, (HEIGHT / 2) - PLAYER_HEIGHT,
                         PLAYER_WIDTH, PLAYER_HEIGHT)
    return player


def draw_player(player):
    pygame.draw.rect(screen, "red", player)


def main():
    player = create_player()

    clock = pygame.time.Clock()

    # Keep track of the circle
    circle, vx, vy = create_circle()

    start_time = time.time()

    # Game loop
    running = True
    hit = False

    while running:
        elapsed_time = time.time() - start_time
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Move the circle
        circle.move_ip(vx, vy)

        # Bounce off the walls
        if circle.left < 0 or circle.right > WIDTH:
            vx = -vx
        if circle.top < 0 or circle.bottom > HEIGHT:
            vy = -vy

        # Draw the circle
        screen.fill(BG_COLOR)
        time_text = FONT.render(f"Time: {round(elapsed_time)}s", 1, "white")
        screen.blit(time_text, (10, 10))
        draw_player(player)
        draw_circle(screen, CIRCLE_COLOR, circle.center, CIRCLE_RADIUS)
        if circle.colliderect(player):
            hit = True

        pygame.display.flip()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player.x - PLAYER_VEL >= 0:
            player.x -= PLAYER_VEL
        if keys[pygame.K_RIGHT] and player.x + PLAYER_VEL + player.width <= WIDTH:
            player.x += PLAYER_VEL

        if keys[pygame.K_UP] and player.y - PLAYER_VEL >= 0:
            player.y -= PLAYER_VEL
        if keys[pygame.K_DOWN] and player.y + PLAYER_VEL + player.height <= HEIGHT:
            player.y += PLAYER_VEL

        if hit:
            lost_text = FONT.render("You Lost!", 1, "white")
            screen.blit(lost_text, (WIDTH/2 - lost_text.get_width()/2, HEIGHT/2 - lost_text.get_height()/2))
            pygame.display.update()
            pygame.time.delay(4000)
            break

        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()

