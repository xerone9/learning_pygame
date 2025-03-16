import pygame
import pygame.mixer
import math
from PIL import Image
import random
import time


pygame.font.init()
pygame.mixer.init()

pygame.display.set_caption("Space Shooter")

BACKGROUND_IMG = "space_shooter_assets/bg3.gif"
ENERGY_IMG = "space_shooter_assets/atom.gif"
PLAYER_IMG = pygame.image.load('space_shooter_assets/jet1.png')
SHIELD_IMG = pygame.image.load('space_shooter_assets/mega_flare.png')
ENEMY_IMG = pygame.image.load('space_shooter_assets/enemy.png')
ENEMY_MISSILE = pygame.image.load('space_shooter_assets/enemy_missile.png')
SMALL_MISSILE_IMG = pygame.image.load('space_shooter_assets/small_missle.png')
LARGE_MISSILE_IMG = pygame.image.load('space_shooter_assets/large_missile.png')
SEPARATE_CANNON = pygame.image.load('space_shooter_assets/separate_cannon.png')


# Define constants
WIDTH = 800
HEIGHT = 880
BG_COLOR = (102, 204, 255)

PLAYER_WIDTH = 100
PLAYER_HEIGHT = 100
PLAYER_COLOR = (0, 255, 0)

SHIELD_WIDTH = PLAYER_WIDTH + 60
SHIELD_HEIGHT = PLAYER_HEIGHT + 60

NEXT_FIRE_DELAY = 1000
ENEMY_NEXT_FIRE_DELAY = 0

PLAYER_BULLET_WIDTH = 4
PLAYER_BULLET_HEIGHT = 20
PLAYER_BULLET_COLOR = (255, 0, 0)
PLAYER_MISSILE_WIDTH = 100
PLAYER_MISSILE_HEIGHT = 400

ENEMY_WIDTH = 400
ENEMY_HEIGHT = 350
ENEMY_SPEED = 1
ENEMY_HEALTH_COLOR = (254, 100, 100)
ENEMY_BULLET_COLOR = (64, 93, 137)

ENEMY_BULLET_WIDTH = 12
ENEMY_BULLET_HEIGHT = 20
ENEMY_MISSILE_WIDTH = 50
ENEMY_MISSILE_HEIGHT = 200

SCREEN_HEIGHT = 950

ASSESSMENT_SCORE_COLORS = {
    "Attendance": 'red',
    "Quiz": 'green',
    "Assignments": 'blue',
    "Midterm": 'yellow',
    "Activities": 'orange'
}

screen = pygame.display.set_mode((WIDTH, SCREEN_HEIGHT))


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


