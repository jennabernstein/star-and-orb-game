from drawable import Drawable
from mobile import Mobile
import numpy as np

"""
By: Jenna Bernstein
A class for the star that is a mobile object
"""
class Star(Mobile):

    def __init__(self, position):
        super().__init__("star.png", position)
        self.pos = position

    def getPos(self):
        """ return the position of the star """
        return self.pos

    def getVel(self):
        """ return the velocity of the star """
        return self.vel
    
    def setPos(self, pos):
        """ set the position of the star """
        self.pos = pos
    
    def setVel(self, vel):
        """ set the velocity of the star """
        self.vel = vel
    
    def setColorKey(self, position):
        """ set the color key of the star """
        self.image.set_colorkey(position)