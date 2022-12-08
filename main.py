import pygame
import SmallObject
import time
import Physics2D

pygame.init()

WIDTH, HEIGHT = 1000, 900
win = pygame.display.set_mode((WIDTH, HEIGHT))


obj1 = SmallObject.smallObject(100, 100, 100, 100, 1000000, color=(255, 0, 0))
obj2 = SmallObject.smallObject(100, 500, 1000, 1000, 10000000, name="Ground1")


run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            run = False
            break


    win.fill((255, 255, 255))
    obj2.draw(win)
    obj1.draw(win)


    pygame.draw.rect(win, (0, 255, 0), pygame.Rect(obj1.bottom.x, obj1.bottom.y, 10, 10))
    movetowards = Physics2D.update(obj1.rb.mass, obj2.rb.mass, pygame.math.Vector2(obj1.vector.x, obj1.vector.y), obj2.vector)
    #print(movetowards)
    obj1.vector = movetowards
    print(obj1.vector, obj2.vector)
    pygame.display.update()