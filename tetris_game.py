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

rect_width = 20
rect_height = 20
rect_x = (WIDTH / 2) - (rect_width / 2)
rect_y = 10
vel_y = 20
vel_x = 20

bottom_bricks = []
bottom_bricks_border = []
placed_bricks = ""

block_color = "blue"

border_width = 2
border_color = "white"

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
            blocks.append((block, vel_x, vel_y))
            borders.append((border_of_block, vel_x, vel_y))
        else:
            x_axis -= (rect_width * 2)
            block = pygame.Rect(x_axis + border_width, y_axis + border_width, rect_width - 2 * border_width,
                                rect_height - 2 * border_width)
            border_of_block = pygame.Rect(x_axis, y_axis, rect_width, rect_height)
            blocks.append((block, vel_x, vel_y))
            borders.append((border_of_block, vel_x, vel_y))

    all_rotations_blocks.append(blocks)
    all_rotations_borders.append(borders)
    blocks = []
    borders = []

    x_axis = rect_x + (rect_width * 2)
    y_axis = rect_y
    for i in range(4):
        if i <= 2:
            block = pygame.Rect(x_axis + border_width, y_axis + border_width, rect_width - 2 * border_width,
                                rect_height - 2 * border_width)
            border_of_block = pygame.Rect(x_axis, y_axis, rect_width, rect_height)
            y_axis += rect_height
            blocks.append((block, vel_x, vel_y))
            borders.append((border_of_block, vel_x, vel_y))
        else:
            y_axis -= (rect_height * 2)
            x_axis -= rect_width
            block = pygame.Rect(x_axis + border_width, y_axis + border_width, rect_width - 2 * border_width,
                                rect_height - 2 * border_width)
            border_of_block = pygame.Rect(x_axis, y_axis, rect_width, rect_height)
            blocks.append((block, vel_x, vel_y))
            borders.append((border_of_block, vel_x, vel_y))

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
            blocks.append((block, vel_x, vel_y))
            borders.append((border_of_block, vel_x, vel_y))
        else:
            x_axis -= (rect_width * 2)
            block = pygame.Rect(x_axis + border_width, rect_y + border_width, rect_width - 2 * border_width,
                                rect_height - 2 * border_width)
            border_of_block = pygame.Rect(x_axis, rect_y, rect_width, rect_height)
            blocks.append((block, vel_x, vel_y))
            borders.append((border_of_block, vel_x, vel_y))

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
            blocks.append((block, vel_x, vel_y))
            borders.append((border_of_block, vel_x, vel_y))
        else:
            y_axis -= (rect_height * 2)
            block = pygame.Rect(x_axis + border_width, y_axis + border_width, rect_width - 2 * border_width,
                                rect_height - 2 * border_width)
            border_of_block = pygame.Rect(x_axis, y_axis, rect_width, rect_height)
            blocks.append((block, vel_x, vel_y))
            borders.append((border_of_block, vel_x, vel_y))

    all_rotations_blocks.append(blocks)
    all_rotations_borders.append(borders)

    blocks = all_rotations_blocks
    borders = all_rotations_borders

    return blocks, borders


