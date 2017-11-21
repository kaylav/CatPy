import pygame
import pygamegame #the framework

class myProject(pygamegame.PygameGame):
    def init(self):
        self.mode = "welcome"
        self.message = "World Helo"
    def mousepressed(self, x, y):
        print("It's working!!!")
        print(self.message)

'''
Possible modes:
if self.mode ==

"welcome"
"setup"
"backyard"
"groomsetup"
"groom"
"feedsetup"
"feed"
"pond"
"tree"
"garden"
"doghouse"
"indoors"
"napsetup"
"nap"
"laser"
"mouse"
"settings"
"aboutme"


""

'''
#must create different modes within keyCode
'''
def mousePressed(event, data):
    if (data.mode == "splashScreen"): splashScreenMousePressed(event, data)
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
