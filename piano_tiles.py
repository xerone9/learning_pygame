import pygame
import pygame.mixer
import random
from PIL import Image
import time


pygame.font.init()
FONT = pygame.font.SysFont("comicsans", 30)
pygame.mixer.init()

pygame.display.set_caption("Piano Tiles - Clone")
BACKGROUND_IMG = "piano_tiles_bg.gif"

# Define constants
WIDTH = 401
HEIGHT = 800
BG_COLOR = (173, 216, 230)
separate_tile_border = (255, 255, 255)

PLAYER_WIDTH = 98
PLAYER_HEIGHT = 120

screen = pygame.display.set_mode((WIDTH, HEIGHT))


def get_gif_frames(filename, width, height):
    frames = []
    resized_py_game_image_object = []
    with Image.open(filename) as im:
        for i in range(im.n_frames):
            im.seek(i)
            frame = im.copy()
            frames.append(frame)
    for frame in frames:
        mode = frame.mode
        size = frame.size
        data = frame.tobytes()
        py_image = pygame.image.fromstring(data, size, mode)
        py_image.set_colorkey((255, 255, 255))
        py_image.set_alpha(255)  # set the alpha channel to fully opaque
        scaled_image = pygame.transform.scale(py_image, (width, height))
        resized_py_game_image_object.append(scaled_image)
    resized_py_game_image_object.pop(0)
    return resized_py_game_image_object


def create_tile(x):
    vx = 0
    vy = 2
    tile = pygame.Rect(x, -120, PLAYER_WIDTH, PLAYER_HEIGHT), vx, vy
    return tile


def draw(background, tiles, score, font_size):
    # screen.fill(BG_COLOR)
    screen.blit(background, (0, 0))
    pygame.draw.rect(screen, separate_tile_border, pygame.Rect(0, 0, 1, HEIGHT))
    pygame.draw.rect(screen, separate_tile_border, pygame.Rect(100, 0, 1, HEIGHT))
    pygame.draw.rect(screen, separate_tile_border, pygame.Rect(200, 0, 1, HEIGHT))
    pygame.draw.rect(screen, separate_tile_border, pygame.Rect(300, 0, 1, HEIGHT))
    pygame.draw.rect(screen, separate_tile_border, pygame.Rect(400, 0, 1, HEIGHT))

    for i, (tile, vx, vy) in enumerate(tiles):
        tile.move_ip(vx, vy)

    for tile, _, _ in tiles:
        pygame.draw.rect(screen, "black", tile)

    font = pygame.font.Font(None, font_size)
    score_text = font.render(str(score), 1, "red")
    screen.blit(score_text, (WIDTH/2 - score_text.get_width()/2, 30))

    pygame.display.update()


