import pygame
import pathlib
from math import *


pygame.init()
screen = pygame.display.set_mode([800, 600])
clock = pygame.time.Clock()
images_path = str(pathlib.Path().resolve()) + "/images/"
img = pygame.image.load(images_path + "alien.png").convert_alpha()

vec = 40
v0 = 80
x = 1
y = 550
vx = -1 * v0 * cos(vec)
vy = -1 * v0 * sin(vec)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((40, 44, 52))
    screen.blit(img, (x, y))

    if y <= 550:
        vy += 10 / 75
        x += vx / 75
        y += vy / 75

    pygame.display.flip()
    clock.tick(75)

pygame.quit()
