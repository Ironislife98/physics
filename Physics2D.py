import pygame.math
import math

Attractors = []

G = 6.6743 * (10 ** -11)


class RigidBody2D:
    def __init__(self, mass, drag):
        self.mass = mass
        self.drag = drag

    def addForce(self, initialVector, moveTowards, force):
        """Takes in initialVector and forceVector and returns Vector2 of initalVector moved towards a vector by a force"""
        return initialVector.move_towards(moveTowards.xy, force)


class Attractor:
    def __init__(self, RigidBody, childClass):
        self.childClass = childClass
        Attractors.append(self.childClass)

    def update(self):
        toreturn = []
        for attractor in Attractors:
            if attractor.childClass.name != self.childClass.name:
                toreturn.append(self.Attract(attractor))
        """temp = pygame.Vector2(0, 0)
        for item in toreturn:
            temp = temp + item"""
        return toreturn

    def Attract(self, objToAttract):
        """
        All params need to have .vector -> pygame.Vector2 and .mass -> int/float values
        """
        # F = ((m1 * m2) / d^2) * G
        direction = self.childClass.vector - objToAttract.vector
        distance = direction.magnitude()
        try:
            forcemagnitude =  G * (self.childClass.rb.mass * objToAttract.rb.mass) / math.pow(distance, 2)
            # Calculate Euclidian distance Instead
            force = direction.normalize() * forcemagnitude
        except ZeroDivisionError:
            force = pygame.math.Vector2(0, 0)
        force = force.distance_to(objToAttract.vector)
        # Add some force
        # How?
        # return pygame.math.Vector2.move_towards(objToAttract.vector, force)
        return self.rb.addForce(self.childClass.vector, objToAttract.vector, force)



def findGround(height, objx, listOfGround):
    # for all positions, get ground y value, calculate before game runs
    # store in dict
    # access for gravity
    for y in range(height):
        for rect in listOfGround:
            #print(objx, y)
            pygame.draw.rect(win, (0, 0, 255), pygame.Rect(objx, y, 10, 1))
            if rect.collidepoint(objx, y):
                print(objx, y)

def update(smallMass: float, largeMass: float, smallVector: pygame.math.Vector2, largeVector: pygame.math.Vector2) -> pygame.math.Vector2:
    #findGround(900, smallVector.x, [pygame.Rect(largeVector.x, largeVector.y, 1000, 1000)])
    distance = smallVector.distance_to(largeVector)
    try:
        # f = G * (m1 * m2 / d^2)
        force = G * ((smallMass * largeMass) / distance)
        # f = GM / d^2
        # force = (G * largeMass) / distance
    except ZeroDivisionError:
        force = 0
    # print(f"Force: {force}, Distance: {distance}")
    return smallVector.move_towards(largeVector, force)

