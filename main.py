import pygame
from constant import *


def leftClickHandler(surface, mousePos, nodes, link):
    collide = link != []
    if not (collide):
        for node in nodes:
            if node.collidepoint(mousePos):
                collide = True
                break
    if not (collide):
        return pygame.draw.circle(surface, fg, mousePos, nodeRadius, nodeWidth)


def rightClickHandler(mousePos):
    pass


# Init Pygame Window
pygame.init
screen = pygame.display.set_mode((width, height))
screen.fill(bg)

nodes = []

running = True
while running:
    # Event Handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONUP:
            mousePos = pygame.mouse.get_pos()
            if event.button == 1:
                tmp = leftClickHandler(screen, mousePos, nodes, [])
                if type(tmp) == pygame.Rect:
                    nodes.append(tmp)
            elif event.button == 3:
                rightClickHandler()
    pygame.display.update()


pygame.quit()