def l_l_shape():
    blocks = []
    borders = []
    all_rotations_blocks = []
    all_rotations_borders = []

    x_axis = rect_x + (rect_width * 2)
    y_axis = rect_y
    for i in range(4):
        if i <= 2:
            block = pygame.Rect(x_axis + border_width, y_axis + border_width, rect_width - 2 * border_width,
                                rect_height - 2 * border_width)
            border_of_block = pygame.Rect(x_axis, y_axis, rect_width, rect_height)
            y_axis += rect_height
            blocks.append((block, vel_x, vel_y))
            borders.append((border_of_block, vel_x, vel_y))
        else:
            x_axis -= rect_width
            block = pygame.Rect(x_axis + border_width, rect_y + border_width, rect_width - 2 * border_width,
                                rect_height - 2 * border_width)
            border_of_block = pygame.Rect(x_axis, rect_y, rect_width, rect_height)
            blocks.append((block, vel_x, vel_y))
            borders.append((border_of_block, vel_x, vel_y))

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
            blocks.append((block, vel_x, vel_y))
            borders.append((border_of_block, vel_x, vel_y))
        else:
            x_axis -= rect_width
            block = pygame.Rect(x_axis + border_width, rect_y + border_width, rect_width - 2 * border_width,
                                rect_height - 2 * border_width)
            border_of_block = pygame.Rect(x_axis, rect_y, rect_width, rect_height)
            blocks.append((block, vel_x, vel_y))
            borders.append((border_of_block, vel_x, vel_y))

    all_rotations_blocks.append(blocks)
    all_rotations_borders.append(borders)
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
            blocks.append((block, vel_x, vel_y))
            borders.append((border_of_block, vel_x, vel_y))
        else:
            y_axis -= rect_height
            x_axis += rect_width
            block = pygame.Rect(x_axis + border_width, y_axis + border_width, rect_width - 2 * border_width,
                                rect_height - 2 * border_width)
            border_of_block = pygame.Rect(x_axis, y_axis, rect_width, rect_height)
            blocks.append((block, vel_x, vel_y))
            borders.append((border_of_block, vel_x, vel_y))

    all_rotations_blocks.append(blocks)
    all_rotations_borders.append(borders)
    blocks = []
    borders = []

    x_axis = rect_x
    y_axis = rect_y
    for i in range(4):
        if i <= 2:
            block = pygame.Rect(x_axis + border_width, y_axis + border_width, rect_width - 2 * border_width,
                                rect_height - 2 * border_width)
            border_of_block = pygame.Rect(x_axis, y_axis, rect_width, rect_height)
            x_axis += rect_width
            blocks.append((block, vel_x, vel_y))
            borders.append((border_of_block, vel_x, vel_y))
        else:
            y_axis += rect_height
            block = pygame.Rect(rect_x + border_width, y_axis + border_width, rect_width - 2 * border_width,
                                rect_height - 2 * border_width)
            border_of_block = pygame.Rect(rect_x, y_axis, rect_width, rect_height)
            blocks.append((block, vel_x, vel_y))
            borders.append((border_of_block, vel_x, vel_y))

    all_rotations_blocks.append(blocks)
    all_rotations_borders.append(borders)

    blocks = all_rotations_blocks
    borders = all_rotations_borders

    return blocks, borders

def l_r_shape():
    blocks = []
    borders = []
    all_rotations_blocks = []
    all_rotations_borders = []

    x_axis = rect_x
    y_axis = rect_y
    for i in range(4):
        if i <= 2:
            block = pygame.Rect(x_axis + border_width, y_axis + border_width, rect_width - 2 * border_width,
                                rect_height - 2 * border_width)
            border_of_block = pygame.Rect(x_axis, y_axis, rect_width, rect_height)
            y_axis += rect_width
            blocks.append((block, vel_x, vel_y))
            borders.append((border_of_block, vel_x, vel_y))
        else:
            x_axis += rect_width
            block = pygame.Rect(x_axis + border_width, rect_y + border_width, rect_width - 2 * border_width,
                                rect_height - 2 * border_width)
            border_of_block = pygame.Rect(x_axis, rect_y, rect_width, rect_height)
            blocks.append((block, vel_x, vel_y))
            borders.append((border_of_block, vel_x, vel_y))

    all_rotations_blocks.append(blocks)
    all_rotations_borders.append(borders)
    blocks = []
    borders = []

    x_axis = rect_x
    y_axis = rect_y
    for i in range(4):
        if i <= 2:
            block = pygame.Rect(x_axis + border_width, y_axis + border_width, rect_width - 2 * border_width,
                                rect_height - 2 * border_width)
            border_of_block = pygame.Rect(x_axis, y_axis, rect_width, rect_height)
            x_axis += rect_width
            blocks.append((block, vel_x, vel_y))
            borders.append((border_of_block, vel_x, vel_y))
        else:
            x_axis -= rect_width
            y_axis += rect_height
            block = pygame.Rect(x_axis + border_width, y_axis + border_width, rect_width - 2 * border_width,
                                rect_height - 2 * border_width)
            border_of_block = pygame.Rect(x_axis, y_axis, rect_width, rect_height)
            blocks.append((block, vel_x, vel_y))
            borders.append((border_of_block, vel_x, vel_y))

    all_rotations_blocks.append(blocks)
    all_rotations_borders.append(borders)
    blocks = []
    borders = []

    x_axis = rect_x + (rect_width * 2)
    y_axis = rect_y
    for i in range(4):
        if i <= 2:
            block = pygame.Rect(x_axis + border_width, y_axis + border_width, rect_width - 2 * border_width,
                                rect_height - 2 * border_width)
            border_of_block = pygame.Rect(x_axis, y_axis, rect_width, rect_height)
            y_axis += rect_height
            blocks.append((block, vel_x, vel_y))
            borders.append((border_of_block, vel_x, vel_y))
        else:
            x_axis -= rect_width
            y_axis -= rect_height
            block = pygame.Rect(x_axis + border_width, y_axis + border_width, rect_width - 2 * border_width,
                                rect_height - 2 * border_width)
            border_of_block = pygame.Rect(x_axis, y_axis, rect_width, rect_height)
            blocks.append((block, vel_x, vel_y))
            borders.append((border_of_block, vel_x, vel_y))

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
            blocks.append((block, vel_x, vel_y))
            borders.append((border_of_block, vel_x, vel_y))
        else:
            y_axis -= rect_height
            block = pygame.Rect(rect_x + border_width, rect_y + border_width, rect_width - 2 * border_width,
                                rect_height - 2 * border_width)
            border_of_block = pygame.Rect(rect_x, rect_y, rect_width, rect_height)
            blocks.append((block, vel_x, vel_y))
            borders.append((border_of_block, vel_x, vel_y))

    all_rotations_blocks.append(blocks)
    all_rotations_borders.append(borders)

    blocks = all_rotations_blocks
    borders = all_rotations_borders

    return blocks, borders


