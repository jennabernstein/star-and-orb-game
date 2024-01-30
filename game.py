
import pygame
from vector import vec, rectAdd
from random import randint
import numpy as np
from constants import SCALE
from drawable import Drawable
from Star import Star
from Orb import Orb

"""
Game Engine class contains the main information and specifics of the game, utilizing classes 
such as mobile, drawable, star, and orb to work with the draw surface
Draws, handles events, and updates for the main driver of the code according to this specific game
"""
class GameEngine(object):
    def __init__(self):
        # set size of screen to 800x800
        self.RESOLUTION = vec(800, 800)
        self.background = Drawable("blueBackground.jpeg", vec(0,0))

        # create star in middle of screen
        self.star = Star((385, 385))
        # make background of star transparent
        self.star.setColorKey(self.star.image.get_at((0,0)))

        # initialize orb list
        self.orbs = []

        # initialize other variables necessary
        self.maxVel = 250
        self.acceleration = 75
        self.count = 0

    def draw(self, drawSurface):
        """
        Draws items to the drawsurface provided
        """
        drawSurface.fill((255,255,255))
        self.background.draw(drawSurface)

        # blit star to screen here
        self.star.draw(drawSurface)
        self.starRect = pygame.Rect(self.star.pos[0], self.star.pos[1], self.star.image.get_width(), self.star.image.get_height())

        # keep track of score
        font = pygame.font.SysFont("Arial", 20)
        score = font.render("Score: ", False, (0, 0, 0))
        scoreNum = font.render(str(self.count), False, (0, 0, 0))
        drawSurface.blit(score, (700, 0))
        drawSurface.blit(scoreNum, (775, 0))

        # draw orbs to screen here
        for o in self.orbs:
            o[0].draw(drawSurface)
            
    def handleEvent(self, event):
        """
        Handles and event given
        - key down: accelerates/ decelerates depending on direction clicked and direction it was going before
        - mouse button down: creates orb with random color and velocity
        """
        if event.type == pygame.KEYDOWN:
            # check if star velocity is less than max
            # then, accelerate/ decelerate depending on direction clicked and direction it was going before
            if event.key == pygame.K_DOWN:
                if self.star.vel[1] < self.maxVel:
                    self.star.vel[1] += self.acceleration
            elif event.key == pygame.K_UP:
                if self.star.vel[1] > (-1 * self.maxVel):
                    self.star.vel[1] -= self.acceleration
            elif event.key == pygame.K_LEFT:
                if self.star.vel[0] > (-1 * self.maxVel):
                    self.star.vel[0] -= self.acceleration
            elif event.key == pygame.K_RIGHT:   
                if self.star.vel[0] < self.maxVel:
                    self.star.vel[0] += self.acceleration     
        
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # when mouse is clicked, save position
            oPos = vec(*event.pos) - vec(50/2,50/2)
            # create random color for orb
            color1 = randint(0, 255)
            color2 = randint(0,255)
            color3 = randint(0,255)
            color = (color1, color2, color3)
            # create new orb
            orb = Orb(oPos, color)
            orb.updateColor()
            orbRect = pygame.Rect(orb.pos[0], orb.pos[1], orb.image.get_width(), orb.image.get_height())
            # add orb to the list of orbs with its hitbox
            self.orbs.append([orb, orbRect])

    def update(self, seconds):
        """
        update items in the game (orbs and stars) according to the seconds given
        """
        # update the star velocity
        self.star.pos += self.star.vel * seconds
        self.star.update(seconds)
        # apply the bouncing feature to the star
        if self.star.pos[0] < 0 or self.star.pos[0] > self.RESOLUTION[0] - self.star.image.get_width():
            self.star.vel[0] *= -1
        if self.star.pos[1] < 0 or self.star.pos[1] > self.RESOLUTION[1] - self.star.image.get_height():
            self.star.vel[1] *= -1

        orbs_copy = self.orbs.copy()
        for o in orbs_copy:
            # update orb location according to velocity
            o[0].update(seconds)
            # update hitbox rectangle with the orb's new position
            o[1] = pygame.Rect(o[0].pos[0], o[0].pos[1], o[0].image.get_width(), o[0].image.get_height())
            # apply the bouncing feature to the star
            if o[0].pos[0] < 0 or o[0].pos[0] > self.RESOLUTION[0] - o[0].image.get_width():
                o[0].vel[0] *= -1
            if o[0].pos[1] < 0 or o[0].pos[1] > self.RESOLUTION[1] - o[0].image.get_height():
                o[0].vel[1] *= -1
            # track if the star and an orb collid
            if o[1].colliderect(self.starRect):
                # increment score
                self.count += 1
                # remove that orb
                self.orbs.remove(o)