import pygame
import pygame.mixer
import random
import time
from PIL import Image

pygame.font.init()
pygame.mixer.init()

pygame.display.set_caption("Save Me")

# Define constants


WIDTH, HEIGHT = 800, 600
BG_COLOR = (255, 255, 255)
BACKGROUND_IMG = "assets/background/bg2.gif"

POWER_RADIUS = 11
POWER_SIZE = POWER_RADIUS
RESPAWN_POWER = 14
POWER_DURATION = 7

CIRCLE_RADIUS = 50
CIRCLE_VELOCITY = 5
RESPAWN_CIRCLE = 5

PLAYER_WIDTH = 25
PLAYER_HEIGHT = 25
PLAYER_VEL = 5

TOP_SCORE = 0

try:
    with open("settings.ini") as file:
        data = file.readlines()
        for line in data:
            if line.startswith("#") or line.startswith("\n"):
                pass
            else:
                values = str(line.strip())
                if line.startswith("WIDTH"):
                    WIDTH = int(values.split(" = ")[1])
                if line.startswith("HEIGHT"):
                    HEIGHT = int(values.split(" = ")[1])
                if line.startswith("POWER_RADIUS"):
                    POWER_RADIUS = int(values.split(" = ")[1])
                if line.startswith("RESPAWN_POWER"):
                    RESPAWN_POWER = int(values.split(" = ")[1])
                if line.startswith("POWER_DURATION"):
                    POWER_DURATION = int(values.split(" = ")[1])
                if line.startswith("CIRCLE_RADIUS"):
                    CIRCLE_RADIUS = int(values.split(" = ")[1])
                if line.startswith("CIRCLE_VELOCITY"):
                    CIRCLE_VELOCITY = int(values.split(" = ")[1])
                if line.startswith("RESPAWN_CIRCLE"):
                    RESPAWN_CIRCLE = int(values.split(" = ")[1])
                if line.startswith("PLAYER_WIDTH"):
                    PLAYER_WIDTH = int(values.split(" = ")[1])
                if line.startswith("PLAYER_HEIGHT"):
                    PLAYER_HEIGHT = int(values.split(" = ")[1])
                if line.startswith("PLAYER_VEL"):
                    PLAYER_VEL = int(values.split(" = ")[1])
                if line.startswith("TOP_SCORE"):
                    TOP_SCORE = int(values.split(" = ")[1])
except FileNotFoundError:
    pass

PLAYER_IMAGE = pygame.image.load("assets/spawns/player.jpg")
PLAYER_IMAGE = pygame.transform.scale(PLAYER_IMAGE, (35, 35))
PLAYER_FIRE_IMG = "assets/spawns/player_fire.gif"

DONT_TOUCH_POWER_IMG = "assets/spawns/fire_circle.gif"
DESTROY_ALL_RUNE_IMG = "assets/spawns/destroy_all_rune.gif"
SHIELD_RUNE_IMG = "assets/spawns/shield_rune.gif"

ENEMIES_DEAD_IMG = "assets/spawns/enemies_dead.gif"
ENEMY_DEAD_IMG = "assets/spawns/enemy_dead.gif"
SHIELD_IMG = pygame.image.load("assets/spawns/shield.png")
SHIELD_IMG = pygame.transform.scale(SHIELD_IMG, (PLAYER_WIDTH + 50, PLAYER_HEIGHT + 50))

ENEMY_IMG = "assets/spawns/enemy8.gif"



PLAYER_SOUND = pygame.mixer.Sound("assets\sounds\Player.wav")
DESTROY_ALL_SOUND = pygame.mixer.Sound("assets\sounds\Destroy_All.wav")
SINGLE_ENEMY_KILL = pygame.mixer.Sound("assets\sounds\Ring_Destroyed.wav")
FIRE_RUNE_PICKUP_SOUND = pygame.mixer.Sound("assets\sounds\Fire_Rune_Collected.wav")
ENEMY_COLLIDE_SOUND = pygame.mixer.Sound("assets\sounds\Ring_Collide.wav")
SHIELD_SOUND = pygame.mixer.Sound("assets\sounds\Shield.wav")
WALL_HIT_SOUND = pygame.mixer.Sound("assets\sounds\Wall_Hit.wav")
RUNE_SPAWNED_SOUND = pygame.mixer.Sound("assets\sounds\Spawn.wav")
LOST_SOUND = pygame.mixer.Sound("assets\sounds\Lost.wav")

