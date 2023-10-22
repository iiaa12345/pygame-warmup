import pygame
import pathlib


# init pygame engine
pygame.init()

# set up the drawing window
screen = pygame.display.set_mode([800, 600])

# load sprite image
images_path = str(pathlib.Path().resolve()) + "/images/"
img = pygame.image.load(images_path + "sprite.png").convert_alpha()

x = 400 - img.get_rect().width / 2
y = 300 - img.get_rect().height / 2

# run main game loop
running = True
while running:
    # process event from pygame events queue
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the background with color in RGB format
    screen.fill((40, 44, 52))

    # draw sprite image
    x = 400 - img.get_rect().width / 2
    y = 300 - img.get_rect().height / 2
    screen.blit(img, (x, y))

    # TODO: draw your loaded sprite image

    # flip the display
    pygame.display.flip()

# quit pygame engine
pygame.quit()
