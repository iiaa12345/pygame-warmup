import pygame
import pathlib


pygame.init()

screen = pygame.display.set_mode([800, 600])

clock = pygame.time.Clock()

images_path = str(pathlib.Path().resolve()) + "/images/"
img = pygame.image.load(images_path + "alien.png").convert_alpha()

x = 400 - img.get_rect().width / 2
y = 300 - img.get_rect().height / 2
v = 0

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((40, 44, 52))
    screen.blit(img, (x, y))

    if y < 550:
        v += 10 / 75
        y += v / 75

    pygame.display.flip()
    clock.tick(75)

pygame.quit()
