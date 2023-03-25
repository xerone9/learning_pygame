import pygame
import pygame.mixer
import random
import math
import time


pygame.font.init()
pygame.mixer.init()
pygame.init()

pygame.display.set_caption("Tetris")

# Define constants
WIDTH = 800
HEIGHT = 600
BG_COLOR = (0,0,0)

BALL_RADIUS = 20
BALL_COLOR = "dark orange"
BALL_VEL_X = 2
BALL_VEL_Y = 2

NO_OF_BALLS = 41 # Odd Number Only (Still dont know whats the bug)

rect_width = 20
rect_height = 20
rect_x = (WIDTH / 2) - (rect_width / 2)
rect_y = 10
block_color = "blue"

border_width = 2
border_color = "white"

CORDS = []
CIRCLES = []

screen = pygame.display.set_mode((WIDTH, HEIGHT))
FONT = pygame.font.SysFont("comicsans", 30)


def t_shape():
    blocks = []
    borders = []
    all_rotations_blocks = []
    all_rotations_borders = []
    x_axis = rect_x
    y_axis = rect_y + rect_height

    for i in range(4):
        if i <= 2:
            block = pygame.Rect(x_axis + border_width, rect_y + border_width, rect_width - 2 * border_width,
                                rect_height - 2 * border_width)
            border_of_block = pygame.Rect(x_axis, rect_y, rect_width, rect_height)
            x_axis += rect_width
            blocks.append(block)
            borders.append(border_of_block)
        else:
            x_axis -= (rect_width * 2)
            block = pygame.Rect(x_axis + border_width, y_axis + border_width, rect_width - 2 * border_width,
                                rect_height - 2 * border_width)
            border_of_block = pygame.Rect(x_axis, y_axis, rect_width, rect_height)
            blocks.append(block)
            borders.append(border_of_block)

    all_rotations_blocks.append(blocks)
    all_rotations_borders.append(borders)
    blocks = []
    borders = []

    x_axis = rect_x
    y_axis = rect_y + rect_height

    for i in range(4):
        if i <= 2:
            block = pygame.Rect(x_axis + border_width, y_axis + border_width, rect_width - 2 * border_width,
                                rect_height - 2 * border_width)
            border_of_block = pygame.Rect(x_axis, y_axis, rect_width, rect_height)
            x_axis += rect_width
            blocks.append(block)
            borders.append(border_of_block)
        else:
            x_axis -= (rect_width * 2)
            block = pygame.Rect(x_axis + border_width, rect_y + border_width, rect_width - 2 * border_width,
                                rect_height - 2 * border_width)
            border_of_block = pygame.Rect(x_axis, rect_y, rect_width, rect_height)
            blocks.append(block)
            borders.append(border_of_block)

    all_rotations_blocks.append(blocks)
    all_rotations_borders.append(borders)
    blocks = []
    borders = []

    x_axis = rect_x + rect_width
    y_axis = rect_y
    for i in range(4):
        if i <= 2:
            block = pygame.Rect(rect_x + border_width, y_axis + border_width, rect_width - 2 * border_width,
                                rect_height - 2 * border_width)
            border_of_block = pygame.Rect(rect_x, y_axis, rect_width, rect_height)
            y_axis += rect_height
            blocks.append(block)
            borders.append(border_of_block)
        else:
            y_axis -= (rect_height * 2)
            block = pygame.Rect(x_axis + border_width, y_axis + border_width, rect_width - 2 * border_width,
                                rect_height - 2 * border_width)
            border_of_block = pygame.Rect(x_axis, y_axis, rect_width, rect_height)
            blocks.append(block)
            borders.append(border_of_block)

    all_rotations_blocks.append(blocks)
    all_rotations_borders.append(borders)
    blocks = []
    borders = []

    x_axis = rect_x - rect_width
    y_axis = rect_y
    for i in range(4):
        if i <= 2:
            block = pygame.Rect(rect_x + border_width, y_axis + border_width, rect_width - 2 * border_width,
                                rect_height - 2 * border_width)
            border_of_block = pygame.Rect(rect_x, y_axis, rect_width, rect_height)
            y_axis += rect_height
            blocks.append(block)
            borders.append(border_of_block)
        else:
            y_axis -= (rect_height * 2)
            block = pygame.Rect(x_axis + border_width, y_axis + border_width, rect_width - 2 * border_width,
                                rect_height - 2 * border_width)
            border_of_block = pygame.Rect(x_axis, y_axis, rect_width, rect_height)
            blocks.append(block)
            borders.append(border_of_block)

    all_rotations_blocks.append(blocks)
    all_rotations_borders.append(borders)

    random_choice = random.randint(0, 3)

    blocks = all_rotations_blocks[random_choice]
    borders = all_rotations_borders[random_choice]

    return blocks, borders


