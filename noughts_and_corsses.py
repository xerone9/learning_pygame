import pygame
import time
import random
pygame.font.init()

WIDTH, HEIGHT = 600, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Noughts And Crosses")

BG_COLOR = (0, 0, 0)
TOP_BAR = HEIGHT / 10

NOUGHT_COLOR = (0, 0, 255)
NOUGHT_WIDTH = 50



FONT = pygame.font.SysFont("comicsans", 30)


def draw(player_signs, cpu_signs, circle_points, cross_points, draw_points):
    # Stage
    WIN.fill(BG_COLOR)
    pygame.draw.rect(WIN, "white", pygame.Rect(0, TOP_BAR, WIDTH, 2))
    pygame.draw.rect(WIN, "white", pygame.Rect(TOP_BAR, int((HEIGHT - TOP_BAR) / 3) + TOP_BAR, WIDTH - (TOP_BAR * 2), 5))
    pygame.draw.rect(WIN, "white", pygame.Rect(TOP_BAR, int((HEIGHT - TOP_BAR) / 3) * 2 + TOP_BAR, WIDTH - (TOP_BAR * 2), 5))
    pygame.draw.rect(WIN, "white", pygame.Rect(WIDTH / 3, TOP_BAR * 2, 5, HEIGHT - (TOP_BAR * 3)))
    pygame.draw.rect(WIN, "white", pygame.Rect((WIDTH / 3) * 2, TOP_BAR * 2, 5, HEIGHT - (TOP_BAR * 3)))


    for player_cords in player_signs:
        pygame.draw.circle(WIN, NOUGHT_COLOR, player_cords, NOUGHT_WIDTH)
        pygame.draw.circle(WIN, (0, 0, 0, 0), player_cords, NOUGHT_WIDTH - (NOUGHT_WIDTH / 5))

    for cpu_cords in cpu_signs:
        pygame.draw.line(WIN, "red", (cpu_cords[0][0], cpu_cords[0][1]), (cpu_cords[1][0], cpu_cords[1][1]), 5)
        pygame.draw.line(WIN, "red", (cpu_cords[1][0], cpu_cords[0][1]), (cpu_cords[0][0], cpu_cords[1][1]), 5)

    circle_text = FONT.render(f'Circle: {circle_points: 2}', 1, "blue")
    WIN.blit(circle_text, (10, 10))

    draw_text = FONT.render(f'Draw: {draw_points: 2}', 1, "yellow")
    WIN.blit(draw_text, (WIDTH/2 - draw_text.get_width()/2, 10))

    cross_text = FONT.render(f'Cross: {cross_points: 2}', 1, "red")
    WIN.blit(cross_text, ((WIDTH - 10) - cross_text.get_width(), 10))

    pygame.display.update()


