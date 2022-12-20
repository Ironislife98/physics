import pygame
from pygame import Rect
import pygameutilities.Physics2D as Physics2D
import pygameutilities.Collision2D as Collision2D
from pygameutilities.objectClasses import physicsObject

pygame.init()

WIDTH, HEIGHT = 1000, 900
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Physics Example")


groundObjects = []


class smallObject(physicsObject):
    def __init__(self, x, y, width, height, mass, name="smallObject", color=(0, 0, 0)):
        super().__init__(x, y, width, height, mass, name)
        self.jumping = True
        self.color = color

    def draw(self, surface):
        self.rect = Rect(self.vector.x, self.vector.y, self.width, self.height)
        pygame.draw.rect(surface, self.color, self.rect)


obj1 = smallObject(100, 100, 100, 100, 100000, color=(255, 0, 0))
obj2 = smallObject(200, 800, 1000, 1000, 100000000, name="Ground1")
obj3 = smallObject(300, 100, 100, 100, 100000, color=(255, 0, 0))
obj4 = smallObject(600, 600, 1000, 1000, 100000000)

groundObjects.append(obj2)
groundObjects.append(obj4)

gravObject = Physics2D.Gravity(windowHeight=HEIGHT)
gravObject.precomputeGround([obj2.rect])


def jump():
    if not obj1.spacebarPressed:
        obj1.jumping = True
        obj1.spacebarPressed = True



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
    obj3.draw(win)
    obj4.draw(win)

    collide = Collision2D.detectCollision(obj1, groundObjects)
    if collide[0] and obj1.jumping:
        obj1.rect.bottom = collide[1].rect.top
        obj1.vector.y = obj1.rect.top
        obj1.jumping = False
        obj1.spacebarPressed = False
    elif not collide[0] and obj1.jumping:
        movetowards = gravObject.update(obj1.rb.mass, obj2.rb.mass, pygame.math.Vector2(obj1.vector.x, obj1.vector.y), obj2.vector)
        obj1.vector.y = movetowards.y

    collide = Collision2D.detectCollision(obj3, groundObjects)
    if collide[0] and obj3.jumping:
        obj3.rect.bottom = collide[1].rect.top
        obj3.vector.y = obj3.rect.top
        obj3.jumping = False
    elif not collide[0] and obj3.jumping:
        movetowards = gravObject.update(obj3.rb.mass, obj2.rb.mass, pygame.math.Vector2(obj3.vector.x, obj3.vector.y), obj2.vector)
        obj3.vector.y = movetowards.y

    if pygame.key.get_pressed()[pygame.K_SPACE]:
        jump()

    if pygame.mouse.get_pressed()[0]:
        obj1.vector.xy = pygame.mouse.get_pos()
        obj1.jumping = True


    #print(obj1.vector, obj2.vector)
    pygame.display.update()