def s_l_shape():
    blocks = []
    borders = []
    all_rotations_blocks = []
    all_rotations_borders = []

    x_axis = rect_x
    y_axis = rect_y
    for i in range(4):
        if i <= 1:
            block = pygame.Rect(rect_x + border_width, y_axis + border_width, rect_width - 2 * border_width,
                                rect_height - 2 * border_width)
            border_of_block = pygame.Rect(rect_x, y_axis, rect_width, rect_height)
            y_axis += rect_height
            blocks.append((block, vel_x, vel_y))
            borders.append((border_of_block, vel_x, vel_y))
        elif i <= 2:
            x_axis += rect_width
            y_axis -= rect_height
            block = pygame.Rect(x_axis + border_width, y_axis + border_width, rect_width - 2 * border_width,
                                rect_height - 2 * border_width)
            border_of_block = pygame.Rect(x_axis, y_axis, rect_width, rect_height)
            y_axis += rect_height
            blocks.append((block, vel_x, vel_y))
            borders.append((border_of_block, vel_x, vel_y))
        else:
            block = pygame.Rect(x_axis + border_width, y_axis + border_width, rect_width - 2 * border_width,
                                rect_height - 2 * border_width)
            border_of_block = pygame.Rect(x_axis, y_axis, rect_width, rect_height)
            blocks.append((block, vel_x, vel_y))
            borders.append((border_of_block, vel_x, vel_y))

    all_rotations_blocks.append(blocks)
    all_rotations_borders.append(borders)
    blocks = []
    borders = []

    x_axis = rect_x
    y_axis = rect_y + rect_height
    for i in range(4):
        if i <= 1:
            block = pygame.Rect(x_axis + border_width, y_axis + border_width, rect_width - 2 * border_width,
                                rect_height - 2 * border_width)
            border_of_block = pygame.Rect(x_axis, y_axis, rect_width, rect_height)
            x_axis += rect_width
            blocks.append((block, vel_x, vel_y))
            borders.append((border_of_block, vel_x, vel_y))
        elif i <= 2:
            x_axis -= rect_width
            y_axis -= rect_height
            block = pygame.Rect(x_axis + border_width, y_axis + border_width, rect_width - 2 * border_width,
                                rect_height - 2 * border_width)
            border_of_block = pygame.Rect(x_axis, y_axis, rect_width, rect_height)
            x_axis += rect_width
            blocks.append((block, vel_x, vel_y))
            borders.append((border_of_block, vel_x, vel_y))
        else:
            block = pygame.Rect(x_axis + border_width, y_axis + border_width, rect_width - 2 * border_width,
                                rect_height - 2 * border_width)
            border_of_block = pygame.Rect(x_axis, y_axis, rect_width, rect_height)
            blocks.append((block, vel_x, vel_y))
            borders.append((border_of_block, vel_x, vel_y))

    all_rotations_blocks.append(blocks)
    all_rotations_borders.append(borders)

    # random_choice = random.randint(0, 3)
    #
    # blocks = all_rotations_blocks[random_choice]
    # borders = all_rotations_borders[random_choice]

    blocks = all_rotations_blocks
    borders = all_rotations_borders

    return blocks, borders


