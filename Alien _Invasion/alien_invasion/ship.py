import pygame as pg
from pygame.sprite import Sprite
from sys import platform
import os

class Ship(Sprite):
    """A class to manage the ship"""

    def __init__(self, ai_game):
        """Initialize the ship and set its starting position"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        #Load the ship image and get its rect.
        if platform == "linux" or platform == "linux2":
            #linux
            self.image = pg.image.load('images\ship.bmp')
        elif platform == "darwin":
            # OS X
            self.image = pg.image.load('Alien _Invasion/images/ship.bmp')
        elif platform == "win32":
            # Windows...
            self.image = pg.image.load('images\ship.bmp')

        self.rect = self.image.get_rect()

        #Start each new ship at the bottom center of the screen
        self.rect.midbottom = self.screen_rect.midbottom

        #Store a decimal value for the ship's horizontal position.
        self.x = float(self.rect.x)

        #Movement flag
        self.moving_right = False
        self.moving_left = False


    def update(self):
        """Update the ships position based on movement flag"""
        #Update the ships x value, not the rect
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
        
        #update rect object from self.x
        self.rect.x =self.x


    def blitme(self):
        """Draw the ship at its current location"""
        self.screen.blit(self.image, self.rect)


    def center_ship(self):
        """Center the ship on the screen"""
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)

    
