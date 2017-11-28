import pygame
import pygamegame #the framework


#
class myProject(pygamegame.PygameGame):
    #class attribute

    def init(self):
        self.mode = "welcome"
        self.x = 50
        self.y = 50

        pass
    def mousePressed(self, x, y):
        pass

    #def redrawAllWelcome(self, screen):
    #    pygame.draw.rect(screen, (0,0,0), (50,50,50,50))

    def keyPressed(self, keyCode, modifier):
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
        if self.mode == "welcome": #redrawAllWelcome(self, screen)
            pygame.draw.rect(screen, (0,0,0), (self.x,self.y,50,50))
        pass


    #WELCOME MODE



#what is the syntax to draw???/

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


""

'''
#must create different modes within keyCode
'''
def mousePressed(event, data):
    if (data.mode == "welcome"): welcomeMousePressed(event, data)
    elif (data.mode == "playGame"):   playGameMousePressed(event, data)
    elif (data.mode == "help"):       helpMousePressed(event, data)

def keyPressed(event, data):
    if (data.mode == "splashScreen"): splashScreenKeyPressed(event, data)
    elif (data.mode == "playGame"):   playGameKeyPressed(event, data)
    elif (data.mode == "help"):       helpKeyPressed(event, data)

def timerFired(data):
    if (data.mode == "splashScreen"): splashScreenTimerFired(data)
    elif (data.mode == "playGame"):   playGameTimerFired(data)
    elif (data.mode == "help"):       helpTimerFired(data)

def redrawAll(canvas, data):
    if (data.mode == "splashScreen"): splashScreenRedrawAll(canvas, data)
    elif (data.mode == "playGame"):   playGameRedrawAll(canvas, data)
    elif (data.mode == "help"):       helpRedrawAll(canvas, data)
    '''



#creating and running the game
game = myProject()
game.run()
