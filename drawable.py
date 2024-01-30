from spriteManager import SpriteManager
import pygame

"""
Drawable class represents an image with a filename, position, and image 
as attributes that can be drawn to a surface
"""
class Drawable(object):
    def __init__(self, filename, position, offset = None):
        self.filename = filename
        self.position = position
        SM = SpriteManager.getInstance()
        self.image = SM.getSprite(self.filename, offset)

    def draw(self, drawSurface):
        """ blits drawable image to the drawsurface given """
        drawSurface.blit(self.image, list(map(int, self.position)))
        