def s_r_shape():
    blocks = []
    borders = []
    all_rotations_blocks = []
    all_rotations_borders = []

    x_axis = rect_x
    y_axis = rect_y
    for i in range(4):
        if i <= 1:
            block = pygame.Rect(x_axis + border_width, rect_y + border_width, rect_width - 2 * border_width,
                                rect_height - 2 * border_width)
            border_of_block = pygame.Rect(x_axis, rect_y, rect_width, rect_height)
            x_axis += rect_width
            blocks.append((block, vel_x, vel_y))
            borders.append((border_of_block, vel_x, vel_y))
        elif i <= 2:
            x_axis -= rect_width
            y_axis += rect_height
            block = pygame.Rect(x_axis + border_width, y_axis + border_width, rect_width - 2 * border_width,
                                rect_height - 2 * border_width)
            border_of_block = pygame.Rect(x_axis, y_axis, rect_width, rect_height)
            x_axis += rect_width
            blocks.append((block, vel_x, vel_y))
            borders.append((border_of_block, vel_x, vel_y))
        else:
            block = pygame.Rect(x_axis + border_width, y_axis + border_width, rect_width - 2 * border_width,
                                rect_height - 2 * border_width)
            border_of_block = pygame.Rect(x_axis, y_axis, rect_width, rect_height)
            blocks.append((block, vel_x, vel_y))
            borders.append((border_of_block, vel_x, vel_y))

    all_rotations_blocks.append(blocks)
    all_rotations_borders.append(borders)
    blocks = []
    borders = []

    x_axis = rect_x + rect_width
    y_axis = rect_y
    for i in range(4):
        if i <= 1:
            block = pygame.Rect(x_axis + border_width, y_axis + border_width, rect_width - 2 * border_width,
                                rect_height - 2 * border_width)
            border_of_block = pygame.Rect(x_axis, y_axis, rect_width, rect_height)
            y_axis += rect_height
            blocks.append((block, vel_x, vel_y))
            borders.append((border_of_block, vel_x, vel_y))
        elif i <= 2:
            x_axis -= rect_width
            y_axis -= rect_height
            block = pygame.Rect(x_axis + border_width, y_axis + border_width, rect_width - 2 * border_width,
                                rect_height - 2 * border_width)
            border_of_block = pygame.Rect(x_axis, y_axis, rect_width, rect_height)
            y_axis += rect_height
            blocks.append((block, vel_x, vel_y))
            borders.append((border_of_block, vel_x, vel_y))
        else:
            block = pygame.Rect(x_axis + border_width, y_axis + border_width, rect_width - 2 * border_width,
                                rect_height - 2 * border_width)
            border_of_block = pygame.Rect(x_axis, y_axis, rect_width, rect_height)
            blocks.append((block, vel_x, vel_y))
            borders.append((border_of_block, vel_x, vel_y))

    all_rotations_blocks.append(blocks)
    all_rotations_borders.append(borders)

    # random_choice = random.randint(0, 3)
    #
    # blocks = all_rotations_blocks[random_choice]
    # borders = all_rotations_borders[random_choice]

    blocks = all_rotations_blocks
    borders = all_rotations_borders

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
            blocks.append((block, vel_x, vel_y))
            borders.append((border_of_block, vel_x, vel_y))
        elif i <= 2:
            x_axis = rect_x
            block = pygame.Rect(x_axis + border_width, y_axis + border_width, rect_width - 2 * border_width,
                                rect_height - 2 * border_width)
            border_of_block = pygame.Rect(x_axis, y_axis, rect_width, rect_height)
            blocks.append((block, vel_x, vel_y))
            borders.append((border_of_block, vel_x, vel_y))
        else:
            x_axis += rect_width
            block = pygame.Rect(x_axis + border_width, y_axis + border_width, rect_width - 2 * border_width,
                                rect_height - 2 * border_width)
            border_of_block = pygame.Rect(x_axis, y_axis, rect_width, rect_height)
            blocks.append((block, vel_x, vel_y))
            borders.append((border_of_block, vel_x, vel_y))

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
        blocks.append((block, vel_x, vel_y))
        borders.append((border_of_block, vel_x, vel_y))

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
        blocks.append((block, vel_x, vel_y))
        borders.append((border_of_block, vel_x, vel_y))

    all_rotations_blocks.append(blocks)
    all_rotations_borders.append(borders)

    blocks = all_rotations_blocks
    borders = all_rotations_borders

    return blocks, borders


