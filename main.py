import pygame
from constant import *
from node import Node


def leftClickHandler(surface, mousePos, nodes, link):
    collide = len(link) == 2
    if not (collide):
        for node in nodes:
            if node.rect.collidepoint(mousePos):
                collide = True
                if len(nodes) >= 2:
                    link.append(node)
                    if len(link) == 1:
                        return link
                break
    if not (collide):
        return Node(pygame.draw.circle(surface, fg, mousePos, nodeRadius, nodeWidth))
    if len(link) == 2 and len(nodes) >= 2:
        print("a")
        Node.connect(link[0], link[1])
        return link


def rightClickHandler(mousePos):
    pass


# Init Pygame Window
pygame.init
screen = pygame.display.set_mode((width, height))
screen.fill(bg)

nodes = []
link = []
edges = []

running = True
while running:
    # Event Handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONUP:
            mousePos = pygame.mouse.get_pos()
            if event.button == 1:
                tmp = leftClickHandler(screen, mousePos, nodes, link)
                if type(tmp) == Node:
                    nodes.append(tmp)
                if type(tmp) == list:
                    link = tmp
                    if len(tmp) == 2:
                        edges.append(pygame.draw.line(
                            screen, fg, link[0].rect.center, link[1].rect.center))
                        link = []
            elif event.button == 3:
                rightClickHandler()
    pygame.display.update()


pygame.quit()
