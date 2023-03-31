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
WIDTH = 400
HEIGHT = 400
BG_COLOR = (0,0,0)

rect_width = 20
rect_height = 20
rect_x = (WIDTH / 2) - rect_width
rect_y = 20
vel_y = 20
vel_x = 20

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

    x_axis = rect_x + rect_width
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

    blocks = all_rotations_blocks
    borders = all_rotations_borders

    return blocks, borders


def box_shape():
    blocks = []
    all_rotations_blocks = []
    borders = []
    all_rotations_borders = []
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

    all_rotations_blocks.append(blocks)
    all_rotations_borders.append(borders)

    blocks = all_rotations_blocks
    borders = all_rotations_borders

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

    for i, (rect, vx, vy) in enumerate(shape[1]):
        pygame.draw.rect(screen, border_color, rect, border_width)

    for i, (rect, vx, vy) in enumerate(shape[0]):
        pygame.draw.rect(screen, block_color, rect)

    for i, (rect, vx, vy) in enumerate(bottom_bricks_border):
        pygame.draw.rect(screen, border_color, rect, border_width)

    for i, (rect, vx, vy) in enumerate(bottom_bricks):
        pygame.draw.rect(screen, block_color, rect)

    pygame.display.update()


def main():
    clock = pygame.time.Clock()

    elapsed_time = 0
    next_block = time.time()
    next_spawn = True

    shape_count = 0
    shapes = None
    shape_names = ["bar", "box", "t", "s_l", "s_r", "l_l", "l_r"]
    retain_state = True
    rotation = 0
    all_rotations = 0

    bottom_bricks = []
    bottom_bricks_border = []

    down_pressed = False  # variable to keep track of the space key state
    prev_down_state = False

    check_line_filled = []
    for i in range(int(WIDTH/rect_width)):
        check_line_filled.append(i * rect_width)

    running = True
    while running:
        elapsed_time += 1 / 15
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        bar = bar_shape()
        box = box_shape()
        t = t_shape()
        s_l = s_l_shape()
        s_r = s_r_shape()
        l_l = l_l_shape()
        l_r = l_r_shape()


        if next_spawn:
            shape_count += 1
            all_shapes = [bar, box, t, s_l, s_r, l_l, l_r]
            shapes = random.choice(all_shapes)
            # shapes = box
            all_rotations = len(shapes[0])
            shape_name = shape_names[all_shapes.index(shapes)]
            next_block = time.time() + 0.5
            next_spawn = False

            if not shapes == box:
                if shapes == bar or shapes == s_r or shapes == s_l:
                    rotation = random.randint(0,1)
                else:
                    rotation = random.randint(0, 3)
            else:
                rotation = 0

        # current_shape_all_rotations = tuple(shapes)
        blocks = shapes[0]
        borders = shapes[1]

        shape = blocks[rotation], borders[rotation]
        # shape = current_shape_all_rotations[0][rotation], current_shape_all_rotations[1][rotation]

        for i, (rect, vx, vy) in enumerate(shape[1]):
            if not next_spawn:
                if time.time() >= next_block:
                    if rect.y + rect_height >= HEIGHT:
                        for j, (all_rect, all_vx, all_vy) in enumerate(shape[1]):
                            if (all_rect, all_vx, all_vy) not in bottom_bricks_border:
                                bottom_bricks_border.append((all_rect, all_vx, all_vy))
                        for j, (all_rect, all_vx, all_vy) in enumerate(shape[0]):
                            if (all_rect, all_vx, all_vy) not in bottom_bricks:
                                bottom_bricks.append((all_rect, all_vx, all_vy))
                        next_spawn = True
                        break

        if not next_spawn:
            if time.time() >= next_block:
                for i, (rect, vx, vy) in enumerate(shape[1]):
                    for j, (rect_border, vx_border, vy_border) in enumerate(bottom_bricks_border):
                        if rect_border.top == rect.bottom and rect.x == rect_border.x:
                            retain_state = False
                            break
                    else:
                        continue
                    break
                if retain_state:
                    for j in range(all_rotations):
                        if j == rotation:
                            for i, ((rect1, vx1, vy1), (rect2, vx2, vy2)) in enumerate(zip(shape[0], shape[1])):
                                rect1.y += vel_y
                                rect2.y += vel_y
                        else:
                            for i, ((rect1, vx1, vy1), (rect2, vx2, vy2)) in enumerate(zip(shapes[0][j], shapes[1][j])):
                                rect1.y += vel_y
                                rect2.y += vel_y
                    next_block = time.time() + 0.5
                else:
                    for i, ((rect1, vx1, vy1), (rect2, vx2, vy2)) in enumerate(zip(shape[0], shape[1])):
                        if (rect1, vx1, vy1) not in bottom_bricks:
                            bottom_bricks.append((rect1, vx1, vy1))
                        if (rect2, vx2, vy2) not in bottom_bricks_border:
                            bottom_bricks_border.append((rect2, vx2, vy2))
                        retain_state = True
                    next_spawn = True

        get_all_y_axis = []
        bricks_to_remove = []
        no_of_rows_to_remove = []
        for j, (rect_border, vx_border, vy_border) in enumerate(bottom_bricks_border):
            if rect_border.y not in get_all_y_axis:
                get_all_y_axis.append(rect_border.y)

        for i in get_all_y_axis:
            get_all_x_axis = []
            for j, (rect_border, vx_border, vy_border) in enumerate(bottom_bricks_border):
                if i == rect_border.y:
                    get_all_x_axis.append(rect_border.x)
                if sorted(get_all_x_axis) == check_line_filled:
                    for k, (rect_border, vx_border, vy_border) in enumerate(bottom_bricks_border):
                        if rect_border.y == i:
                            if i not in no_of_rows_to_remove:
                                no_of_rows_to_remove.append(i)
                            bricks_to_remove.append(k)

        result = [item for index, item in enumerate(bottom_bricks_border) if index not in bricks_to_remove]
        bottom_bricks_border = result.copy()
        result = [item for index, item in enumerate(bottom_bricks) if index not in bricks_to_remove]
        bottom_bricks = result.copy()

        try:
            for i in no_of_rows_to_remove:
                for j, ((rect1, vx1, vy1), (rect2, vx2, vy2)) in enumerate(zip(bottom_bricks, bottom_bricks_border)):
                    if rect2.y < i:
                        rect1.y += vel_y
                        rect2.y += vel_y
        except TypeError:
            pass

        keys = pygame.key.get_pressed()

        prev_down_state = down_pressed
        down_pressed = keys[pygame.K_UP]

        rotations = [rotation]
        if down_pressed and not prev_down_state:
            check_valid_rotations = True
            if shape_name == "s_l" or shape_name == "s_r" or shape_name == "bar":
                if rotations[0] < 1:
                    rotations[0] += 1
                else:
                    rotations[0] = 0
                for i, (all_rect, vx_border, vy_border) in enumerate(shapes[1][rotations[0]]):
                    if all_rect.x + WIDTH or all_rect.x < 0 or all_rect.y + rect_height > HEIGHT:
                        if all_rect.x + rect_width > WIDTH:
                            check_valid_rotations = False
                            break
                        if all_rect.x < 0:
                            check_valid_rotations = False
                            break
                        if all_rect.y + rect_height >= HEIGHT:
                            check_valid_rotations = False
                            break

                if check_valid_rotations:
                    rotation = rotations[0]

            elif shape_name == "t" or shape_name == "l_l" or shape_name == "l_r":
                if rotations[0] < 3:
                    rotations[0] += 1
                else:
                    rotations[0] = 0
                for i, (all_rect, vx_border, vy_border) in enumerate(shapes[1][rotations[0]]):
                    if all_rect.x + WIDTH > WIDTH or all_rect.x < 0 or all_rect.y + rect_height >= HEIGHT:
                        if all_rect.x + rect_width > WIDTH:
                            check_valid_rotations = False
                            break
                        if all_rect.x < 0:
                            check_valid_rotations = False
                            break
                        if all_rect.y + rect_height >= HEIGHT:
                            check_valid_rotations = False
                            break
                        for j, (rect_border, vx_border, vy_border) in enumerate(bottom_bricks_border):
                            if rect_border.x == all_rect.x and rect_border.y == all_rect.y:
                                check_valid_rotations = False
                                break

                if check_valid_rotations:
                    rotation = rotations[0]
            elif box:
                pass

        if keys[pygame.K_LEFT]:
            state = True
            for i, (rect, vx, vy) in enumerate(shape[1]):
                if rect.x <= 0:
                    state = False
                else:
                    for j, (all_rect, vx_border, vy_border) in enumerate(bottom_bricks_border):
                        if all_rect.x + rect_width == rect.x and all_rect.y == rect.y:
                            state = False

            if state and not next_spawn:
                for j in range(all_rotations):
                    if j == rotation:
                        for i, ((rect1, vx1, vy1), (rect2, vx2, vy2)) in enumerate(zip(shape[0], shape[1])):
                            rect1.x -= vel_x
                            rect2.x -= vel_x
                    else:
                        for i, ((rect1, vx1, vy1), (rect2, vx2, vy2)) in enumerate(zip(shapes[0][j], shapes[1][j])):
                            rect1.x -= vel_x
                            rect2.x -= vel_x

        if keys[pygame.K_RIGHT]:
            state = True
            for i, (rect, vx, vy) in enumerate(shape[1]):
                if rect.right >= WIDTH:
                    state = False
                else:
                    for j, (all_rect, vx_border, vy_border) in enumerate(bottom_bricks_border):
                        if rect.x + rect_width == all_rect.x and all_rect.y == rect.y:
                            state = False

            if state and not next_spawn:
                for j in range(all_rotations):
                    if j == rotation:
                        for i, ((rect1, vx1, vy1), (rect2, vx2, vy2)) in enumerate(zip(shape[0], shape[1])):
                            rect1.x += vel_x
                            rect2.x += vel_x
                    else:
                        for i, ((rect1, vx1, vy1), (rect2, vx2, vy2)) in enumerate(zip(shapes[0][j], shapes[1][j])):
                            rect1.x += vel_x
                            rect2.x += vel_x

        if keys[pygame.K_DOWN]:
            state = True
            for i, (rect, vx, vy) in enumerate(shape[1]):
                if rect.bottom >= HEIGHT:
                    next_block = time.time()
                    state = False
                else:
                    for j, (all_rect, vx_border, vy_border) in enumerate(bottom_bricks_border):
                        if rect.y + rect_height == all_rect.y and all_rect.x == rect.x:
                            state = False

            if state:
                for j in range(all_rotations):
                    if j == rotation:
                        for i, ((rect1, vx1, vy1), (rect2, vx2, vy2)) in enumerate(zip(shape[0], shape[1])):
                            rect1.y += vel_y
                            rect2.y += vel_y
                    else:
                        for i, ((rect1, vx1, vy1), (rect2, vx2, vy2)) in enumerate(zip(shapes[0][j], shapes[1][j])):
                            rect1.y += vel_y
                            rect2.y += vel_y

        clock.tick(15)
        draw(shape, bottom_bricks, bottom_bricks_border)


if __name__ == "__main__":
    main()