def main():
    run = True

    turn = "circle"

    mouse_x, mouse_y = 0, 0

    all_positions = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    win_conditions = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 5, 9], [3, 5, 7], [1, 4, 7], [2, 5, 8], [3, 6, 9]]
    winning_lines = {
        "[1, 2, 3]": [(62, 178), (540, 178)],
        "[4, 5, 6]": [(62, 340), (540, 340)],
        "[7, 8, 9]": [(62, 490), (540, 490)],
        "[1, 5, 9]": [(55,120), (550, 540)],
        "[3, 5, 7]": [(550, 120), (55, 540)],
        "[1, 4, 7]": [(122, 120), (122, 540)],
        "[2, 5, 8]": [(305, 120), (305, 540)],
        "[3, 6, 9]": [(483, 120), (483, 540)]
    }
    current_position = 10

    cpu_signs = []
    players_signs = []
    cpu_positions = []
    players_positions = []

    circle_dictionary = {
        "1": (120, 170),
        "2": (300, 170),
        "3": (480, 170),
        "4": (120, 340),
        "5": (300, 340),
        "6": (480, 340),
        "7": (120, 505),
        "8": (300, 505),
        "9": (480, 505)
    }

    cross_dictionary = {
        "1": [(70, 140), (180, 220)],
        "2": [(250, 140), (360, 220)],
        "3": [(430, 140), (540, 220)],
        "4": [(70, 300), (180, 380)],
        "5": [(250, 300), (360, 380)],
        "6": [(430, 300), (540, 380)],
        "7": [(70, 450), (180, 530)],
        "8": [(250, 450), (360, 530)],
        "9": [(430, 450), (540, 530)]
    }

    circle_points = 0
    cross_points = 0
    draw_points = 0

    turn_lock = time.time()

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # Get the position of the mouse click
                if time.time() >= turn_lock:
                    pos = pygame.mouse.get_pos()
                    # print(f"Mouse button {event.button} clicked at {pos}")
                    mouse_x, mouse_y = pos

            elif event.type == pygame.MOUSEMOTION:
                # Get the current position of the mouse cursor
                pos = pygame.mouse.get_pos()
                # print(f"Mouse moved to {pos}")



        if mouse_x <= 199 and mouse_y >= TOP_BAR and mouse_y <= 241 :
            current_position = 1
        elif mouse_x <= 199 and mouse_y >= 244 and mouse_y <= 421 :
            current_position = 4
        elif mouse_x <= 199 and mouse_y >= 423:
            current_position = 7

        elif mouse_x >= 203 and mouse_x <= 401 and mouse_y >= TOP_BAR and mouse_y <= 241 :
            current_position = 2
        elif mouse_x >= 203 and mouse_x <= 401 and mouse_y >= 244 and mouse_y <= 421 :
            current_position = 5
        elif mouse_x >= 203 and mouse_x <= 401 and mouse_y >= 423:
            current_position = 8

        elif mouse_x >= 402 and mouse_y >= TOP_BAR and mouse_y <= 241 :
            current_position = 3
        elif mouse_x >= 402 and mouse_y >= 244 and mouse_y <= 421 :
            current_position = 6
        elif mouse_x >= 402 and mouse_y >= 423:
            current_position = 9

        if turn == "circle":
            if current_position in all_positions:
                player_cords = circle_dictionary[str(current_position)]
                players_signs.append(player_cords)
                all_positions.remove(current_position)
                players_positions.append(current_position)
                turn = "cross"
        else:
            if current_position in all_positions:
                cpu_cords = cross_dictionary[str(current_position)]
                cpu_signs.append(cpu_cords)
                all_positions.remove(current_position)
                cpu_positions.append(current_position)
                turn = "circle"

        draw(players_signs, cpu_signs, circle_points, cross_points, draw_points)

        for sublist in win_conditions:
            if set(sublist).issubset(set(players_positions)):
                lost_text = FONT.render("Circle Wins", 1, "white")
                WIN.blit(lost_text, (WIDTH / 2 - lost_text.get_width() / 2, HEIGHT / 2 - lost_text.get_height() / 2))
                pygame.draw.line(WIN, "green", winning_lines[str(sublist)][0], winning_lines[str(sublist)][1], 5)
                pygame.display.update()
                pygame.time.delay(2000)
                all_positions = [1, 2, 3, 4, 5, 6, 7, 8, 9]
                circle_points += 1
                cpu_signs.clear()
                players_signs.clear()
                cpu_positions.clear()
                players_positions.clear()
                current_position = 10
                mouse_x, mouse_y = -1, -1
                turn_lock = time.time() + 0.2
                break
            elif set(sublist).issubset(set(cpu_positions)):
                lost_text = FONT.render("Cross Wins", 1, "white")
                WIN.blit(lost_text, (WIDTH / 2 - lost_text.get_width() / 2, HEIGHT / 2 - lost_text.get_height() / 2))
                pygame.draw.line(WIN, "green", winning_lines[str(sublist)][0], winning_lines[str(sublist)][1], 5)
                pygame.display.update()
                pygame.time.delay(2000)
                all_positions = [1, 2, 3, 4, 5, 6, 7, 8, 9]
                pygame.display.update()
                cross_points += 1
                cpu_signs.clear()
                players_signs.clear()
                cpu_positions.clear()
                players_positions.clear()
                current_position = 10
                mouse_x, mouse_y = -1,-1
                turn_lock = time.time() + 0.2
                break

        if len(all_positions) <= 0:
            lost_text = FONT.render("Its a Draw", 1, "white")
            WIN.blit(lost_text, (WIDTH/2 - lost_text.get_width()/2, HEIGHT/2 - lost_text.get_height()/2))
            pygame.display.update()
            pygame.time.delay(2000)
            all_positions = [1, 2, 3, 4, 5, 6, 7, 8, 9]
            draw_points += 1
            cpu_signs.clear()
            players_signs.clear()
            cpu_positions.clear()
            players_positions.clear()
            current_position = 10
            mouse_x, mouse_y = -1, -1

    pygame.quit()


if __name__ == "__main__":
    main()
