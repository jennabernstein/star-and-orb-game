from drawable import Drawable
from vector import vec

"""
Mobile is a child of the Drawable class which also has a velocity and an update method to track it
"""
class Mobile (Drawable):
    def __init__(self, filename, position, offset=None):
        super().__init__(filename, position, offset)
        self.vel = vec(0,0)
        

    def update(self, seconds):
          self.position += self.vel * seconds
          