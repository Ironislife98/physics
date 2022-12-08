import pygame
import SmallObject
import time

pygame.init()

WIDTH, HEIGHT = 1000, 900
win = pygame.display.set_mode((WIDTH, HEIGHT))


obj1 = SmallObject.smallObject(300, 100, 100, 100, 1)
obj2 = pygame.Vector2(300, 700)

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            run = False
            break
    win.fill((255, 255, 255))

    obj1.vector.move_towards_ip(obj2, 9.8)
    obj1.draw(win)
    distance = obj1.vector.distance_to(obj2)
    if distance == 0:
        obj1.vector = pygame.Vector2(300, 100)
    print(obj1.vector.xy)
    pygame.display.update()