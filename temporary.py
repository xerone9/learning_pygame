import pygame

pygame.init()
screen = pygame.display.set_mode((640, 480))
clock = pygame.time.Clock()

space_pressed = False  # variable to keep track of the space key state
prev_space_state = False  # variable to keep track of the previous space key state

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    keys = pygame.key.get_pressed()
    prev_space_state = space_pressed
    space_pressed = keys[pygame.K_SPACE]

    if space_pressed and not prev_space_state:
        print("Space bar pressed")

    if keys[pygame.K_ESCAPE]:
        pygame.quit()
        quit()

    screen.fill((255, 255, 255))
    pygame.display.flip()
    clock.tick(60)
