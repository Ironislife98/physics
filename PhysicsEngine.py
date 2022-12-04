from typing import Optional

from pygame import sprite


class PhysicsEngine:
    def __init__(self):
        self.distance = 0

    def earthGravity(self, smallmass: float, largemass_y: float, smallmass_y: float, distance=None) -> float:
        """Returns a float containing the change in y-value needed to simulate gravity"""
        if not distance:
            self.distance = (6.4 * (10 ** 6)) ** 2
        else:
            self.distance = distance
        try:
            force = ((6.67 * (10 ** -11)) * (6 * 10 ** 24) * smallmass) / self.distance
        except ZeroDivisionError:
            force = 0
        return force

    def verticalCollision(self, obj1, collisionobjs: list[any], dy: float) -> list[any]:
        """Returns a list of objects that a object has collided with, the index of the, and the type of collision
            Assumes all objects have values for object.vector, object.rect, object.height"""
        collided_objects = []
        for obj in collisionobjs:
            if sprite.collide_mask(obj1, obj):
                if dy > 0:
                    # Player hit floor
                    obj1.rect.bottom = obj.rect.top
                elif dy < 0:
                    # Player hit roof
                    obj1.rect.top = obj.rect.bottom
                collided_objects.append(obj)
        """for obj in collisionobjs:
            if obj1.rect.colliderect(obj.rect):
                obj1.rect.bottom = obj.rect.top
                collided_objects.append(obj)"""
        return collided_objects
