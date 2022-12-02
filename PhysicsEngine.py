from pygame import sprite

class PhysicsEngine:
    def __init__(self):
        self.distance = 0
        self.overrideDistance = False

    def earthGravity(self, smallmass: float, largemass_y: int, smallmass_y: int) -> float:
        """Returns a float containing the change in value needed to simulate gravity"""
        if not self.overrideDistance:
            self.distance = (6.4 * (10 ** 6)) ** 2
        try:
            force = ((6.67 * (10 ** -11)) * (6 * 10 ** 24) * smallmass) / self.distance
        except ZeroDivisionError:
            force = 0
        return force

    def verticalCollision(self, obj1, collisionobjs: list[any], dy: float, top_collision=None, bottom_collision=None) -> list[any]:
        """Returns a list of objects that a object has collided with and runs function on collision if given one"""
        collided_objects = []
        for obj in collisionobjs:
            if sprite.collide_mask(obj1, obj):
                if dy > 0:
                    obj1.rect.bottom = obj.rect.top
                    if bottom_collision != None:
                        bottom_collision()
                elif dy < 0:
                    obj1.rect.top = obj.rect.bottom
                    if top_collision != None:
                            top_collision()
                collided_objects.append(obj)
        
        return collided_objects
