'''
Cat.py
Implements the Cat Class, which is the object that the user plays as
'''
import pygame
import math
from GameObject import GameObject

class Cat(gameObject):
    @staticmethod
    def init():
        pass
        #load image of cat only once

    def __init__(self, x, y):
        super(Cat, self).__init__(x, y, Cat.catImage, 30)
        self.happy = 1
        self.hungry = 0.9
        self.sleepy = 5
        self.timeAlive = 0 #amount of time the game has been running

    def update(self, dt, keysDown, xPos, yPos):
        self.timeAlive += dt

        if keysDown(pygame.K_LEFT):
            pass
            #move left

        if keysDown(pygame.K_RIGHT):
            pass
            #move right

        if keysDown(pygame.K_UP):
            pass
            #move up
        if keysDown(pygame.K_DOWN):
            pass
            #move down

        super(Cat, self).update(screenWidth, screenHeight)

    #def walk(x, y)

    #def enter(x, y)
        #this is to enter a game mode or look at an animation
