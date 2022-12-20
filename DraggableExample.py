import pygame
import sys
import pygameutilities.Draggable as Draggable

pygame.init()


WIDTH, HEIGHT = 1000, 900

win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Draggable Example")


run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            run = False
            sys.exit()
            break
    Draggable.checkMouse()
    pygame.display.update()