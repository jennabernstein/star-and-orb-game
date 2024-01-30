from mobile import Mobile
from vector import vec
import random

"""
By: Jenna Bernstein 
A class for an orb mobile object that moves on its own with a random color and velocity 
"""
class Orb(Mobile):
    def __init__(self, position, color):
        super().__init__("orb.png", position)
        self.pos = position
        self.vel = self.randomVector()
        self.color = color
        

    def updateColor(self):
        """ update the color of the orb while maintaining its transparent background"""
        self.colored = self.image.copy()
        colorKey = self.image.get_at((0,0))
        self.colored.set_colorkey(colorKey)
        for x in range(self.colored.get_width()):
            for y in range(self.colored.get_height()):
                if self.colored.get_at((x, y)) != colorKey:
                    self.colored.set_at((x, y), self.color)


    def draw(self, drawSurface):
        """ draw the new colored image to the surface"""
        drawSurface.blit(self.colored, self.pos)
    
    def setVelocity(self, vector):
        """ set the velocity of the orb """
        self.vel = vector

    def setColorKey(self, position):
        """ set the color key of the orb """
        self.image.set_colorkey(position)

    def randomVector(self):
        """ return a random vector for the orb """
        posOrNeg = [0,1,2,3]
        parity = random.choice(posOrNeg)
        if parity <= 1:
            xVal = random.randint(100, 150)
        else:
            xVal = random.randint(-150, -100)
        if parity == 1 or parity == 3:
            yVal = random.randint(-150, -100)
        else:
            yVal = random.randint(100, 150)
        return vec(xVal, yVal)


