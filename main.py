import pygame
import SmallObject
import time
import Physics2D
import Collision2D

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

    collide = Collision2D.detectCollision(obj1, [obj2])
    if collide[0] and obj1.jumping:
        obj1.rect.bottom = collide[1].rect.top
        obj1.vector.y = obj1.rect.top
        obj1.jumping = False
        print("colllide")
        #obj1.vector = pygame.math.Vector2(10, 100)
    elif not collide[0] and obj1.jumping:
        movetowards = Physics2D.update(obj1.rb.mass, obj2.rb.mass, pygame.math.Vector2(obj1.vector.x, obj1.vector.y), obj2.vector)
        obj1.vector.y = movetowards.y
        #print("move down")
    pygame.draw.rect(win, (0, 255, 0), pygame.Rect(obj1.bottom.x, obj1.bottom.y, 10, 10))   
    #print(movetowards)
    
    #print(obj1.vector, obj2.vector)
    pygame.display.update()