def draw(background, player, player_bullets, energies, student_assessment_scores, collectables, enemy_bullets, enemy, ENEMY_HEALTH, main_enemy_bullets, player_missile, enemy_missiles, show_shield):
    # screen.blit(background, (0, 0))
    screen.fill(BG_COLOR)

    # resized_image = pygame.transform.scale(ENEMY_IMG, (
    # int(ENEMY_IMG.get_width() * 1.5), int(ENEMY_IMG.get_height() * 1.5)))
    # resized_image_rect = resized_image.get_rect()
    # resized_image_rect.topleft = (200, 10)
    # screen.blit(resized_image, resized_image_rect.topleft)

    y_axis = HEIGHT / 2 - 100
    for key, value in collectables.items():
        FONT = pygame.font.SysFont("comicsans", 30)
        score_text = FONT.render(key, 1, "White")
        screen.blit(score_text, (WIDTH / 2 - 150, y_axis))
        y_axis += 40

    for key, value in energies.items():
        screen.blit(value[0], value[1].topleft)

    if len(collectables) <= 0:
        screen.blit(player_missile[0], player_missile[1].topleft)

    if len(show_shield) > 0:
        for i in show_shield:
            screen.blit(i[0], i[1].topleft)
    screen.blit(player[0], player[1].topleft)

    for i in enemy_missiles[1]:
        screen.blit(enemy_missiles[0], i.topleft)

    for bullet in player_bullets:
        pygame.draw.rect(screen, PLAYER_BULLET_COLOR, bullet)

    for bullet in enemy_bullets:
        pygame.draw.rect(screen, 'orange', bullet)

    for bullet in main_enemy_bullets:
        pygame.draw.rect(screen, ENEMY_BULLET_COLOR, bullet)

    if len(collectables) <= 0:
        x_axis = 10
        for i in range(4):
            resized_image = pygame.transform.scale(SEPARATE_CANNON, (int(SEPARATE_CANNON.get_width() * 0.5), int(SEPARATE_CANNON.get_height() * 0.5)))
            resized_image_rect = resized_image.get_rect()
            resized_image_rect.topleft = (x_axis, -12)
            screen.blit(resized_image, resized_image_rect.topleft)
            if i != 1:
                x_axis += 50
            else:
                x_axis += 640

    status_bar = pygame.Rect(WIDTH - ((WIDTH / 5) * 4), 910, 500, 30)
    pygame.draw.rect(screen, PLAYER_COLOR, status_bar, 1)
    attendance_score = student_assessment_scores["Attendance"] / 100 * 494
    status_bar_fill = pygame.Rect((WIDTH - ((WIDTH / 5) * 4) + 3), 913, attendance_score, 24)
    pygame.draw.rect(screen, PLAYER_COLOR, status_bar_fill)
    FONT = pygame.font.SysFont("comicsans", 30)
    score_text = FONT.render(str('Health'), 1, "black")
    screen.blit(score_text, (WIDTH / 2 - score_text.get_width() / 2, SCREEN_HEIGHT - 48))

    if len(collectables) <= 0:
        enemy_status_bar = pygame.Rect(WIDTH - ((WIDTH / 5) * 4), 20, 500, 30)
        pygame.draw.rect(screen, ENEMY_HEALTH_COLOR, enemy_status_bar, 1)
        enemy_status_bar_fill = pygame.Rect((WIDTH - ((WIDTH / 5) * 4) + 3), 23, ENEMY_HEALTH / 100 * 494, 24)
        pygame.draw.rect(screen, ENEMY_HEALTH_COLOR, enemy_status_bar_fill)
        FONT = pygame.font.SysFont("comicsans", 30)
        score_text = FONT.render(str(round(ENEMY_HEALTH, 2)), 1, "black")
        screen.blit(score_text, (WIDTH / 2 - score_text.get_width() / 2, 12))

    distance = 0
    for i in range(round(student_assessment_scores["Activities"] / 20)):
        fire_power = pygame.Rect((10 + distance), 915, 15, 20)
        pygame.draw.rect(screen, "blue", fire_power)
        distance += 22
    FONT = pygame.font.SysFont("comicsans", 20)
    score_text = FONT.render('Fire Rate', 1, "White")
    screen.blit(score_text, (50, SCREEN_HEIGHT - 70))

    if student_assessment_scores["Midterm"] > 0:
        resized_image = pygame.transform.scale(SMALL_MISSILE_IMG, (int(SMALL_MISSILE_IMG.get_width() * 0.1), int(SMALL_MISSILE_IMG.get_height() * 0.1)))
        resized_image_rect = resized_image.get_rect()
        resized_image_rect.topleft = (10, SCREEN_HEIGHT - 120)
        screen.blit(resized_image, resized_image_rect.topleft)

    distance = 0
    for i in range(round(student_assessment_scores["Quiz"] / 20)):
        no_of_cannon = pygame.Rect(((WIDTH - (WIDTH / 5) + 40) + distance), 915, 15, 20)
        pygame.draw.rect(screen, "blue", no_of_cannon)
        distance += 22
    FONT = pygame.font.SysFont("comicsans", 20)
    score_text = FONT.render('Cannons', 1, "White")
    screen.blit(score_text, ((WIDTH - (WIDTH / 5) + 40), SCREEN_HEIGHT - 70))

    distance = 0
    for i in range(math.floor(student_assessment_scores["Assignments"] / 33)):
        mega_blast_defend = pygame.Rect((WIDTH - (WIDTH / 5) + 140), (915 - distance) - 30, 15, 20)
        pygame.draw.rect(screen, "red", mega_blast_defend)
        distance += 30

    if len(collectables) <= 0:
        screen.blit(enemy[0], enemy[1].topleft)

    pygame.display.update()