def main():
    clock = pygame.time.Clock()
    engine = True
    running = True
    key_pressed = True

    font_size_duration = time.time()

    music_duration = time.time()
    music_play_time = 0.4

    timer_interval = 100
    last_timer_event = pygame.time.get_ticks()
    background_images = get_gif_frames(BACKGROUND_IMG, WIDTH, HEIGHT)
    bg_img_index = 0

    tiles = []
    score = 0
    x = random.choice([1, 101, 201, 301])
    tile, vx, vy = create_tile(x)
    tiles.append((tile, vx, vy))
    standard_speed = 150
    score_speed_thershold = 50
    # start_time = time.time()
    sound_file = "Piano Tiles - Congfei Wei Piano Tiles 2.wav"  # Replace with your sound file path
    pygame.mixer.music.load(sound_file)
    pygame.mixer.music.play()
    pygame.mixer.music.pause()

    while engine:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                engine = False



        current_time = pygame.time.get_ticks()
        if current_time - last_timer_event >= timer_interval:
            bg_img_index = (bg_img_index + 1) % len(background_images)
        background = background_images[bg_img_index]

        if font_size_duration > time.time():
            font_size = 100
        else:
            font_size = 80

        if music_duration > time.time():
            pygame.mixer.music.unpause()
        else:
            pygame.mixer.music.pause()

        try:
            last_tile = tiles[-1]
            last_rect, _, _ = last_tile
            y_value = last_rect.y
            x_value = last_rect.x
            x_choices = [1, 101, 201, 301]
            x_choices.remove(x_value)
            if y_value > -1:
                x = random.choice(x_choices)
                tile, vx, vy = create_tile(x)
                tiles.append((tile, vx, vy))
        except IndexError:
            x_choices = [1, 101, 201, 301]
            x = random.choice(x_choices)
            tile, vx, vy = create_tile(x)
            tiles.append((tile, vx, vy))

        # if time.time() - start_time >= 5:
        #     start_time = time.time()
        #     standard_speed += 1

        if score >= score_speed_thershold:
            score_speed_thershold += 50
            standard_speed += 50

        if event.type == pygame.KEYUP:
            key_pressed = True

        first_tile = tiles[0]
        first_rect, _, _ = first_tile
        x_value = first_rect.x
        y_value = first_rect.y
        if y_value > HEIGHT + 10:
            running = False

        try:
            keys = pygame.key.get_pressed()
            if key_pressed:
                if keys[pygame.K_q]:
                    first_tile = 1
                    if x_value == first_tile:
                        tiles.pop(0)
                        score += 1
                        font_size_duration = time.time() + 0.05
                        music_duration = time.time() + music_play_time
                        key_pressed = False
                    else:
                        wrong_tile = pygame.Rect(first_tile, y_value, PLAYER_WIDTH, PLAYER_HEIGHT)
                        pygame.draw.rect(screen, "red", wrong_tile)
                        pygame.display.flip()
                        running = False

            if key_pressed:
                if keys[pygame.K_w]:
                    second_tile = 101
                    if x_value == second_tile:
                        tiles.pop(0)
                        score += 1
                        font_size_duration = time.time() + 0.05
                        music_duration = time.time() + music_play_time
                        key_pressed = False
                    else:
                        wrong_tile = pygame.Rect(second_tile, y_value, PLAYER_WIDTH, PLAYER_HEIGHT)
                        pygame.draw.rect(screen, "red", wrong_tile)
                        pygame.display.flip()
                        running = False

            if key_pressed:
                if keys[pygame.K_e]:
                    third_tile = 201
                    if x_value == third_tile:
                        tiles.pop(0)
                        score += 1
                        font_size_duration = time.time() + 0.05
                        music_duration = time.time() + music_play_time
                        key_pressed = False
                    else:
                        wrong_tile = pygame.Rect(third_tile, y_value, PLAYER_WIDTH, PLAYER_HEIGHT)
                        pygame.draw.rect(screen, "red", wrong_tile)
                        pygame.display.flip()
                        running = False

            if key_pressed:
                if keys[pygame.K_r]:
                    forth_tile = 301
                    if x_value == forth_tile:
                        tiles.pop(0)
                        score += 1
                        font_size_duration = time.time() + 0.05
                        music_duration = time.time() + music_play_time
                        key_pressed = False
                    else:
                        wrong_tile = pygame.Rect(forth_tile, y_value, PLAYER_WIDTH, PLAYER_HEIGHT)
                        pygame.draw.rect(screen, "red", wrong_tile)
                        pygame.display.flip()
                        running = False
        except IndexError:
            pass

        clock.tick(standard_speed)

        if not running:
            font_size = 80
            font = pygame.font.Font(None, font_size)
            lost_text = font.render("You Lost", 1, "purple")
            screen.blit(lost_text, (WIDTH / 2 - lost_text.get_width() / 2, HEIGHT / 2 - lost_text.get_height() / 2))
            pygame.mixer.music.stop()
            pygame.mixer.music.unload()
            pygame.display.flip()
            pygame.time.delay(3000)  # 5000 milliseconds (5 seconds)
            engine = False

        draw(background, tiles, score, font_size)


if __name__ == "__main__":
    main()