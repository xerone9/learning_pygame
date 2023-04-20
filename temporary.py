import pygame
import math

pygame.init()

# set up the display window
screen_width = 1200
screen_height = 800
screen = pygame.display.set_mode((screen_width, screen_height))

CIRCLE_RADIUS = 60
circle_x = int(screen_width * 0.10)
circle_y = screen_height - CIRCLE_RADIUS  # start at bottom of screen
circle_speed = 5
circle_speed_x = 5
circle_speed_y = 5
circle_direction = "path"

# set up circular path variables

path_radius = 200
path_angle = 90


def create_circle():
    x = CIRCLE_RADIUS
    y = screen_height * 0.50
    circle = pygame.Rect(x - CIRCLE_RADIUS, y - CIRCLE_RADIUS, CIRCLE_RADIUS * 2, CIRCLE_RADIUS * 2), circle_speed_x, circle_speed_y
    return circle


def draw(circle):
    pygame.draw.circle(screen, "green", circle.center, CIRCLE_RADIUS)

# game loop
running = True

turn = True
go_right = True

path_center_y = screen_width * 0.55
path_center_x = 150
shift_factor_x = -50
shift_factor_y = -300

circle, vx, vy = create_circle()

while running:
    # event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if go_right:
        path_angle += int(circle_speed / 2)
    else:
        path_angle -= int(circle_speed / 2)

    circle.x = path_center_x - math.cos(math.radians(path_angle)) * path_radius + shift_factor_x * math.cos(
    math.radians(path_angle))
    circle.y = path_center_y - math.sin(math.radians(path_angle)) * path_radius + shift_factor_y * math.sin(
    math.radians(path_angle))
    turn = True

    if circle.y >= screen_height - (CIRCLE_RADIUS * 2):
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
    elif circle.x + (CIRCLE_RADIUS * 2) >= screen_width:
        go_right = False

    print(shift_factor_x)
    screen.fill((255, 255, 255))
    draw(circle)
    pygame.display.update()

    # limit the frame rate to 60 fps
    pygame.time.Clock().tick(60)

pygame.quit()