def l_shape():
    blocks = []
    borders = []
    x_axis = rect_x
    y_axis = rect_y

    for i in range(4):
        if i <= 2:
            block = pygame.Rect(x_axis + border_width, y_axis + border_width, rect_width - 2 * border_width,
                                rect_height - 2 * border_width)
            border_of_block = pygame.Rect(x_axis, y_axis, rect_width, rect_height)
            y_axis += rect_height
            blocks.append(block)
            borders.append(border_of_block)
        else:
            x_axis += rect_width
            block = pygame.Rect(x_axis + border_width, rect_y + border_width, rect_width - 2 * border_width,
                                rect_height - 2 * border_width)
            border_of_block = pygame.Rect(x_axis, rect_y, rect_width, rect_height)
            blocks.append(block)
            borders.append(border_of_block)

    return blocks, borders


def s_shape():
    blocks = []
    borders = []
    x_axis = rect_x
    y_axis = rect_y

    for i in range(4):
        if i <= 1:
            block = pygame.Rect(rect_x + border_width, y_axis + border_width, rect_width - 2 * border_width,
                                rect_height - 2 * border_width)
            border_of_block = pygame.Rect(rect_x, y_axis, rect_width, rect_height)
            y_axis += rect_height
            blocks.append(block)
            borders.append(border_of_block)
        elif i <= 2:
            x_axis += rect_width
            y_axis -= rect_height
            block = pygame.Rect(x_axis + border_width, y_axis + border_width, rect_width - 2 * border_width,
                                rect_height - 2 * border_width)
            border_of_block = pygame.Rect(x_axis, y_axis, rect_width, rect_height)
            y_axis += rect_height
            blocks.append(block)
            borders.append(border_of_block)
        else:
            block = pygame.Rect(x_axis + border_width, y_axis + border_width, rect_width - 2 * border_width,
                                rect_height - 2 * border_width)
            border_of_block = pygame.Rect(x_axis, y_axis, rect_width, rect_height)
            blocks.append(block)
            borders.append(border_of_block)

    return blocks, borders


def box_shape():
    blocks = []
    borders = []
    x_axis = rect_x
    y_axis = rect_y + rect_height

    for i in range(4):
        if i <= 1:
            block = pygame.Rect(x_axis + border_width, rect_y + border_width, rect_width - 2 * border_width,
                                rect_height - 2 * border_width)
            border_of_block = pygame.Rect(x_axis, rect_y, rect_width, rect_height)
            x_axis += rect_width
            blocks.append(block)
            borders.append(border_of_block)
        elif i <= 2:
            x_axis = rect_x
            block = pygame.Rect(x_axis + border_width, y_axis + border_width, rect_width - 2 * border_width,
                                rect_height - 2 * border_width)
            border_of_block = pygame.Rect(x_axis, y_axis, rect_width, rect_height)
            blocks.append(block)
            borders.append(border_of_block)
        else:
            x_axis += rect_width
            block = pygame.Rect(x_axis + border_width, y_axis + border_width, rect_width - 2 * border_width,
                                rect_height - 2 * border_width)
            border_of_block = pygame.Rect(x_axis, y_axis, rect_width, rect_height)
            blocks.append(block)
            borders.append(border_of_block)

    return blocks, borders