screen = pygame.display.set_mode((WIDTH, HEIGHT))
FONT = pygame.font.SysFont("comicsans", 30)


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

def create_power_up():
    x = random.randint(CIRCLE_RADIUS, WIDTH - CIRCLE_RADIUS)
    y = random.randint(CIRCLE_RADIUS, HEIGHT - CIRCLE_RADIUS)
    circle = pygame.Rect(x - CIRCLE_RADIUS, y - CIRCLE_RADIUS, CIRCLE_RADIUS, CIRCLE_RADIUS)
    return circle


def create_circle():
    x = random.randint(CIRCLE_RADIUS, WIDTH - CIRCLE_RADIUS)
    y = CIRCLE_RADIUS
    vx = random.choice([-CIRCLE_VELOCITY, CIRCLE_VELOCITY])
    vy = random.choice([-CIRCLE_VELOCITY, CIRCLE_VELOCITY])
    circle = pygame.Rect(x - CIRCLE_RADIUS, y - CIRCLE_RADIUS, CIRCLE_RADIUS, CIRCLE_RADIUS), vx, vy
    return circle


def create_player():
    player = pygame.Rect((WIDTH / 2) - PLAYER_WIDTH, (HEIGHT / 2) - PLAYER_HEIGHT,
                         PLAYER_WIDTH, PLAYER_HEIGHT)
    return player


def draw(background, player, circles, powers, fire_ring, fire_rune, shield_rune, destroy_all_rune, elapsed_time, RUNE_SPAWNED, rune_collected, enemy, explosion_effect_container, single_enemy_explosion_effect, single_enemy_dead):

    screen.blit(background, (0,0))


    for power in powers:
        # screen.blit(fire_rune, (power.x, power.y))
        # pygame.draw.circle(screen, POWER_COLOR, power.center, POWER_RADIUS)
        if RUNE_SPAWNED == "DONT_TOUCH":
            screen.blit(fire_rune, (power.x, power.y))
        if RUNE_SPAWNED == "INVULNERABLE":
            screen.blit(shield_rune, (power.x, power.y))
        if RUNE_SPAWNED == "DESTROY_ALL":
            screen.blit(destroy_all_rune, (power.x, power.y))


    current_time = pygame.time.get_ticks()

    angle = -current_time / 2 % 360
    rotated_image = pygame.transform.rotate(PLAYER_IMAGE, angle)

    new_rect = rotated_image.get_rect(center=player.center)

    # surface = pygame.Surface(rotated_image.get_size(), pygame.SRCALPHA)
    # Draw the rotated image onto the surface
    offset = (new_rect.centerx - player.centerx, new_rect.centery - player.centery)

    # Add the offset to the position of the new rectangle
    new_rect.x += offset[0]
    new_rect.y += offset[1]

        # Draw the rotated image (Player) onto the screen at the position of the new rectangle
    if len(rune_collected) < 1:
        screen.blit(rotated_image, (new_rect.x, new_rect.y))

    # Draw the surface onto the screen at the position of the rectangle
    # screen.blit(surface, (player.x, player.y))
    for i, (circle, vx, vy) in enumerate(circles):
        circle.move_ip(vx, vy)

        if circle.left < 0 or circle.right > WIDTH:
            WALL_HIT_SOUND.play()
            vx = -vx
        if circle.top < 0 or circle.bottom > HEIGHT:
            if circle.bottom > HEIGHT:
                WALL_HIT_SOUND.play()
            vy = -vy

        for j, (other_circle, other_vx, other_vy) in enumerate(circles):
            if i != j:
                if circle.colliderect(other_circle):
                    ENEMY_COLLIDE_SOUND.play()
                    vx = -vx
                    vy = -vy
                    circles[i] = (circle, vx, vy)

        circles[i] = (circle, vx, vy)

    for circle, _, _ in circles:
        screen.blit(enemy, (circle.x, circle.y))
        # pygame.draw.circle(screen, CIRCLE_COLOR, circle.center, CIRCLE_RADIUS)

    for circle, _, _ in single_enemy_explosion_effect:
        SINGLE_ENEMY_KILL.play()
        screen.blit(single_enemy_dead, (circle.x, circle.y))

    if len(rune_collected) > 0:
        if rune_collected[0] == "DONT_TOUCH":
            screen.blit(fire_ring, (player.x - 17, player.y - 17))
        if rune_collected[0] == "INVULNERABLE":
            screen.blit(rotated_image, (new_rect.x, new_rect.y))
            screen.blit(SHIELD_IMG, (player.x - 25, player.y - 25))
        if rune_collected[0] == "DESTROY_ALL":
            if len(explosion_effect_container) > 0:
                for circle, _, _ in explosion_effect_container:
                    screen.blit(enemy, (circle.x, circle.y))
            screen.blit(rotated_image, (new_rect.x, new_rect.y))

    time_text = FONT.render(f"Time: {round(elapsed_time)}s", 1, "white")
    screen.blit(time_text, (10, 10))


    # for i in rune_collected:
    #     power_text = FONT.render(i, 1, "green")
    #     screen.blit(power_text, ((WIDTH - power_text.get_width()) - 15, power_text.get_height() - 25))

    if round(elapsed_time) > TOP_SCORE:
        top_score = FONT.render(f'TOP SCORE: {round(elapsed_time):3}', 1, "green")
        screen.blit(top_score, ((WIDTH - top_score.get_width()) - 15, top_score.get_height() - 25))
    else:
        top_score = FONT.render(f'TOP SCORE: {TOP_SCORE:2}', 1, "green")
        screen.blit(top_score, ((WIDTH - top_score.get_width()) - 15, top_score.get_height() - 25))


    pygame.display.update()


