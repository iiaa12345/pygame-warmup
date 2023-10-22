import pygame
import pathlib


# init pygame engine
pygame.init()

# set up the drawing window
screen = pygame.display.set_mode([800, 600])

# setup the clock for a decent framerate
clock = pygame.time.Clock()

# load sprite image
images_path = str(pathlib.Path().resolve()) + "/images/"
img = pygame.image.load(images_path + "alien.png").convert_alpha()

# sprite initial coords
x = 400 - img.get_rect().width / 2
y = 300 - img.get_rect().height / 2

# run main game loop
running = True
while running:
    # process event from pygame events queue
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x -= 1
            elif event.key == pygame.K_RIGHT:
                x += 1
            elif event.key == pygame.K_UP:
                y -= 1
            elif event.key == pygame.K_DOWN:
                y += 1

    # fill the background with color in RGB format
    screen.fill((40, 44, 52))

    # draw sprite image
    screen.blit(img, (x, y))

    # TODO: implement alien movement on left, right, up and down key events

    # flip the display
    pygame.display.flip()

    # maintain 30 FPS
    clock.tick(30)

# quit pygame engine
pygame.quit()
