import pygame
import pygamegame #the framework

class myProject(pygamegame.PygameGame):
    def init(self):
        self.message = "World Helo"
    def mousepressed(self, x, y):
        print("It's working!!!")
        print(self.message)

#creating and running the game
game = myProject()
game.run()