def main():
    clock = pygame.time.Clock()
    key_repeat_timer = 0
    enemy_next_fire = 0
    main_enemy_next_fire = 0
    ENEMY_HEALTH = 100
    main_enemy_spawn_time = False
    shield_acitivated = False
    main_enemy_spawn = False
    limit_fire = time.time()
    missile_animation = False
    player_missile_start_speed = 1
    running = True
    player_x, player_y = WIDTH // 2 - PLAYER_WIDTH // 2, HEIGHT - PLAYER_HEIGHT * 2
    enemy_x, enemy_y = 200, -220
    player_missile_x, player_missile_y = WIDTH / 2 - (PLAYER_MISSILE_WIDTH / 2), SCREEN_HEIGHT - 20
    player_image = pygame.transform.scale(PLAYER_IMG, (PLAYER_WIDTH, PLAYER_HEIGHT))
    shield_image = pygame.transform.scale(SHIELD_IMG, (SHIELD_WIDTH, SHIELD_HEIGHT))
    missile_image = pygame.transform.scale(LARGE_MISSILE_IMG, (PLAYER_MISSILE_WIDTH, PLAYER_MISSILE_HEIGHT))
    enemy_missile_image = pygame.transform.scale(ENEMY_MISSILE, (ENEMY_MISSILE_WIDTH, ENEMY_MISSILE_HEIGHT))
    enemy_image = pygame.transform.scale(ENEMY_IMG, (ENEMY_WIDTH, ENEMY_HEIGHT))
    player_bullets = []
    enemy_bullets = []
    main_enemy_bullets = []
    enemy_missiles = []
    show_shield = []

    enemy_missile_x = 2
    for i in range(14):
        enemy_missile = pygame.Rect(enemy_missile_x, -ENEMY_MISSILE_HEIGHT, ENEMY_MISSILE_WIDTH, ENEMY_MISSILE_HEIGHT)
        enemy_missiles.append(enemy_missile)
        enemy_missile_x += 57
    enemy_missiles = [enemy_missile_image, enemy_missiles]


    timer_interval = 100
    last_timer_event = pygame.time.get_ticks()

    background_images = get_gif_frames(BACKGROUND_IMG, WIDTH, SCREEN_HEIGHT)
    energy_images = get_gif_frames(ENERGY_IMG, 50, 50)
    bg_img_index = 0
    energy_img_index = 0

    collectables = {
        "Attendance": 10,
        "Quiz": 100,
        "Assignments": 0,
        "Midterm": 100,
        "Activities": 100
    }

    student_assessment_scores = {
        "Attendance": 0,
        "Quiz": 0,
        "Assignments": 0,
        "Midterm": 0,
        "Activities": 0
    }
    enemy = pygame.Rect(enemy_x, enemy_y, ENEMY_WIDTH, ENEMY_HEIGHT)
    enemy = [enemy_image, enemy]


    enemy[1].topleft = (enemy_x, enemy_y)
    enemy_movement_direction = [1, 0]
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        current_time = pygame.time.get_ticks()

        if student_assessment_scores["Activities"] < 5:
            NEXT_FIRE_DELAY = 1000 / (5 / 10)
        else:
            NEXT_FIRE_DELAY = 1000 / (student_assessment_scores["Activities"] / 10)
        fire_cannons = round(student_assessment_scores["Quiz"] / 20)

        if current_time - last_timer_event >= timer_interval:
            bg_img_index = (bg_img_index + 1) % len(background_images)
            energy_img_index = (energy_img_index + 1) % len(energy_images)

        background = background_images[bg_img_index]
        energy_image = energy_images[energy_img_index]

        keys = pygame.key.get_pressed()

        # Update player position based on arrow keys
        if keys[pygame.K_LEFT]:
            player_x -= 5
        if keys[pygame.K_RIGHT]:
            player_x += 5
        if keys[pygame.K_UP]:
            player_y -= 5
        if keys[pygame.K_DOWN]:
            player_y += 5



        if keys[pygame.K_LCTRL]:
            if key_repeat_timer == 0 or pygame.time.get_ticks() - key_repeat_timer > NEXT_FIRE_DELAY:
                if fire_cannons < 1:
                    fire_cannons = 1
                fire_start_positions = {
                    1: (player_x + (PLAYER_WIDTH / 2)),
                    2: (player_x + (PLAYER_WIDTH / 2)) - 5,
                    3: (player_x + (PLAYER_WIDTH / 2)) - 10,
                    4: (player_x + (PLAYER_WIDTH / 2)) - 15,
                    5: (player_x + (PLAYER_WIDTH / 2)) - 20
                }
                bullet_start_position = fire_start_positions[fire_cannons]
                for i in range(fire_cannons):
                    player_bullet = pygame.Rect(bullet_start_position, player_y - PLAYER_BULLET_HEIGHT - 2, PLAYER_BULLET_WIDTH, PLAYER_BULLET_HEIGHT)
                    player_bullets.append(player_bullet)
                    key_repeat_timer = pygame.time.get_ticks()
                    bullet_start_position += 10

        if keys[pygame.K_SPACE]:
            if len(collectables) <= 0 and student_assessment_scores["Midterm"] > 0:
                print("missle Fired")
                missile_animation = True


        if len(player_bullets) > 0:
            for bullet in player_bullets:
                if bullet.y <= -PLAYER_BULLET_HEIGHT:
                    player_bullets.remove(bullet)
                else:
                    bullet.y -= 10



        player = pygame.Rect(player_x, player_y, PLAYER_WIDTH, PLAYER_HEIGHT)
        player = [player_image, player]



        player_missile = pygame.Rect(player_missile_x, player_missile_y, PLAYER_WIDTH, PLAYER_HEIGHT)
        player_missile = [missile_image, player_missile]

        y_axis = HEIGHT / 2 - 100
        energies = {}
        for key, value in collectables.items():
            energy = pygame.Rect(WIDTH / 2 + 70, y_axis, 50, 50)
            energy = [energy_image, energy]
            energies[key] = energy
            y_axis += 40

        # Boundaries to keep the player within the screen
        player_x = max(0, min(player_x, WIDTH - PLAYER_WIDTH))
        player_y = max(0, min(player_y, HEIGHT - PLAYER_HEIGHT))

        for key, (energy_image, energy_rect) in energies.items():
            if player[1].colliderect(energy_rect):
                student_assessment_scores[key] = collectables[key]
                del collectables[key]

        if len(collectables) <= 0:
            if time.time() > enemy_next_fire:
                x_axis = 25
                for i in range(4):
                    enemy_bullet = pygame.Rect(x_axis, 50, ENEMY_BULLET_WIDTH, ENEMY_BULLET_HEIGHT)
                    enemy_bullets.append(enemy_bullet)
                    if i != 1:
                        x_axis += 50
                    else:
                        x_axis += 640
                speed_up_bullet = ENEMY_HEALTH / 100
                if ENEMY_HEALTH < 10:
                    speed_up_bullet = 0.2
                enemy_next_fire = time.time() + speed_up_bullet

        if len(enemy_bullets) > 0:
            for bullet in enemy_bullets:
                if bullet.y >= SCREEN_HEIGHT:
                    enemy_bullets.remove(bullet)
                bullet.y += 10

        for bullet in enemy_bullets:
            bullet_rect = pygame.Rect(bullet)
            bullet_mask = pygame.mask.from_surface(pygame.Surface((bullet.width, bullet.height)))
            player_mask = pygame.mask.from_surface(player_image)
            collision = bullet_mask.overlap(player_mask, (player[1].x - bullet_rect.x, player[1].y - bullet_rect.y))
            if collision:
                if time.time() >= limit_fire:
                    student_assessment_scores["Attendance"] = student_assessment_scores["Attendance"] - 1
                    print('I am hit')
                    limit_fire = time.time() + 0.5

        for bullet in main_enemy_bullets:
            bullet_rect = pygame.Rect(bullet)
            bullet_mask = pygame.mask.from_surface(pygame.Surface((bullet.width, bullet.height)))
            player_mask = pygame.mask.from_surface(player_image)
            collision = bullet_mask.overlap(player_mask, (player[1].x - bullet_rect.x, player[1].y - bullet_rect.y))
            if collision:
                if time.time() >= limit_fire:
                    student_assessment_scores["Attendance"] = student_assessment_scores["Attendance"] - 1
                    print('I am hit')
                    limit_fire = time.time() + 0.5

        if len(collectables) <= 0:
            main_enemy_spawn = True
        else:
            main_enemy_spawn_time = time.time() + 4
        if main_enemy_spawn and time.time() > main_enemy_spawn_time:
            enemy_heath = ENEMY_HEALTH
            if ENEMY_HEALTH < 20:
                enemy_heath = 20
            enemy_health_percentage = 100 / enemy_heath
            enemy[1].x += enemy_health_percentage * enemy_movement_direction[0]
            enemy[1].y += enemy_health_percentage * enemy_movement_direction[1]
            x_axis = 150
            if time.time() > main_enemy_next_fire:
                for i in range(5):
                    enemy_bullet = pygame.Rect(enemy[1].x + x_axis, enemy[1].y + 330, ENEMY_BULLET_WIDTH, ENEMY_BULLET_HEIGHT)
                    main_enemy_bullets.append(enemy_bullet)
                    x_axis += 25
                speed_up_bullet = ENEMY_HEALTH / 100
                if ENEMY_HEALTH < 10:
                    speed_up_bullet = 0.2
                main_enemy_next_fire = time.time() + speed_up_bullet

            if len(main_enemy_bullets) > 0:
                for bullet in main_enemy_bullets:
                    if bullet.y >= SCREEN_HEIGHT:
                        main_enemy_bullets.remove(bullet)
                    bullet.y += 10

            if enemy[1].left <= 0 or enemy[1].right >= WIDTH:
                enemy_movement_direction[0] *= -1

            if enemy[1].top <= 0 or enemy[1].bottom >= HEIGHT:
                enemy_movement_direction[1] *= -1

            collision = pygame.mask.from_surface(player[0]).overlap(pygame.mask.from_surface(enemy[0]), (
            enemy[1].x - player[1].x, enemy[1].y - player[1].y))

            if collision:
                print("Collision detected!")

            for bullet in player_bullets:
                # Assuming enemy_image is a pygame.Surface
                # bullet_rect = pygame.Rect(bullet)
                # bullet_mask = pygame.mask.from_surface(pygame.Surface((bullet.width, bullet.height)))
                # enemy_mask = pygame.mask.from_surface(enemy_image)
                # collision = bullet_mask.overlap(enemy_mask, (enemy[1].x - bullet_rect.x, enemy[1].y - bullet_rect.y))
                # if collision:
                #     print("Bullet collided with the enemy!")
                collision_rect_bullet = pygame.Rect(bullet.x + bullet.width // 4, bullet.y + bullet.height // 4,
                                                    bullet.width // 2, bullet.height // 2)
                collision_rect_enemy = pygame.Rect(enemy[1].x + enemy[1].width // 4, enemy[1].y + enemy[1].height // 4,
                                                   enemy[1].width // 2, enemy[1].height // 2)

                if collision_rect_bullet.colliderect(collision_rect_enemy):
                    ENEMY_HEALTH -= 0.10
                    player_bullets.remove(bullet)

            if missile_animation:
                player_missile_y -= player_missile_start_speed
                player_missile_start_speed += 0.5
                # collision = pygame.mask.from_surface(enemy[0]).overlap(pygame.mask.from_surface(player_missile[0]), (
                #     enemy[1].x - player_missile[1].x, enemy[1].y - player_missile[1].y))
                #
                # if collision:
                #     player_missile_y += SCREEN_HEIGHT
                if player_missile[1].colliderect(enemy[1]):
                    player_missile_y += SCREEN_HEIGHT
                    ENEMY_HEALTH = ENEMY_HEALTH - (student_assessment_scores["Midterm"] / 3)
                    student_assessment_scores["Midterm"] = 0
                    missile_animation = False
        if main_enemy_spawn and time.time() < main_enemy_spawn_time:
            enemy[1].y += 1

        show_shield = []
        if ENEMY_HEALTH < 85 or ENEMY_HEALTH < 55 or ENEMY_HEALTH < 35:
            for enemy_missile in enemy_missiles[1]:
                enemy_missile.y += 10
                if enemy_missile.colliderect(player[1]):
                    if time.time() >= limit_fire:
                        if student_assessment_scores["Assignments"] > 2:
                            limit_fire = time.time() + 0.5
                            student_assessment_scores["Assignments"] -= 33
                            shield_acitivated = True
                        else:
                            student_assessment_scores["Attendance"] = student_assessment_scores["Attendance"] - 33
                            enemy_missiles[1].remove(enemy_missile)
                            limit_fire = time.time() + 0.5
                if enemy_missile.y > SCREEN_HEIGHT:
                    enemy_missiles[1].remove(enemy_missile)
                    show_shield.clear()
                    shield_acitivated = False

        if shield_acitivated:
            shield = pygame.Rect(player[1].x - 30, player_y - 30, SHIELD_WIDTH, SHIELD_HEIGHT)
            shield = [shield_image, shield]
            show_shield = [shield]

        clock.tick(60)
        draw(background, player, player_bullets, energies, student_assessment_scores, collectables, enemy_bullets, enemy, ENEMY_HEALTH, main_enemy_bullets, player_missile, enemy_missiles, show_shield)


if __name__ == "__main__":
    main()
