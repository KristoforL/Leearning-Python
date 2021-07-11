import pygame as pg
from pygame.sprite import Sprite
from sys import platform
import os

class Alien(Sprite):
    """A class to represent a single alien in the fleet"""

    def __init__(self, ai_game):
        """Initialize the alien and set its starting position"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings=ai_game.settings


        #Load the alien image and set its rect attribute
        if platform == "linux" or platform == "linux2":
            #linux
            self.image = pg.image.load('Day 30\images\alien.bmp')
        elif platform == "darwin":
            # OS X
            self.image = pg.image.load('Alien _Invasion/images/alien.bmp')
        elif platform == "win32":
            # Windows...
            self.image = pg.image.load('Day 30\images\alien.bmp')

        self.rect = self.image.get_rect()

        #Start each new alien near the top left of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        #Store the aliens exact horizontal position
        self.x = float(self.rect.x)

    def check_edges(self):
        """Return True if alien is at edge of screen"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True

    def update(self):
        """Move the alien to the right"""
        self.x += (self.settings.alien_speed *self.settings.fleet_direction)
        self.rect.x =self.x

    