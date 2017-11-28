import pygame
import pygamegame #the framework


class myProject(pygamegame.PygameGame):

    def init(self):
        self.mode = "welcome"
        self.playButtonColor = (249,194,209)
        self.x = 50
        self.y = 50
        print("init")
        pass

    def mousePressed(self, x, y):
        pass

    def mouseDrag(self, x, y):
        pass

    def mouseMotion(self, x, y):
        self.mouse = pygame.mouse.get_pos()
        if self.mode == "welcome":
            print("mouseX", x)
            print("mouseY", y)
            #from https://pythonprogramming.net/making-interactive-pygame-buttons/?completed=/pygame-buttons-part-1-button-rectangle/
            if self.width//2-(150//2) + 150 > x > self.width//2-(150//2) and self.height*(3/4) + 50 > y > self.height*(3/4):
                self.playButtonColor = (0,0,0)
            else:
                self.playButtonColor = (249,194,209)
        pass
    #def redrawAllWelcome(self, screen):
    #    pygame.draw.rect(screen, (0,0,0), (50,50,50,50))

    def keyPressed(self, keyCode, modifier):
        if self.mode == "welcome":
            print("key pressed")
            if keyCode == pygame.K_LEFT:
                print("LEFT")
                self.x -= 10
                #move left

            if keyCode == pygame.K_RIGHT:
                print("RIGHT")
                self.x += 10
                #move right

            #if keysDown(pygame.K_UP):
            #    pass
                #move up
            #if keysDown(pygame.K_DOWN):
            #    pass

    def redrawAll(self, screen):
        if self.mode == "welcome":
            #draw welcome text
            myfont = pygame.font.SysFont('Arial', 70)
            textsurface = myfont.render('Welcome to CatPy!', False, (0, 0, 0))
            text_rect = textsurface.get_rect(center=(self.width//2, self.height//4))
            screen.blit(textsurface, text_rect)
            #create button

            pygame.draw.rect(screen, self.playButtonColor, (self.width//2-(150//2),self.height*(3/4),150,50))
            textsurface = myfont.render('Play', False, (0, 0, 0))
            text_rect = textsurface.get_rect(center=(self.width//2, self.height*(3/4)+25))
            screen.blit(textsurface, text_rect)

        pass


    #WELCOME MODE



'''
Possible modes:
if self.mode ==

* "welcome"
* "backyard"
"groomsetup"
--> "groom"
"feedsetup"
--> "feed"
* "indoors"
"napsetup"
--> "nap"
"lasersetup"
--> "laser"

# "setup"
# "pond"
# "tree"
# "garden"
# "doghouse"
# "mouse"
# "settings"
# "aboutme"

'''



#creating and running the game
game = myProject()
game.run()
