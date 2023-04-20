import pygame
import time
import math
pygame.font.init()

WIDTH, HEIGHT = 1200, 800
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("PANG")

BG_COLOR = "White"

PLAYER_WIDTH = 40
PLAYER_HEIGHT = 20
PLAYER_VEL = 10

CIRCLE_RADIUS = 60
circle_x = int(WIDTH * 0.10)
circle_y = HEIGHT - CIRCLE_RADIUS  # start at bottom of screen
circle_speed = 5
circle_speed_x = 5
circle_speed_y = 5

path_radius = 200

FONT = pygame.font.SysFont("comicsans", 30)


def create_circle():
    x = CIRCLE_RADIUS
    y = HEIGHT * 0.50
    circle = pygame.Rect(x - CIRCLE_RADIUS, y - CIRCLE_RADIUS, CIRCLE_RADIUS * 2, CIRCLE_RADIUS * 2), circle_speed_x, circle_speed_y
    return circle


def draw(triangle_vertices, fire, elapsed_time, circle):
    WIN.fill(BG_COLOR)

    time_text = FONT.render(f"Time: {round(elapsed_time)}s", 1, "white")
    WIN.blit(time_text, (10, 10))

    pygame.draw.line(WIN, "red", fire[0], fire[1], 5)
    # pygame.draw.rect(WIN, "red", fire)
    pygame.draw.polygon(WIN, "red", triangle_vertices)

    pygame.draw.circle(WIN, "green", circle.center, CIRCLE_RADIUS)

    pygame.display.update()


def main():
    clock = pygame.time.Clock()
    run = True

    go_right = True

    path_center_y = WIDTH * 0.55
    path_center_x = 150
    shift_factor_x = -50
    shift_factor_y = -300

    path_angle = 90

    circle, vx, vy = create_circle()

    fire_allowed = True
    fire_anchor = False

    hit = False

    fire = [(0,0), (0,0)]

    player_spawn = (WIDTH / 2) - (PLAYER_WIDTH / 2)
    triangle_vertices = [(player_spawn, HEIGHT), ((PLAYER_WIDTH / 2) + player_spawn, HEIGHT - PLAYER_HEIGHT),
                         (PLAYER_WIDTH + player_spawn, HEIGHT)]

    bullet_anchor_size = HEIGHT
    bullet_position = 0

    start_time = time.time()
    line_draw_delay = time.time() + 0.03

    while run:
        elapsed_time = time.time() - start_time
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

        if go_right:
            path_angle += int(circle_speed / 2)
        else:
            path_angle -= int(circle_speed / 2)

        circle.x = path_center_x - math.cos(math.radians(path_angle)) * path_radius + shift_factor_x * math.cos(
            math.radians(path_angle))
        circle.y = path_center_y - math.sin(
            math.radians(path_angle)) * path_radius + shift_factor_y * math.sin(
            math.radians(path_angle))
        turn = True

        if circle.y >= HEIGHT - (CIRCLE_RADIUS * 2):
            shift_factor_x += 5
            shift_factor_y += 50
            if turn:
                if go_right:
                    path_center_x = circle.x + path_radius + abs(shift_factor_x)
                    path_angle = 0
                    turn = False
                else:
                    path_center_x = circle.x - path_radius - abs(shift_factor_x)
                    path_angle = 180
                    turn = False

        if circle.x <= 0:
            go_right = True
        elif circle.x + (CIRCLE_RADIUS * 2) >= WIDTH:
            go_right = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and triangle_vertices[0][0] >= 0:
            player_spawn -= PLAYER_VEL
            triangle_vertices = [(player_spawn, HEIGHT), ((PLAYER_WIDTH / 2) + player_spawn, HEIGHT - PLAYER_HEIGHT),
                                 (PLAYER_WIDTH + player_spawn, HEIGHT)]
        if keys[pygame.K_RIGHT] and triangle_vertices[-1][0] <= WIDTH:
            player_spawn += PLAYER_VEL
            triangle_vertices = [(player_spawn, HEIGHT), ((PLAYER_WIDTH / 2) + player_spawn, HEIGHT - PLAYER_HEIGHT),
                                 (PLAYER_WIDTH + player_spawn, HEIGHT)]

        if fire_allowed:
            if keys[pygame.K_SPACE]:
                fire_anchor = True
                fire_allowed = False
                bullet_position = triangle_vertices[1][0]

        if fire_anchor:
            if time.time() > line_draw_delay:
                bullet_anchor_size -= 20
                fire = [(bullet_position, HEIGHT), (bullet_position, bullet_anchor_size)]
                line_draw_delay = time.time() + 0.03
            if abs(bullet_anchor_size) <= 0:
                fire_anchor = False
                fire_allowed = True
                fire = [(0,0), (0,0)]
                bullet_anchor_size = HEIGHT

        if hit:
            lost_text = FONT.render("You Lost!", 1, "white")
            WIN.blit(lost_text, (WIDTH/2 - lost_text.get_width()/2, HEIGHT/2 - lost_text.get_height()/2))
            pygame.display.update()
            pygame.time.delay(4000)
            break

        draw(triangle_vertices, fire, elapsed_time, circle)
        clock.tick(60)

    pygame.quit()


if __name__ == "__main__":
    main()
