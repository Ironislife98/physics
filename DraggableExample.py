import pygame
import sys
import pygameutilities.Draggable as Draggable
import pygameutilities.objectClasses as objectClasses


pygame.init()


WIDTH, HEIGHT = 1000, 900

win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Draggable Example")


def draw():
    win.fill((255, 255, 255))
    pygame.draw.rect(win, (255, 0, 0), pygame.Rect(p.vector.x, p.vector.y, p.width, p.height))


p = objectClasses.physicsObject(100, 100, 100, 100, 1000, "Example Player")
currentlydragging = False

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            run = False
            sys.exit()
            break
    if pygame.mouse.get_pressed(num_buttons=3)[0] or currentlydragging:
        currentlydragging = True
        mousepos = pygame.math.Vector2(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])
        dragpoint = Draggable.move_object(p.rect, mousepos)
        if dragpoint != None:
            p.vector = dragpoint
        else:
            currentlydragging = False
    else:
        currentlydragging = False
    draw()
    pygame.display.update()