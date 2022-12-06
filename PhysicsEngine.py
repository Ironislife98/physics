from typing import Optional

from pygame import sprite, Vector2


class PhysicsEngine:
    def __init__(self):
        self.distance = 0

    def earthGravity(self, smallmass: float, vector1, vector2, largemass_y: float, smallmass_y: float, distance=None) -> float:
        """Returns a float containing the change in y-value needed to simulate gravity"""
        """if not distance:
            self.distance = (6.4 * (10 ** 6)) ** 2
        else:
            self.distance = distance
        self.distance = ((vector2.y - vector1.y) / 100) * (10 ** 6.7)
        if self.distance < 0:
            force = 0
        else:
            force = ((6.67 * (10 ** -11)) * (6 * 10 ** 24) * smallmass) / self.distance ** 2"""
        self.distance = ((vector2.y - vector1.y) / 100) * (10 ** 6.7)
        force = (9.8 * smallmass) / self.distance
        print(force)
        return force

    def verticalCollision(self, object, collisionobjs):
        ObjectY = range(int(object.vector.y), int(object.vector.y + object.height))
        for i in collisionobjs:
            yrange = range(int(i.vector.y), int(i.vector.y + object.height))
            print(yrange in ObjectY)
    
    def horizontalCollision(self):
        pass