def bar_shape():
    blocks = []
    all_rotations_blocks = []
    borders = []
    all_rotations_borders = []
    x_axis = rect_x
    for i in range(4):
        block = pygame.Rect(x_axis + border_width, rect_y + border_width, rect_width - 2 * border_width,
                            rect_height - 2 * border_width)
        border_of_block = pygame.Rect(x_axis, rect_y, rect_width, rect_height)
        x_axis += rect_width
        blocks.append(block)
        borders.append(border_of_block)

    all_rotations_blocks.append(blocks)
    all_rotations_borders.append(borders)

    blocks = []
    borders = []
    y_axis = rect_y
    for i in range(4):
        block = pygame.Rect(rect_x + border_width, y_axis + border_width, rect_width - 2 * border_width,
                            rect_height - 2 * border_width)
        border_of_block = pygame.Rect(rect_x, y_axis, rect_width, rect_height)
        y_axis += rect_height
        blocks.append(block)
        borders.append(border_of_block)

    all_rotations_blocks.append(blocks)
    all_rotations_borders.append(borders)

    random_choice = random.randint(0,1)

    blocks = all_rotations_blocks[random_choice]
    borders = all_rotations_borders[random_choice]

    return blocks, borders


def draw(shape):
    screen.fill(BG_COLOR)

    # pygame.draw.rect(screen, "white", border_of_block, border_width)
    # pygame.draw.rect(screen, "blue", block)

    cords = []
    for block, border in zip(shape[0], shape[1]):
        pygame.draw.rect(screen, border_color, border, border_width)
        pygame.draw.rect(screen, block_color, block)
        cords.append((block.x, block.y))

    # new_x = cords[-1][0]
    # new_y = cords[-1][1]
    #
    # rotated_cords = []
    #
    # for i in range(len(cords)):
    #     rotated_cords.append((new_x, new_y))
    #     new_y += rect_width
    #
    # for block, border, cords in zip(shape[0], shape[1], rotated_cords):
    #     border.x, border.y = (cords[0] - 2, cords[1]-2)
    #     block.x, block.y = cords






    pygame.display.update()


def main():
    clock = pygame.time.Clock()

    # block = pygame.Rect(rect_x + border_width, rect_y + border_width, rect_width - 2 * border_width, rect_height - 2 * border_width)
    # border_of_block = pygame.Rect(rect_x, rect_y, rect_width, rect_height)

    bar = bar_shape()
    box = box_shape()
    t = t_shape()
    s = s_shape()
    l = l_shape()

    # shape = random.choice([bar, box, t, s, l])
    shape = t

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            cords = []
            for block, border in zip(shape[0], shape[1]):
                cords.append((block.x, block.y))

            new_x = cords[-1][0]
            new_y = cords[-1][1]

            rotated_cords = []

            for i in range(len(cords)):
                rotated_cords.append((new_x, new_y))
                new_y += rect_width

            for block, border, cords in zip(shape[0], shape[1], rotated_cords):
                border.x, border.y = (cords[0] - 2, cords[1] - 2)
                block.x, block.y = cords

        # if keys[pygame.K_LEFT] and player.x - PLAYER_VEL >= 0:
        #     start = True
        #     player.x -= PLAYER_VEL
        # if keys[pygame.K_RIGHT] and player.x + PLAYER_VEL + player.width <= WIDTH:
        #     start = True
        #     player.x += PLAYER_VEL
        #
        # if keys[pygame.K_DOWN] and player.y + PLAYER_VEL + player.height <= HEIGHT:
        #     start = True
        #     player.y += PLAYER_VEL


        # if hit:
        #     lost_text = FONT.render("You Lost!", 1, "white")
        #     screen.blit(lost_text, (WIDTH / 2 - lost_text.get_width() / 2, HEIGHT / 2 - lost_text.get_height() / 2))
        #     pygame.display.update()
        #     pygame.time.delay(5000)
        #     break


        clock.tick(10)
        draw(shape)


if __name__ == "__main__":
    main()
