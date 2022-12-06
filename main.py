import pygame
import SmallObject
import time

pygame.init()

WIDTH, HEIGHT = 1000, 900
win = pygame.display.set_mode((WIDTH, HEIGHT))


obj1 = SmallObject.smallObject(100, 100, 100, 100, 1)
obj2 = SmallObject.smallObject(400, 500, 100, 100, 1, name="Ground1")


run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            run = False
            break


    win.fill((255, 255, 255))

    obj1.draw(win)
    obj2.draw(win)

    for vector in obj1.update():
        obj1.vector.move_towards_ip(vector, 100)
    for vector in obj2.update():
        obj2.vector.move_towards_ip(vector, 10)
    print(obj1.vector, obj2.vector)
    pygame.display.update()