def main():
    # Loading Images
    background_images = get_gif_frames(BACKGROUND_IMG, WIDTH, HEIGHT)
    destroy_all_rune_images = get_gif_frames(DESTROY_ALL_RUNE_IMG, POWER_SIZE + 40, POWER_SIZE + 40)
    fire_ring_images = get_gif_frames(PLAYER_FIRE_IMG, PLAYER_WIDTH + 55, PLAYER_HEIGHT + 30)
    fire_rune_images = get_gif_frames(DONT_TOUCH_POWER_IMG, POWER_SIZE + 40, POWER_SIZE + 40)
    shield_rune_images = get_gif_frames(SHIELD_RUNE_IMG, POWER_SIZE + 40, POWER_SIZE + 40)
    enemy_images = get_gif_frames(ENEMY_IMG, CIRCLE_RADIUS, CIRCLE_RADIUS)
    enemy_dead_images = get_gif_frames(ENEMIES_DEAD_IMG, CIRCLE_RADIUS + 70, CIRCLE_RADIUS + 70)
    single_enemy_dead_images = get_gif_frames(ENEMY_DEAD_IMG, CIRCLE_RADIUS + 35, CIRCLE_RADIUS + 35)

    # Loading Sounds



    bg_img_index = 0

    fire_ring_index = 0

    enemy_index = 0
    enemy_dead_index = 0
    single_enemy_dead_index = 0

    fire_rune_index = 0
    shield_rune_index = 0
    destroy_all_rune_index = 0

    timer_interval = 100  # milliseconds
    last_timer_event = pygame.time.get_ticks()


    player = create_player()

    clock = pygame.time.Clock()

    # Keep track of the circles
    circles = []
    next_circle_time = time.time() + 2

    explosion_effect_container = []
    single_enemy_explosion_effect = []

    powers = []
    next_power_time = time.time() + 7

    RUNE_SPAWNED = ""
    rune_collected = []

    start_time = time.time()

    running = True
    hit = False
    power_collected = True
    invulnerable = False
    dont_touch_me = False

    power_duration = time.time() + 5.0
    explosion_effect = time.time()
    single_explosion_effect = time.time()

    while running:
        elapsed_time = time.time() - start_time
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        current_time = pygame.time.get_ticks()

        if current_time - last_timer_event >= timer_interval:
            bg_img_index = (bg_img_index + 1) % len(background_images)
            fire_ring_index = (fire_ring_index + 1) % len(fire_ring_images)
            fire_rune_index = (fire_rune_index + 1) % len(fire_rune_images)
            shield_rune_index = (shield_rune_index + 1) % len(shield_rune_images)
            destroy_all_rune_index = (destroy_all_rune_index + 1) % len(destroy_all_rune_images)
            enemy_index = (enemy_index + 3) % len(enemy_images)
            single_enemy_dead_index = (single_enemy_dead_index + 1) % len(single_enemy_dead_images)
            last_timer_event = current_time

        backgound = background_images[bg_img_index]
        fire_ring = fire_ring_images[fire_ring_index]
        fire_rune = fire_rune_images[fire_rune_index]
        shield_rune = shield_rune_images[shield_rune_index]
        destroy_all_rune = destroy_all_rune_images[destroy_all_rune_index]
        enemy = enemy_images[enemy_index]
        single_enemy_dead = single_enemy_dead_images[single_enemy_dead_index]

        # Create a new circle if it's time
        if time.time() >= next_circle_time:
            circle, vx, vy = create_circle()
            circles.append((circle, vx, vy))
            next_circle_time = time.time() + RESPAWN_CIRCLE

        if time.time() >= next_power_time:
            RUNE_SPAWNED_SOUND.play()
            random_number = random.randint(1, 100) > 70
            if random_number:
                RUNE_SPAWNED = "DESTROY_ALL"
            else:
                RUNE_SPAWNED = random.choice(["INVULNERABLE", "DONT_TOUCH"])

            powers.append(create_power_up())
            next_power_time = time.time() + RESPAWN_POWER
            power_duration = time.time() + POWER_DURATION

        drones = circles.copy()
        for i, (circle, vx, vy) in enumerate(drones):
            if circle.colliderect(player):
                if dont_touch_me:
                    single_enemy_explosion_effect.append((circle, vx, vy))
                    circles.remove((circle, vx, vy))
                else:
                    hit = True

        if explosion_effect > time.time():
            enemy = enemy_dead
        else:
            explosion_effect_container.clear()

        if single_explosion_effect > time.time():
            pass
        else:
            SINGLE_ENEMY_KILL.stop()
            single_enemy_explosion_effect.clear()

        for power in powers:
            if power.colliderect(player):
                if RUNE_SPAWNED == "DONT_TOUCH":
                    FIRE_RUNE_PICKUP_SOUND.play()
                powers.pop()
                power_collected = True
                next_power_time = time.time() + RESPAWN_POWER
                power_duration = time.time() + 5.0
            elif time.time() >= power_duration:
                powers.pop()

        if time.time() <= power_duration and power_collected and time.time() > start_time + 7:
            rune_collected.append(RUNE_SPAWNED)

            if RUNE_SPAWNED == "INVULNERABLE":
                SHIELD_SOUND.play()
                invulnerable = True
                hit = False

            if RUNE_SPAWNED == "DONT_TOUCH":
                dont_touch_me = True
                hit = False
                single_explosion_effect = time.time() + 0.2

            if RUNE_SPAWNED == "DESTROY_ALL":
                next_circle_time = time.time()
                enemy_dead_index = (enemy_dead_index + 1) % len(enemy_dead_images)
                enemy_dead = enemy_dead_images[enemy_dead_index]
                if len(circles) > 1:
                    explosion_effect = time.time() + 0.2
                    DESTROY_ALL_SOUND.play()
                    explosion_effect_container = circles.copy()
                circles.clear()
        else:
            invulnerable = False
            dont_touch_me = False
            power_collected = False
            rune_collected.clear()

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
            LOST_SOUND.play()
            if elapsed_time > TOP_SCORE:
                with open("settings.ini", 'r') as file:
                    filedata = file.read()
                filedata = filedata.replace(f'TOP_SCORE = {TOP_SCORE}', f'TOP_SCORE = {round(elapsed_time)}')

                with open("settings.ini", 'w') as file:
                    file.write(filedata)
            pygame.time.delay(5000)
            break

        draw(backgound, player, circles, powers, fire_ring, fire_rune, shield_rune, destroy_all_rune, elapsed_time, RUNE_SPAWNED, rune_collected, enemy, explosion_effect_container, single_enemy_explosion_effect, single_enemy_dead)
        clock.tick(60)

    pygame.quit()


if __name__ == "__main__":
    main()