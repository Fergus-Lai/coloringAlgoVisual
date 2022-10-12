import pygame
from constant import *

pygame.init

width, height = 900, 900
screen = pygame.display.set_mode((width, height))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill(black)

pygame.quit()
