WIDTH, HEIGHT = 800, 600
POWER_RADIUS = 11
RESPAWN_POWER = 14
POWER_DURATION = 7

CIRCLE_RADIUS = 50
CIRCLE_VELOCITY = 5
RESPAWN_CIRCLE = 5

PLAYER_WIDTH = 25
PLAYER_HEIGHT = 25
PLAYER_VEL = 5

try:
    with open("settings.ini") as file:
        data = file.readlines()
        for line in data:
            if line.startswith("#") or line.startswith("\n"):
                pass
            else:
                values = str(line.strip())
                if line.startswith(WIDTH):
                    WIDTH = values.split(" = ")[1]
                if line.startswith(HEIGHT):
                    HEIGHT = values.split(" = ")[1]
                if line.startswith(POWER_RADIUS):
                    POWER_RADIUS = values.split(" = ")[1]
                if line.startswith(RESPAWN_POWER):
                    RESPAWN_POWER = values.split(" = ")[1]
                if line.startswith(POWER_DURATION):
                    POWER_DURATION = values.split(" = ")[1]
                if line.startswith(CIRCLE_RADIUS):
                    CIRCLE_RADIUS = values.split(" = ")[1]
                if line.startswith(CIRCLE_VELOCITY):
                    CIRCLE_VELOCITY = values.split(" = ")[1]
                if line.startswith(RESPAWN_CIRCLE):
                    RESPAWN_CIRCLE = values.split(" = ")[1]
                if line.startswith(PLAYER_WIDTH):
                    PLAYER_WIDTH = values.split(" = ")[1]
                if line.startswith(PLAYER_HEIGHT):
                    PLAYER_HEIGHT = values.split(" = ")[1]
                if line.startswith(PLAYER_VEL):
                    PLAYER_VEL = values.split(" = ")[1]



except FileNotFoundError:
    pass