'''
GameObject.py
implements the base GameObject class
#each object will have a size, coordinates, and image
Structure from Lukas Peraza Pygame Lecture
'''
import pygame


class GameObject(pygame.sprite.Sprite):
    def __init__(self, x, y, image, radius):
        super(GameObject, self).__init__()
        # x, y define the center of the object
        self.x, self.y, self.image, self.radius = x, y, image, radius
        self.baseImage = image.copy()  # non-rotated version of image
        w, h = image.get_size() #get size of image, be able to resize
        #cats will have to walk around, using different images to look
        #like animation


    def updateRect(self):
        # update the object's  attribute with the new coordinates
        pass

    def update(self, screenWidth, screenHeight):
        pass
