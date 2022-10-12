import pygame
from constant import *


# Init Pygame Window
pygame.init
screen = pygame.display.set_mode((width, height))

running = True
while running:
    # Event Handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill(black)

pygame.quit()