def draw(shape, bottom_bricks, bottom_bricks_border):
    screen.fill(BG_COLOR)

    # pygame.draw.rect(screen, "white", border_of_block, border_width)
    # pygame.draw.rect(screen, "blue", block)

    # cords = []
    # for block, border in zip(shape[0], shape[1]):
    #     pygame.draw.rect(screen, border_color, border, border_width)
    #     pygame.draw.rect(screen, block_color, block)
    #     cords.append((block.x, block.y))

    for i, (rect, vx, vy) in enumerate(shape[1]):
        pygame.draw.rect(screen, border_color, rect, border_width)

    for i, (rect, vx, vy) in enumerate(shape[0]):
        pygame.draw.rect(screen, block_color, rect)


    for i, (rect, vx, vy) in enumerate(bottom_bricks_border):
        pygame.draw.rect(screen, border_color, rect, border_width)

    for i, (rect, vx, vy) in enumerate(bottom_bricks):
        pygame.draw.rect(screen, block_color, rect)


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
    next_spawn = True


    # block = pygame.Rect(rect_x + border_width, rect_y + border_width, rect_width - 2 * border_width, rect_height - 2 * border_width)
    # border_of_block = pygame.Rect(rect_x, rect_y, rect_width, rect_height)

    bar = bar_shape()
    box = box_shape()
    t = t_shape()
    s_l = s_l_shape()
    s_r = s_r_shape()
    l_l = l_l_shape()
    l_r = l_r_shape()

    shapes = random.choice([bar, box, t, s_l, s_r, l_l, l_r])
    rotation = 0


    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        if next_spawn:
            shapes = random.choice([bar, box, t, s_l, s_r, l_l, l_r])
            next_spawn = False

        if not shapes == box:
            if shapes == bar or shapes == s_r or shapes == s_l:
                rotationx = random.randint(0,1)
            else:
                rotationx = random.randint(0, 3)
            shape = shapes[0][rotation], shapes[1][rotation]
        else:
            shape = box

        if not next_spawn:
            for i, (rect, vx, vy) in enumerate(shape[0]):
                rect.y += vel_y
            for i, (rect, vx, vy) in enumerate(shape[1]):
                rect.y += vel_y

        for i, (rect, vx, vy) in enumerate(shape[0]):
            if rect.bottom + rect_height >= HEIGHT:
                bottom_bricks.append((rect, vx, vy))
                next_spawn = True

        for i, (rect, vx, vy) in enumerate(shape[1]):
            if rect.bottom + rect_height >= HEIGHT:
                bottom_bricks_border.append((rect, vx, vy))
                next_spawn = True


        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            if shapes == box:
                pass
            elif shapes == bar or shapes == s_l or shapes == s_r:
                if rotation < 1:
                    rotation += 1
                else:
                    rotation = 0
            else:
                if rotation < 3:
                    rotation += 1
                else:
                    rotation = 0

        if keys[pygame.K_LEFT]:
            state = True
            for i, (rect, vx, vy) in enumerate(shape[1]):
                if rect.x - rect_width < 0:
                    state = False
            if state:
                for i, (rect, vx, vy) in enumerate(shape[1]):
                    if not rect.x < 0:
                        rect.x -= vel_x
                        shape[1][i] = (rect, vx, vy)

                for i, (rect, vx, vy) in enumerate(shape[0]):
                    if not rect.x < 0:
                        rect.x -= vel_x
                        shape[0][i] = (rect, vx, vy)

        if keys[pygame.K_RIGHT]:
            state = True
            for i, (rect, vx, vy) in enumerate(shape[0]):
                if rect.right + rect_width >= WIDTH:
                    state = False
            if state:
                for i, (rect, vx, vy) in enumerate(shape[1]):
                    rect.x += vel_x
                    shape[1][i] = (rect, vx, vy)

                for i, (rect, vx, vy) in enumerate(shape[0]):
                    rect.x += vel_x
                    shape[0][i] = (rect, vx, vy)

        if keys[pygame.K_DOWN]:
            state = True
            for i, (rect, vx, vy) in enumerate(shape[0]):
                if rect.bottom + rect_height >= HEIGHT:
                    state = False
            if state:
                for i, (rect, vx, vy) in enumerate(shape[1]):
                    rect.y += vel_y
                    shape[1][i] = (rect, vx, vy)

                for i, (rect, vx, vy) in enumerate(shape[0]):
                    rect.y += vel_y
                    shape[0][i] = (rect, vx, vy)

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


        clock.tick(8)
        draw(shape, bottom_bricks, bottom_bricks_border)


if __name__ == "__main__":
    main()
