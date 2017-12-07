##Kayla Vokt (kgv) 15-112 Section H 
# Barebones timer, mouse, and keyboard events from 15-112 course website 
from tkinter import *
import random

# Term Project! PyCat
#https://www.humaneanimalrescue.org/available-pets/
# for converting png to gif https://image.online-convert.com/convert-to-gif

#Helper Function from 15-112 Course 
def almostEqual(d1, d2, epsilon=10**-7):
    # note: use math.isclose() outside 15-112 with Python version 3.5 or later
    return (abs(d2 - d1) < epsilon)
    
####################################
# dispatches modes inspired by starter code on 112 website
####################################

def init(data):
    data.gameImages = dict()
    #mode variable, can be "welcome", "play" many others 
    data.mode = "welcome"
    #variables used in welcome mode 
    welcomeInit(data)
    loadImage(data, data.filename)
    #variables in backyard mode
    backyardInit(data)
    #food game variables
    feedInit(data)
    #brush game variables
    brushInit(data)
    #cat nap variables
    catNapInit(data)
    loadCat(data) # always load images in init!
    loadGif(data)
    
def welcomeInit(data):
    data.welcomeX = 10 
    data.welcomeY = data.height//3
    data.filename = "images/cat1.gif"
    #data.filename = "images/stars.gif"
    data.playButtonColor = rgbString(249,194,209)
    data.catIndex = 0
    data.cornerCat = False
    data.pawCount = 0
    data.squareSelect = 0
    data.prevScreen = "backyard"
   
def backyardInit(data):
    data.timer = 0
    data.age = 0
    data.happy = 100
    data.hungry = 100
    data.sleepy = 100
    data.catX = data.width//2
    data.catY = data.height//2
    data.catX2 = data.catX
    data.catY2 = data.catY
    data.timeAlive = 0
    data.collide = False
    data.playGame = ""
    data.catDX = 0
    data.catDY = 0
    data.moving = False 
    data.settings = False 
    data.catColor = "orange"
    data.catDir = "down"
    data.imageSettings = getImage(data, "images/settings1.gif")
    
    
def feedInit(data):
    data.feedCountdown = 15 
    data.feedTimer = 0
    data.bowlX = data.width//2
    data.bowlY  = data.height - 50 
    data.fishes = [] #y pos, y pos
    data.feedScore = 0
    data.feedFishTime = 0
    data.possibleFish = ["images/fish.gif","images/fish3.gif","images/fish2.gif"]
    data.fishSpeed = 20
    data.foodCount = 0
    
def brushInit(data):
    data.brushCountdown = 15
    data.brushTimer = 0
    data.brushX = data.width//2
    data.brushY = data.width//2
    data.brushScore = 0
    data.lickCount = 0
    
def catNapInit(data):
    data.napLives = 3
    data.napScore = 0
    data.sheepX = 225
    data.sheepY = 330
    data.napTimer = 0
    data.fences = []
    data.randomTimeNap = 0
    data.sheepDY = 0
    

def mousePressed(event, data):
    #redirects to proper mouse pressed function depending on mode 
    if (data.mode == "welcome"): 
        welcomeMousePressed(event, data)
    elif (data.mode == "settings"):       
        settingsMousePressed(event, data)
    elif (data.mode == "backyard"):   
        backyardMousePressed(event, data)
    elif (data.mode == "inside"):   
        insideMousePressed(event, data)
    elif (data.mode == "setupFeed"):       
        setupFeedMousePressed(event, data)
    elif (data.mode == "feedGame"):       
        feedGameMousePressed(event, data)
    elif (data.mode == "instructions"):
        instructionsMousePressed(event, data)
    elif (data.mode == "setupNap"):       
        setupNapMousePressed(event, data)
    elif (data.mode == "napGame"):       
        napGameMousePressed(event, data)
    elif (data.mode == "napGameOver"):       
        napGameOverMousePressed(event, data)
    elif (data.mode == "setupBrush"):       
        setupBrushMousePressed(event, data)
    elif (data.mode == "brushGame"):       
        brushGameMousePressed(event, data)
    elif (data.mode == "brushGameOver"):       
        brushGameOverMousePressed(event, data)

        
def mouseMoved(event, data):
    data.xPos = event.x
    data.yPos = event.y
    if (data.mode == "welcome"): 
        welcomeMouseMoved(event, data)
    elif (data.mode == "settings"): 
        settingsMouseMoved(event, data) # HERE 
    elif (data.mode == "brushGame"): 
        brushGameMouseMoved(event, data)
    elif (data.mode == "backyard" or data.mode == "inside"): 
        gamePlayMouseMoved(event, data)
    
def keyPressed(event, data):
    #direct to correct keypressed mode function
    if (data.mode == "welcome"): 
        welcomeKeyPressed(event, data)
    elif (data.mode == "backyard"):   
        backyardKeyPressed(event, data)
    elif (data.mode == "settings"):   
        settingsKeyPressed(event, data)
    elif (data.mode == "inside"):   
        insideKeyPressed(event, data)
    elif (data.mode == "setupFeed"):       
        setupFeedKeyPressed(event, data)
    elif (data.mode == "feedGame"):       
        feedGameKeyPressed(event, data)
    elif (data.mode == "instructions"):       
        instructionsKeyPressed(event, data)
    elif (data.mode == "setupNap"):       
        setupNapKeyPressed(event, data)
    elif (data.mode == "napGame"):       
        napGameKeyPressed(event, data)
    elif (data.mode == "napGameOver"):       
        napGameOverKeyPressed(event, data)
    elif (data.mode == "setupBrush"):       
        setupBrushKeyPressed(event, data)
    elif (data.mode == "brushGame"):       
        brushGameKeyPressed(event, data)
    elif (data.mode == "brushGameOver"):       
        brushGameOverKeyPressed(event, data)

def timerFired(data):
    #directed to correct keypressed timer fired
    if (data.mode == "welcome"): 
        welcomeTimerFired(data)
    elif (data.mode == "backyard" or data.mode == "inside"):    #INSIDE STUFF 
        gameModeTimerFired(data) #GAME MODE TIMER FIRED 
    elif (data.mode == "setupFeed"):       
        setupFeedTimerFired(data)
    elif (data.mode == "feedGame"):       
        feedGameTimerFired(data)
    elif (data.mode == "setupNap"):       
        setupNapTimerFired(data)
    elif (data.mode == "napGame"):       
        napGameTimerFired(data)
    elif (data.mode == "setupBrush"):       
        setupBrushTimerFired(data)
    elif (data.mode == "brushGame"):       
        brushGameTimerFired(data)
    
def redrawAll(canvas, data):
    #directed to proper redraw function
    if (data.mode == "welcome"): 
        welcomeRedrawAll(canvas, data)
    elif (data.mode == "settings"):   
        settingsRedrawAll(canvas, data)
    elif (data.mode == "backyard"):   
        backyardRedrawAll(canvas, data)
    elif (data.mode == "inside"):   
        insideRedrawAll(canvas, data)
    elif (data.mode == "setupFeed"):       
        setupFeedRedrawAll(canvas, data)
    elif (data.mode == "feedGame"):       
        feedGameRedrawAll(canvas, data)
    elif (data.mode == "instructions"):       
        instructionsRedrawAll(canvas, data)
    elif (data.mode == "setupNap"):       
        setupNapRedrawAll(canvas, data)
    elif (data.mode == "napGame"):       
        napGameRedrawAll(canvas, data)
    elif (data.mode == "setupBrush"):       
        setupBrushRedrawAll(canvas, data)
    elif (data.mode == "brushGame"):       
        brushGameRedrawAll(canvas, data)
        
                       
def loadCat(data):
    data.catImage = PhotoImage(file=data.filename)
    
def getCat(data):
    loadCat(data)
    return data.catImage
    
def getImage(data, filename):
    return data.gameImages[filename]
    
def loadImage(data, filename):
    data.gameImages = dict()
    #code to look through files and make set of all image names 
    filenames = {"images/tree.gif","images/food.gif","images/brush.gif","images/bed.gif", "images/fish.gif", "images/bowl.gif", "images/petcat.gif","images/fence.gif", "images/sheep.gif", "images/door.gif","images/fish3.gif","images/fish2.gif", "images/sprites/cats2-1.gif","images/sprites/cats2-2.gif","images/sprites/cats2-3.gif", "images/stars.gif", "images/cornercat.gif", "images/paws.gif", "images/pinkpaws.gif","images/settings.gif", "images/settings1.gif", "images/paw.gif","images/home.gif", "images/sprites/cats1-2.gif", "images/sprites/cats2-2.gif","images/sprites/cats3-2.gif","images/sprites/cats4-2.gif","images/sprites/cats1-4.gif","images/sprites/cats2-4.gif","images/sprites/cats3-4.gif","images/sprites/cats4-4.gif", "images/sprites/orange-down.gif", "images/sprites/orange-up.gif", "images/sprites/orange-left.gif", "images/sprites/orange-right.gif", "images/sprites/white-down.gif", "images/sprites/white-up.gif", "images/sprites/white-left.gif", "images/sprites/white-right.gif", "images/sprites/brown-down.gif", "images/sprites/brown-up.gif", "images/sprites/brown-left.gif", "images/sprites/brown-right.gif", "images/sprites/black-down.gif", "images/sprites/black-up.gif", "images/sprites/black-right.gif", "images/sprites/black-left.gif", "images/border.gif", "images/lick.gif", "images/sparkle.gif", "images/sushi.gif", "images/ramen.gif", "images/scales.gif","images/yawn.gif", "images/moon.gif", "images/doghouse.gif", "images/pond.gif", "images/byfence.gif", "images/byfence1.gif","images/succ.gif","images/window.gif", "images/chest.gif", "images/rug.gif"} #images labeled for reuse from google.com 
    
    for filename in filenames:
        data.gameImages[filename] = PhotoImage(file=filename)

    
def loadGif(data): #used to make gifs (http://gifmaker.org/) from photo (https://orig00.deviantart.net/3c24/f/2015/172/4/a/cat_sprites_by_biofunk95-d8y869y.png)
    data.pawGifDict = dict()
    for i in range(6):
        data.pawGifDict[i] = PhotoImage(file="images/paws.gif", format="gif -index "+str(i))
        
    data.starGif = dict()
    for i in range(19):
        data.starGif[i] = PhotoImage(file="images/stars.gif", format="gif -index "+str(i))
        
    data.pinkPawsGifDict = dict()
    for i in range(10):
        data.pinkPawsGifDict[i] = PhotoImage(file="images/pinkpaws.gif", format="gif -index "+str(i))
        
    data.lickGif = dict()
    for i in range(39):
        data.lickGif[i] = PhotoImage(file="images/lick.gif", format="gif -index "+str(i))
        
    data.sparkleGif = dict()
    for i in range(24):
        data.sparkleGif[i] = PhotoImage(file="images/sparkle.gif", format="gif -index "+str(i))
        
    data.sushiGif = dict()
    for i in range(4):
        data.sushiGif[i] = PhotoImage(file="images/sushi.gif", format="gif -index "+str(i))
    
    data.ramenGif = dict()
    for i in range(4):
        data.ramenGif[i] = PhotoImage(file="images/ramen.gif", format="gif -index "+str(i))
        
    data.yawnGif = dict()
    for i in range(58):
        data.yawnGif[i] = PhotoImage(file="images/yawn.gif", format="gif -index "+str(i))
        
    data.orangeLeft = dict()
    data.orangeRight = dict()
    data.blackLeft = dict()
    data.blackRight = dict()
    data.whiteLeft = dict()
    data.whiteRight = dict()
    data.brownLeft = dict()
    data.brownRight = dict()
    
    dictList = [["orange", data.orangeLeft, data.orangeRight],
                ["black", data.blackLeft, data.blackRight],
                ["white", data.whiteLeft, data.whiteRight],
                ["brown", data.brownLeft, data.brownRight]
                ]
    
    for color in range(len(dictList)):
        for i in range(4):
            dictList[color][1][i] = PhotoImage(file="images/sprites/" + dictList[color][0] + "-left.gif", format="gif -index "+str(i))
            dictList[color][2][i] = PhotoImage(file="images/sprites/" + dictList[color][0] + "-right.gif", format="gif -index "+str(i))
            

####################################
# ~~~~~~~~ welcome screen ~~~~~~~~~~~
####################################

def welcomeMousePressed(event, data):
    clickX = event.x
    clickY = event.y
    
    if data.width//2-(150//2)+150 > clickX and clickX > data.width//2-(150//2) \
    and data.height*(3/4)+50 > clickY \
    and clickY > data.height*(3/4):
        data.mode = "instructions"

def welcomeKeyPressed(event, data):
    pass 
    
def welcomeMouseMoved(event, data):
    if data.width//2-(150//2)+150 > data.xPos and data.xPos > data.width//2-(150//2) \
    and data.height*(3/4)+50 > data.yPos \
    and data.yPos > data.height*(3/4):
        data.playButtonColor = rgbString(161,66,68)
        data.cornerCat = True 
    else:
        data.playButtonColor = rgbString(249,194,209)
        data.cornerCat = False

def welcomeTimerFired(data):
    data.catIndex += 1        
        
    cat1 = "images/sprites/cats2-1.gif"
    cat2 = "images/sprites/cats2-2.gif"
    cat3 = "images/sprites/cats2-3.gif"
    
    catList = [cat1, cat2, cat3, cat2]

    data.filename = catList[data.catIndex%4]
    
    data.welcomeX -= 10
    if data.welcomeX < 0:
        data.welcomeX = data.width 

def rgbString(red, green, blue): #from 15-112 course website, colors from https://www.sessions.edu/color-calculator/
    return "#%02x%02x%02x" % (red, green, blue)

def welcomeRedrawAll(canvas, data):
    #draw welcome text and instructions
    blue = rgbString(206, 231, 242)
    canvas.create_rectangle(-50,-50,data.width+50, data.height+50, fill=blue)
    canvas.create_text(data.width/2, data.height//6, 
                       text="Welcome to PyCat!", 
                       font="Noteworthy 50 bold")
    canvas.create_rectangle(data.width//2-(150//2),data.height*(3/4),data.width//2-(150//2)+150,data.height*(3/4)+50, fill = data.playButtonColor)
    canvas.create_text(data.width//2,data.height*(3/4)+20, text="Play",font="Noteworthy 35 bold")
                       
    (left, top) = (data.welcomeX, data.welcomeY)
    
    if data.cornerCat:
        #corner cat image 
        cornerCat = getImage(data, "images/cornercat.gif")
        canvas.create_image(50, data.height-cornerCat.height()//2, image=cornerCat)
        
        #animated paws  and pink paws
        paws = data.pawGifDict[0]
        pinkpaws = data.pinkPawsGifDict[0]
        data.pawCount += 1 #.5
        #if data.pawCount == int(data.pawCount):
        paws =  data.pawGifDict[data.pawCount%5]
        pinkpaws =  data.pinkPawsGifDict[data.pawCount%10]
        canvas.create_image(pinkpaws.width()//2, 150, image=pinkpaws)
        canvas.create_image(data.width-75, data.height-100, image=paws)
        
    #draw walking cat     
    image = getCat(data)
    canvas.create_image(left, top, anchor=NW, image=image)
        
    
    
####################################
# ~~~~~~~~~~~settings~~~~~~~~~~~~~
####################################

def settingsMousePressed(event, data):
    #if mouse collide with any of the cat options
    #data.catImage = update, preload in list of image file names 
    #if you press the home buttom and return to the backyard 
    
    if event.x > 0 and event.x < 50 and event.y > 0 and event.y < 50:
        if data.prevScreen == "inside":
            data.mode = "inside"
        else:
            data.mode = "backyard"
    
    if event.x > -10 and event.x < data.width//2 and event.y > 50 and event.y < data.height//2+25:
        data.catColor = "black"
        if data.prevScreen == "inside":
            data.mode = "inside"
        else:
            data.mode = "backyard"
    
    #top right
    elif event.x > data.width//2 and event.x < data.width+10 and event.y > 50 and event.y < data.height//2+25:
        data.catColor = "orange"
        if data.prevScreen == "inside":
            data.mode = "inside"
        else:
            data.mode = "backyard"
    
    #bottom left
    elif event.x > -10 and event.x < data.width//2 and event.y > data.height//2+25 and event.x < data.height+10:
        data.catColor = "white"
        if data.prevScreen == "inside":
            data.mode = "inside"
        else:
            data.mode = "backyard"
    
    #bottom right
    elif event.x > data.width//2 and event.x < data.width+10 and event.y > data.height//2+25 and event.y < data.height+10:
        data.catColor = "brown"
        if data.prevScreen == "inside":
            data.mode = "inside"
        else: 
            data.mode = "backyard"

def settingsKeyPressed(event, data):
    pass

def settingsMouseMoved(event, data):
    #top left 
    if event.x > -10 and event.x < data.width//2 and event.y > 50 and event.y < data.height//2+25:
        data.squareSelect = 1
    
    #top right
    elif event.x > data.width//2 and event.x < data.width+10 and event.y > 50 and event.y < data.height//2+25:
        data.squareSelect = 2
    
    #bottom left
    elif event.x > -10 and event.x < data.width//2 and event.y > data.height//2+25 and event.x < data.height+10:
        data.squareSelect = 3
    
    #bottom right
    elif event.x > data.width//2 and event.x < data.width+10 and event.y > data.height//2+25 and event.y < data.height+10:
        data.squareSelect = 4 
    
    else:
        data.squareSelect = 0



def settingsRedrawAll(canvas, data):
    canvas.create_text(data.width//2, 20, 
                       text = "Select Your Kitten!", 
                       font="Noteworthy 30 bold")
                       
    #paw images
    paw = getImage(data, "images/paw.gif")
    canvas.create_image(5, 25, anchor = "w", image=paw)
    canvas.create_image(data.width//2+125, 25, anchor = "w", image=paw)
    
    canvas.create_rectangle(0,0,50,50, fill="white", width=0)
    home = getImage(data, "images/home.gif")
    canvas.create_image(0, 25, anchor = "w", image=home)
    
                       
                       
    #create grid of four rectangles 
    
    topLeftColor = rgbString(249,194,209) # light pink
    topRightColor = rgbString(159,231,144) #light green
    bottomLeftColor = rgbString(203,185,236) #light purple 
    bottomRightColor = rgbString(174,229,243) #light blue 
    
    cat1 = getImage(data, "images/sprites/cats1-2.gif")
    cat2 = getImage(data, "images/sprites/cats2-2.gif")
    cat3 = getImage(data, "images/sprites/cats3-2.gif")
    cat4 = getImage(data, "images/sprites/cats4-2.gif")
    
    
    
    check = data.squareSelect
    if check != 0:
        if check == 1:
            topLeftColor = rgbString(252,120,227) #darker pink
            cat1 = getImage(data, "images/sprites/cats1-4.gif")
        elif check == 2:
            topRightColor = "green"
            cat2 = getImage(data, "images/sprites/cats2-4.gif")
        elif check == 3:
            bottomLeftColor = "purple"
            cat3 = getImage(data, "images/sprites/cats3-4.gif")
        elif check == 4:
            bottomRightColor = "blue"
            cat4 = getImage(data, "images/sprites/cats4-4.gif")
        
    
    #top left 
    canvas.create_rectangle(-10, 50, data.width//2, data.height//2+25, fill =topLeftColor, width=0)
    canvas.create_image(150, 88+50, image=cat1)
    
    #top right
    canvas.create_rectangle(data.width//2, 50, data.width+10, data.height//2+25, fill =topRightColor,width=0)
    canvas.create_image(450, 88+50, image=cat2)
    
    #bottom left
    canvas.create_rectangle(-10, data.height//2+25, data.width//2, data.height+10, fill=bottomLeftColor,width=0)
    canvas.create_image(150, 263+50, image=cat3)
    #bottom right
    canvas.create_rectangle(data.width//2, data.height//2+25, data.width+10, data.height+10, fill =bottomRightColor,width=0)
    canvas.create_image(450, 263+50, image=cat4)
   
    

    
####################################
# ~~~~~~~~~ backyard game mode  ~~~~~~~~~~~~~~ 
####################################

def backyardMousePressed(event, data):
    if data.settings:
        data.prevScreen = "backyard"
        data.mode = "settings"
    
    mousePressMove(event, data)
    
    if imageCollide(data.imageCat, data.imageDoor, data.catX, data.catY, data.width, data.height//2): 
        data.collide = True
        data.playGame = "Go Inside"    
    
    
def gamePlayMouseMoved(event, data):
    settingsWidth = data.imageSettings.width()//2
    settingsHeight = data.imageSettings.height()//2
    
    if event.x > 110//2 - settingsWidth and event.x < 110//2 + settingsWidth and event.y > data.height-50 - settingsHeight and event.y < data.height-50 + settingsHeight:
         data.settings = True
    else:
        data.settings = False 
     
     
     
def collisionCheck(data):
    if data.mode == "backyard":
        #check for food collision
        if imageCollide(data.imageCat, data.imageFood, data.catX, data.catY, data.width-data.imageFood.width()//2, data.height-data.imageFood.height()//2):
            data.collide = True
            data.playGame = "Play Food Game"
        #check for brush collision
        elif imageCollide(data.imageCat, data.imageBrush, data.catX, data.catY, data.width//4+60, data.height-data.imageBrush.height()//2):
            data.collide = True
            data.playGame = "Play Brush Game"
        #door collision!!!
        elif imageCollide(data.imageCat, data.imageDoor, data.catX, data.catY, data.width, data.height//2): 
            data.collide = True
            data.playGame = "Go Inside"
        else:
            data.collide = False
            data.playGame = ""
    elif data.mode == "inside":
    
        #check for door collision
        if imageCollide(data.imageCat, data.imageDoor, data.catX, data.catY, 120, data.height//2):
            data.collide = True
            data.playGame = "Go to Backyard"
        #check for bed collision
        elif imageCollide(data.imageCat, data.imageBed, data.catX, data.catY, data.width//4+60, data.height-data.imageBed.height()//2//2): 
            data.collide = True
            data.playGame = "Play Cat Nap"
        else:
            data.collide = False
            data.playGame = ""
            
    
def backyardKeyPressed(event, data):
    
    # moveCatAroundKeys(event, data) cant move cat with keys
    collisionCheck(data)
    
    #SWITCH TO FOOD GAME 
    if data.playGame == "Play Food Game" and (event.keysym == "Enter" or event.keysym == "Return"):
        feedInit(data)
        data.mode = "setupFeed"    
        
    #SWITCH TO BRUSH GAME setup
    if data.playGame == "Play Brush Game" and (event.keysym == "Enter" or event.keysym == "Return"):
        brushInit(data)
        data.mode = "setupBrush"
            
    #MOVE TO INSIDE 
    if data.playGame == "Go Inside" and (event.keysym == "Enter" or event.keysym == "Return"):
        swapCatX(data) #swap where cat is on the screen!!! 
        data.mode = "inside"
    
def moveCatAroundKeys(event, data): #not used, only for testing 
    #move cat around backyard 
    if event.keysym == "Right" and data.catX < data.width-data.catImage.width()//2:
        data.catX += 20
        data.catX2 = data.catX
    elif event.keysym == "Left" and data.catX > data.catImage.width()//2:
        data.catX -= 20
        data.catX2 = data.catX
    elif event.keysym == "Up" and data.catY > data.catImage.height()//2:
        data.catY -= 20
        data.catY2 = data.catY
    elif event.keysym == "Down"and data.catY < data.height-data.catImage.height()//2:
        data.catY += 20
        data.catY2 = data.catY
        
        
def getSlope(data):
    dy = data.catY - data.catY2
    dx = data.catX2 - data.catX
    dir, dirX, dirY = None, 0, 0

    #determine direction
    data.catDir = "down"
    
    if dx > 0 and dy > 0 :
        dir, dirX, dirY = "NE", 1, 1 #(+,+)
        data.catDir = "right"
        return (5*dirX,5*dirY)
        
    elif dx < 0 and dy < 0:
        dir, dirX, dirY = "SW", -1, -1 #(-,-)
        data.catDir = "left"
        return (5*dirX,5*dirY)
        
    elif dx > 0 and dy < 0:
        dir, dirX, dirY = "SE", 1, -1 #(+,-)
        data.catDir = "right"
        return (5*dirX,5*dirY)
       
    elif dx < 0 and dy > 0:
        dir, dirX, dirY = "NW", -1, 1 #(-,+)
        data.catDir = "left"
        return (5*dirX,5*dirY)
       
    elif dx > 0 and dy == 0:
        dir, dirX, dirY = "E", 1, 0 #(+,0)
        data.catDir = "right"
        return (5*dirX,5*dirY)
       
    elif dx < 0 and dy == 0:
        dir, dirX, dirY = "W", -1, 0 #(-,0)
        data.catDir = "left"
        return (5*dirX,5*dirY)
       
    elif dx == 0 and dy > 0:
        dir, dirX, dirY = "N", 0, 1 #(0,+)
        data.catDir = "up"
        return (5*dirX,5*dirY)
       
    elif dx == 0 and dy < 0:
        dir, dirX, dirY = "S", 0, -1 #(0,-)
        data.catDir = "down"
        return (5*dirX,5*dirY)
    else:
        data.catDir = "up"
        #print("no movement!!!")
        return (0,0)
    
    return (5*dirX,5*dirY)
    
def hungrySleepy(data):
    hunger = data.hungry
    sleepy = data.sleepy 
    newX, newY = None, None
    hunger *= .35 #has a greater influence on decision
    sleepy *= .65
    if hunger > 90 and sleepy > 90:
        #if not hungry or sleepy cat can move anywhere on the screen 
        return "either" # , newX, newY
    elif hunger > sleepy:
        return "sleepy"
    else: return "hungry"
    
    
def catAI(data):
    #if NOT in the process of mouse pressed 
    #assign new X2, Y2 location for cat to move 
    priority = hungrySleepy(data)
        
    if priority == "either":
        data.catX2 = random.randint(110, data.width-10)
        data.catY2 = random.randint(110, data.height-10)
    elif priority == "hungry":
        radX, radY = oppLevelDiam(data, data.hungry)
        newX, newY = findDestWithinBounds(data.width-data.imageFood.width()//2, data.height-data.imageFood.height()//2, radX, radY)
        data.catX2, data.catY2 = newX, newY
        if data.hungry < 50 and data.mode != "backyard":
            data.mode = "backyard"
    elif priority == "sleepy":
        radX, radY = oppLevelDiam(data, data.sleepy)
        newX, newY = findDestWithinBounds(data.imageBed.width()//2, data.height-data.imageBed.height()//2 , radX, radY)
        data.catX2, data.catY2 = newX, newY
        if data.sleepy < 50 and data.mode != "inside":
            data.mode = "inside"        
        
    
def levelDiameter(data, level):
    #this is for HAPPY level
    if level > 90:
        return 0
    elif level > 75:
        return 100
    elif level > 50:
        return 200
    elif level > 25:
        return 300
    elif level > 15:
        return 400 #move in opposite direction
    elif level >= 0:
        data.catDir = "up"
        return 600 #shake left and right wont listen to player 
    else: return 0 
    
    
def oppLevelDiam(data, level):
    #for hungry and sleepy level 
    if level > 90:
        return data.width//2, 0 # x, y 
    elif level > 75:
        return (data.width - 100)//2, 100
    elif level > 50:
        return (data.width - 200)//2, 150
    elif level > 25:
        return (data.width - 300)//2, 200
    elif level > 15:
        return (data.width - 400)//2, 250
    elif level >= 0:
        return (data.width - 500)//2, 300 
    else:
        return 0, 0
        
def findDestWithinBounds(cx, cy, radX, radY):
    return random.randint(cx-radX,cx+radX), random.randint(radY,400) 
    
    
def constantCatMove(data): # put in TIMER FIRED 
    # HERE update direction???
    data.moving = False
    if abs(data.catX-data.catX2) > 10:
        data.moving = True
        data.catX += data.catDX
    if abs(data.catY - data.catY2) > 10:
        data.moving = True
        data.catY -= data.catDY
     
    
def mousePressMove(event, data):
    #function for when it reaches its location??     
    radius = levelDiameter(data, data.happy)//2
    x2 = event.x 
    y2 = event.y
    
    if radius == 0:
        data.catX2 = x2
        data.catY2 = y2
    elif radius < 200:
        data.catX2 = random.randint(x2-radius, x2+radius)
        data.catY2 = random.randint(x2-radius, x2+radius)
    elif radius == 200: #move in opposite direction
        #print("opposite")
        data.catX2 = abs(data.width - x2)
        data.catY2 = abs(data.height - y2)
    elif radius == 250: #shake left and right wont listen to player
        #animate
        data.catDir = "up"
        print("unhappy, wont move, no!")
        
    #make sure it doesnt go off screen 
    if data.catX2 > data.width:
        data.catX2 = data.width
        data.catDX = 0
        if data.catDY > 0:
            data.catDir = "up"
        elif data.catDY < 0:
            data.catDir = "down"
    if data.catX2 < 110:
        data.catDX = 0
        data.catX2 = 0
        if data.catDY > 0:
            data.catDir = "up"
        elif data.catDY < 0:
            data.catDir = "down"
    if data.catY2 > data.height:
        data.catY2 = data.height
        data.catDY = 0
    if data.catY2 < 0:
        data.catDY = 0
        data.catY2 = 0
        
    #update direction
    if data.catDY == 0 and data.catDY != 0:
        if data.catDY > 0:
            data.catDir = "up"
        else:
            data.carDir = "down"
       
def doneMoving(data):
    data.catDir = "down"
    return (abs(data.catX-data.catX2)<10 and abs(data.catY-data.catY2)<10)
    
    
def gameModeTimerFired(data):
    #continually MOVE CAT AI 
    collisionCheck(data)
    #levels can go over    
    if data.hungry > 100:
        data.hungry = 100
   
    if data.sleepy > 100:
        data.sleepy = 100
    
    if data.happy > 100:
        data.happy = 100
   
        
    data.timer += 1
    time = data.timer//10
    data.age = time // 15
    
    if time % 15 == random.randint(5,15) and data.happy > 0:
        
        data.happy -= 1
    if time % 15 == random.randint(5,15) and data.sleepy > 0:
        
        data.sleepy -= 1
    if time % 15 == random.randint(5,15) and data.hungry > 0:
        
        data.hungry -= 1
        
    data.catDX, data.catDY = getSlope(data)
    
    #if no longer moving, reset DY and DX 
    if data.moving == False:
        data.catDir = "down"
        data.catDX, data.catDY = 0,0 
        
    if data.timer % 5 == 0 and data.catDX == 0 and data.catDY == 0 :
        catAI(data)
        
    if data.catX < 120:
        data.catX = 120
        data.catDX = 0
        
    if data.catX2 < 120:
        data.catX2 = 120
    
    
    constantCatMove(data)
    
 

def backyardRedrawAll(canvas, data):
        
    data.filename = "images/sprites/" + data.catColor+ "-" + data.catDir +".gif"#"images/cathead.gif"
    data.imageCat = getImage(data, data.filename)
    green = rgbString(126,193,100)
    
    canvas.create_rectangle(110, 0, data.width+10, data.height+10, fill=green)
    #canvas.create_rectangle(150,50,data.width-50, data.height-50, fill=rgbString(0,198,62))

    #tree image 
    data.imageTree = getImage(data, "images/tree.gif")
    canvas.create_image(data.width//2+60, data.height//2 , image=data.imageTree)
    
    #doghouse image 
    doghouse = getImage(data, "images/doghouse.gif")
    canvas.create_image(data.width//4+60, 75, image=doghouse)
    
    #pond image 
    pond = getImage(data, "images/pond.gif")
    canvas.create_image(data.width*(3/4)+60, 75, image=pond)
    
    #food image 
    data.imageFood = getImage(data, "images/food.gif")
    canvas.create_image(data.width-data.imageFood.width()//2, data.height-data.imageFood.height()//2, image=data.imageFood)
    
    #brush image 
    data.imageBrush = getImage(data, "images/brush.gif")
    canvas.create_image(data.width//4+60, data.height-data.imageBrush.height()//2, image=data.imageBrush)
    
    #door image 
    data.imageDoor = getImage(data, "images/door.gif")
    canvas.create_image(data.width, data.height//2, image=data.imageDoor)

    
    printLevels(canvas, data)
    
    
def printLevels(canvas, data):
    #print out scores and timer at top left 
    purple = rgbString(140,138,247)
    canvas.create_rectangle(0,0,120, data.height+10, fill=purple, width=0)
    
    canvas.create_text(10, 10, 
                       text = "Time: "+str(int(data.timer//10)), 
                       font="Noteworthy 20 bold", anchor="nw")
    canvas.create_text(10, 35, 
                       text = "Age: "+str(int(data.age)), 
                       font="Noteworthy 20 bold", anchor="nw")
                       
    canvas.create_text(10, 65, #data.height 
                       text = "Happy: "+str(int(data.happy))+"%", 
                       font="Noteworthy 15 bold", anchor="nw")
                       
    yellow = rgbString(255,250,161)
    canvas.create_rectangle(10, 90, 10 + data.happy, 105, fill = yellow, width=0)
    canvas.create_rectangle(10, 90, 110, 105, fill = None)
            
    canvas.create_text(10, 110, 
                       text = "Sleepy: "+str(data.sleepy)+"%", 
                       font="Noteworthy 15 bold", anchor="nw")
                       
    green = rgbString(159,231,144)
    canvas.create_rectangle(10, 135, 10 + data.sleepy, 150, fill = green, width = 0)
    canvas.create_rectangle(10, 135, 110, 150, fill = None)
                       
    canvas.create_text(10, 160, 
                       text = "Hungry: "+str(data.hungry)+"%", 
                       font="Noteworthy 15 bold", anchor="nw")
                       
    canvas.create_rectangle(10, 185, 10 + data.hungry, 200, fill = "pink", width=0)
    canvas.create_rectangle(10, 185, 110, 200, fill = None)
                       
    #data.gamePlayTime += 1  
    #cat = getImage(data, data.filename)                 
    if data.catDir == "left" or data.catDir == "right": 
        if data.catColor == "orange":
            if data.catDir == "left": # HERE 
                data.imageCat =  data.orangeLeft[data.timer%4]
                # call left orange dict 
            else:
                #call right orange dict
                data.imageCat = data.orangeRight[data.timer%4]
        elif data.catColor == "black":
            if data.catDir == "left":  
                data.imageCat =  data.blackLeft[data.timer%4]
            else:
                data.imageCat = data.blackRight[data.timer%4]
        elif data.catColor == "white":
            if data.catDir == "left":  
                data.imageCat =  data.whiteLeft[data.timer%4]
            else:
                data.imageCat = data.whiteRight[data.timer%4]
        elif data.catColor == "brown":
            if data.catDir == "left":  
                data.imageCat =  data.brownLeft[data.timer%4]
            else:
                data.imageCat = data.brownRight[data.timer%4]
        
        #draw gifs !!!!
    
    else:
        
        #draw cat image 
        data.imageCat = getCat(data)
    
    #data.imageCat = getImage(data, cat)
    if data.catX < 120:
        data.catX = 120
        data.catDX = 0
        
    if data.catX2 < 120:
        data.catX2 = 120
    
    
    canvas.create_image(data.catX, data.catY, image=data.imageCat)
    
    #settings image 
    
    if data.settings:
        data.imageSettings = getImage(data, "images/settings1.gif")
        canvas.create_image(110//2, data.height-50, image=data.imageSettings)
        
    else: 
        data.imageSettings = getImage(data, "images/settings.gif")
        canvas.create_image(110//2, data.height-50, image=data.imageSettings)
                       
    if data.collide:
        canvas.create_text(data.width, 5, text="Press Enter to %s" % data.playGame, anchor=NE, fill="white")

    
def imageCollide(image1, image2, x1, y1, x2, y2): #from 15-112 Lab 1
    w1 = image1.width()
    w2 = image2.width() 
    h1 = image1.height()
    h2 = image2.height()
    
    return abs(x2 - x1) < w1//2+ w2//2 and abs(y2 - y1) < h1//2 + h2//2

#distance formula to find distance between 
#mouse pressed and center of each target
def distance(x1, y1, x2, y2):
    return ((x2 - x1)**2 + (y2 - y1)**2)**(1/2)
            


####################################
# inside 
####################################


def insideMousePressed(event, data):
    if data.settings:
        data.mode = "settings"
        data.prevScreen = "inside"
    mousePressMove(event, data)
    pass

def insideKeyPressed(event, data):
    #moveCatAroundKeys(event, data)
        
        
    if data.playGame == "Go to Backyard" and (event.keysym == "Enter" or event.keysym == "Return"):
        swapCatX(data) #swap where cat is on the screen!!! 
        data.mode = "backyard"
    #SWITCH TO NAP GAME setup
    elif data.playGame == "Play Cat Nap" and (event.keysym == "Enter" or event.keysym == "Return"):
        catNapInit(data)
        data.mode = "setupNap" 
        
        
def swapCatX(data):
    data.catX = abs(data.width - data.catX)
    
    if data.mode == "inside":
        data.catX += 60
        
    #data.catX2 = data.catX


def insideRedrawAll(canvas, data): 

    rose = rgbString(234,195,212)
    canvas.create_rectangle(-10, -10, data.width+10, data.height+10, fill=rose)
   
   
    #window image 
    window = getImage(data, "images/window.gif")
    canvas.create_image(data.width-50, data.height//4-10, image=window)
    
    #succulent image 
    succ = getImage(data, "images/succ.gif")
    canvas.create_image(data.width//2+150+75, data.height-50, image=succ)
    
    #rug image 
    rug = getImage(data, "images/rug.gif")
    canvas.create_image(data.width//2+60, data.height//2, image=rug)
    
    #chest image 
    chest = getImage(data, "images/chest.gif")
    canvas.create_image(data.width//4+60, 80, image=chest)
    
    #bed image 
    data.imageBed = getImage(data, "images/bed.gif")
    canvas.create_image(data.width//4+60, data.height-data.imageBed.height()//2 , image=data.imageBed)
    
    #draw door on left middle 
    canvas.create_image(120, data.height//2, image=data.imageDoor)
        
    printLevels(canvas, data)
    pass



####################################
# ~~~~~~~~~~~ set up feed ~~~~~~~~~~~~~~~
####################################

def setupFeedMousePressed(event, data):
    pass

def setupFeedKeyPressed(event, data):
    if event.keysym == "Return":
        data.mode = "feedGame"
    

def setupFeedTimerFired(data):
    pass

def setupFeedRedrawAll(canvas, data):
    canvas.create_rectangle(0,0, data.width+10, data.height+10, fill="lightblue")
    
    sushi = data.sushiGif[0]
    ramen = data.ramenGif[0]
    
    data.foodCount += 1 
    
    sushi =  data.sushiGif[data.foodCount%4]  
    ramen =  data.ramenGif[data.foodCount%4]  
      
    canvas.create_image(data.width//4, data.height-75, image=sushi)
    canvas.create_image(data.width*(3/4), data.height-75, image=ramen)
    
    
    canvas.create_text(data.width//2, data.height//2, text= "    Welcome to the feeding game! \n Try to catch as many fish as you can! \n           Press ~Enter~ to Begin",font="Noteworthy 20")
     

    
    pass 
    
####################################
# feed game
####################################

def feedGameMousePressed(event, data):
    pass

def feedGameKeyPressed(event, data):
    
    if event.keysym == "Right" and data.bowlX < data.width-(data.imageBowl.width()//4):
        data.bowlX += 40
    elif event.keysym == "Left" and data.bowlX > 120+(data.imageBowl.width()//4):
        data.bowlX -= 40
    
    #move left and right with keys 
    #if fish reaches bottom, remove from list


def feedGameTimerFired(data):
    data.feedTimer += 1
    if data.feedTimer % 10 == 0:
        data.feedCountdown -= 1 
        
    if data.feedTimer % 15 == data.feedFishTime:
        createNewFish(data)
        data.feedFishTime = random.randint(10,14)
        print("fish feed time", data.feedFishTime)
        
        
    if data.feedCountdown < 1: 
        data.hungry += data.feedScore
        data.mode = "backyard"
        
    #fish falling every second 
    for i in range(len(data.fishes)):
        data.fishes[i][1] += data.fishSpeed 
        
    #if time runs out and score > 10, data.hungry = 10 
    #def imageCollide(image1, image2, x1, y1, x2, y2) 
        if imageCollide(data.imageBowl, getImage(data, data.possibleFish[data.fishes[i][2]]), data.bowlX, data.bowlY, data.fishes[i][0], data.fishes[i][1]):
            #remove it, add to score
            
            
            # update score depending on size of fish 
            if data.fishes[i][2] == 0:
                data.feedScore += 3
            elif data.fishes[i][2] == 1:
                data.feedScore += 2
            else:
                data.feedScore += 1
            
            data.fishes.remove(data.fishes[i])
            
            break # in order to avoid index out of range error
       

def feedGameRedrawAll(canvas, data):
    
    #scales background 
    scales = getImage(data, "images/scales.gif")
    canvas.create_image(data.width//2, data.height//2, image=scales)
                       
    data.imageBowl = getImage(data, "images/bowl.gif")
    canvas.create_image(data.bowlX, data.bowlY, image=data.imageBowl)
    drawFishes(canvas, data)
    
    canvas.create_rectangle(0,0,120, data.height+10, fill="lightblue", width=0)
    
    canvas.create_text(data.width, 10, 
                       text = "Use arrow keys to move bowl!", 
                       font="Noteworthy 15 bold", anchor="ne")
                       
    canvas.create_text(10, 10, 
                       text = "Timer: "+str(data.feedCountdown), 
                       font="Noteworthy 20 bold", anchor="nw")
                       
    canvas.create_text(10, 35, 
                       text ="Score: %s" % str(data.feedScore), 
                       font="Noteworthy 20 bold", anchor="nw")
    
    

def drawFish(canvas, data, x , y, index): #from lab6 HW 
    imageFish = getImage(data, data.possibleFish[index])
    canvas.create_image(x, y, image=imageFish)
    
def createNewFish(data):

    fishX = random.randint(120,data.width-100)
    fishY = 0
    
    index = random.randint(1,2)
    
    # 2D list stores data as [fishX, fishY] 
    data.fishes.append([fishX, fishY, index])

#print out all fish in list 
def drawFishes(canvas, data):
    for i in range(len(data.fishes)):
        #index 0 is x coord, index 1 is y coord
        #draws fish with correct design 
        drawFish(canvas, data, data.fishes[i][0],
                data.fishes[i][1], data.fishes[i][2])
                
####################################
# INSTRUCTIONS!! 
####################################

def instructionsMousePressed(event, data):
    data.mode = "backyard"
    pass

def instructionsKeyPressed(event, data):
    pass

def instructionsTimerFired(data):
    pass

def instructionsRedrawAll(canvas, data):
    yellow = rgbString(255,250,161)
    canvas.create_rectangle(-10, -10, data.width+10, data.height+10, fill=yellow)
    
    border = getImage(data, "images/border.gif")
    canvas.create_image(data.width//2, data.height//2, image=border)
    
    
    canvas.create_text(data.width//2, data.height//2, text="Welcome to PyCat! An interactive pet care game. \n Your playful kitten has a mind of its own. It will \n explore the backyard and indoors on its own. As \n the player, you can click on the screen and tell the \n kitten where to move, but it will only listen depending \n on its happiness level. Play the minigames to keep your \n kitten happy, healthy, and alert! \n \n \t Click anywhere to begin!", font="Noteworthy 20")
    pass
    
    

    
####################################
# ~~~~~~~~~~~~~~~ setup brush ~~~~~~~~~~~~~~~
####################################

def setupBrushMousePressed(event, data):
    pass

def setupBrushKeyPressed(event, data):
    if event.keysym == "Return":
        data.mode = "brushGame"

def setupBrushTimerFired(data):
    pass

def setupBrushRedrawAll(canvas, data):
    lick = data.lickGif[0]
    canvas.create_rectangle(0,0, data.width+10, data.height+10, fill="lightgreen")
    
    data.lickCount += 1 
    lick =  data.lickGif[data.lickCount%39]    
    canvas.create_image(data.width-75, data.height-100, image=lick)
        
    canvas.create_text(data.width//2, data.height//2, text="Welcome to the Grooming Game! \n Sooth your cat by brushing its fur \n      Press ~Enter~ to Begin" , font="Noteworthy 20")
    
 
    
####################################
# brushGame
####################################

def brushGameMousePressed(event, data):
    data.brushScore += 0.5 
    pass

def brushGameKeyPressed(event, data):
    pass
  
def brushGameMouseMoved(event, data):
    data.brushX = event.x
    data.brushY = event.y
    #follow mouse with brush, if collides: increase score by .1, show data.happy
    pass
    
def brushGameTimerFired(data):
    data.brushTimer += 1
    if data.brushTimer % 10 == 0:
        data.brushCountdown -= 1 
        
    #colliding!!
    if imageCollide(data.imageBrush,data.imagePetCat, data.brushX, data.brushY, data.width//2, data.height//2): 
        data.brushScore += .1
        data.collide = True
    else:
        data.collide = False
        
    if data.brushCountdown < 1: 
        data.happy += data.brushScore
        data.mode = "backyard"
    

def brushGameRedrawAll(canvas, data):
                       
                       
    data.imagePetCat = getImage(data, "images/petcat.gif")
    brown = rgbString(210,167,140)
    tableHeight = (data.height//2 + data.imagePetCat.height()//2)-35
    canvas.create_rectangle(0, tableHeight, data.width+10, data.height, fill =brown, width=0)
    
    canvas.create_rectangle(0,0,120, data.height+10, fill="lightgreen", width=0)
    
    canvas.create_text(data.width, 10, 
                       text = "Brush the cat for points!", 
                       font="Noteworthy 15 bold", anchor="ne")
                       
    canvas.create_text(10, 10, 
                       text = "Timer: "+str(data.brushCountdown), 
                       font="Noteworthy 20 bold", anchor="nw")
    canvas.create_text(10, 35, 
                       text ="Score: %.1f" % (data.brushScore), 
                       font="Noteworthy 20 bold", anchor="nw")
    canvas.create_text(10, 350, 
                       text ="Click for Extra Points!", 
                       font="Noteworthy 10 bold", anchor="nw")

    
    canvas.create_image(data.width//2+60, data.height//2, image=data.imagePetCat)
    
    canvas.create_image(data.brushX, data.brushY, image=data.imageBrush)
    sparkle = data.lickGif[0]
    
    if data.collide:       
        sparkle =  data.sparkleGif[data.brushTimer%24]    
        canvas.create_image(data.width//2+60, 0, anchor="n", image=sparkle)
        
    
    
    #draw a giant cat in the center of screen
    
    pass 
    
####################################
# brushGameOver  not used 
####################################

def brushGameOverMousePressed(event, data):
    pass

def brushGameOverKeyPressed(event, data):
    pass

def brushGameOverTimerFired(data):
    pass

def brushGameOverRedrawAll(canvas, data):
    pass 
    
    

####################################
# ~~~~~~~~~~~~~~~ setupNap ~~~~~~~~~~~~~~~
####################################

def setupNapMousePressed(event, data):
    pass

def setupNapKeyPressed(event, data):
    if event.keysym == "Return":
        data.mode = "napGame"
  
def setupNapTimerFired(data):
    pass

def setupNapRedrawAll(canvas, data):
    
    indigo = rgbString(99,98,158)
    canvas.create_rectangle(-10,-10,data.width+10, data.height+10, fill=indigo)
    
    yawn = data.yawnGif[0]
    
    moon = getImage(data, "images/moon.gif")
    canvas.create_image(25, 55, image=moon)
    
    data.foodCount += 1 
    yawn =  data.yawnGif[data.foodCount%58] 
    
    canvas.create_image(data.width*(3/4), data.height-100, image=yawn) 
    
    
    canvas.create_text(data.width//2, data.height//2, text= "      Welcome to the Cat Nap Game! \n As your cat dreams, jump over the fences \n to get points! Press ~Enter~ to Begin",fill = "white", font="Noteworthy 20")
    
     
    
    
####################################
# napGame still to do nap score and random time intervals 
####################################

def napGameMousePressed(event, data):
    pass

def napGameKeyPressed(event, data):
    #use use and down arrows to avoid fences 
    if event.keysym == "Up" and data.sheepY > 100:
        data.sheepY -= 20
    elif event.keysym == "Down" and data.sheepY < data.height-100:
        data.sheepY += 20
        
    elif event.keysym == "space" and data.sheepDY == 0 or data.sheepDY <= -15 :
        print("pressed jump")
        sheepJump(data)
        
    #eventually space bar is jump 
    pass
  
def napGameTimerFired(data):
    data.napTimer += 1
    
    if data.napTimer % 50 == data.randomTimeNap:
        createNewFence(data)
        data.randomTimeNap = random.randint(35,49)
        #print("randomTimeNap= ", data.randomTimeNap)
        #update random number % 50 at least every 50 seconds 
        
    #remove negative fences and add points
    for i in range(len(data.fences)):
        if data.fences[i][0] < 0:
            data.fences.remove(data.fences[i])
            data.napScore += 1
            break
        
    #continually move fences 
    for i in range(len(data.fences)):
        data.fences[i][0] -= 15
                                    
        
        if imageCollide(data.imageSheep, getImage(data, "images/fence.gif"), data.sheepX, data.sheepY, data.fences[i][0], data.fences[i][1]):
            #remove it, reduce lives star again
            data.fences = [] 
            data.sheepY = 330
            data.napLives -= 1
            break 
             # SHEEP HERE  
             
            #data.sheepY = data.height-50
            
            
    if data.napLives == 0:
        data.mode = "inside"
        data.sleepy += data.napScore #data.napScore 
        
    #jumping !!! 
    if data.sheepDY != 0 or data.sheepY < 330:
        
        if data.sheepY > 330:
            data.sheepY = 330
            data.sheepDY = 0
        else:
            data.sheepY -= data.sheepDY
            data.sheepDY -= 2
        
    
    #position continually moves forward 
    #if collision, stop game, give 3 lives 
    #if fences are removed from list, add to data.sleep score 
    

def napGameRedrawAll(canvas, data):
    
    indigo = rgbString(99,98,158)
    bgIndigo = rgbString(108,158,217)
    
    stars = data.starGif[0]
    
    stars =  data.starGif[data.napTimer%19] #STARS HERE   
    
      
    canvas.create_rectangle(-10,-10,data.width+10, data.height+10, fill=bgIndigo)
    
    canvas.create_image(data.width//2, data.height//2, image=stars)
    
   
    
    drawFences(canvas, data)
    #sky background, need sheep and repeating fence images 
    
    
    #put in little yellow stars!!
    data.imageSheep = getImage(data, "images/sheep.gif")
    canvas.create_image(data.sheepX, data.sheepY, image=data.imageSheep)
    
    canvas.create_rectangle(0,0,120, data.height+10, fill=indigo, width=0)
    
    canvas.create_text(data.width, 10, 
                       text = "Jump Over the Fences for Points", 
                       font="Noteworthy 15 bold", fill = "white", anchor="ne")
                       
    canvas.create_text(10, 10, 
                       text = "Lives Left: "+str(data.napLives), 
                       font="Noteworthy 20 bold", anchor="nw")
    canvas.create_text(10, 35, 
                       text ="Score: " + str(data.napScore), 
                       font="Noteworthy 20 bold", anchor="nw")
     
    
def drawFence(canvas, data, x , y):
    imageFence = getImage(data, "images/fence.gif")
    canvas.create_image(x, y, image=imageFence)
    
def createNewFence(data):

    fenceX = data.width
    fenceY = data.height-25
  
    # 2D list stores data as [fishX, fishY] 
    data.fences.append([fenceX, fenceY])

#print out all fish in list 
def drawFences(canvas, data):
    for i in range(len(data.fences)):
        #index 0 is x coord, index 1 is y coord
        #draws fish with correct design 
        drawFence(canvas, data, data.fences[i][0],
                data.fences[i][1])
    
def sheepJump(data):
    data.sheepY = 280
    data.sheepDY = 20
    #sheepVelocity = 5 positive value 
    #update velocity/position in timer fired 
    
####################################
# napGameOver  not used ??
####################################

def napGameOverMousePressed(event, data):
    pass

def napGameOverKeyPressed(event, data):
    pass

def napGameOverTimerFired(data):
    pass

def napGameOverRedrawAll(canvas, data):
    pass


####################################
# use the run function as-is
####################################

def run(width=300, height=300):
    def redrawAllWrapper(canvas, data):
        canvas.delete(ALL)
        canvas.create_rectangle(0, 0, data.width, data.height,
                                fill='white', width=0)
        redrawAll(canvas, data)
        canvas.update()    

    def mousePressedWrapper(event, canvas, data):
        mousePressed(event, data)
        redrawAllWrapper(canvas, data)
        
    def mouseMovedWrapper(event, canvas, data): #mouse moved functionality from https://stackoverflow.com/questions/22925599/mouse-position-python-tkinter
        mouseMoved(event, data)
        

    def keyPressedWrapper(event, canvas, data):
        keyPressed(event, data)
        redrawAllWrapper(canvas, data)

    def timerFiredWrapper(canvas, data):
        timerFired(data)
        redrawAllWrapper(canvas, data)
        # pause, then call timerFired again
        canvas.after(data.timerDelay, timerFiredWrapper, canvas, data)
        
    
    root = Tk()
    # Set up data and call init
    class Struct(object): pass
    data = Struct()
    data.width = width
    data.height = height
    data.timerDelay = 100 # milliseconds
    init(data)
    # create the root and the canvas
    
    canvas = Canvas(root, width=data.width, height=data.height)
    canvas.pack()
    # set up events
    root.bind("<Button-1>", lambda event:
                            mousePressedWrapper(event, canvas, data))
    root.bind("<Key>", lambda event:
                            keyPressedWrapper(event, canvas, data))
    root.bind("<Motion>", lambda event: mouseMovedWrapper(event, canvas, data))
    timerFiredWrapper(canvas, data)
    # and launch the app
    root.mainloop()  # blocks until window is closed
    print("bye!")


# test functions:
def testDistance():
    print("Testing distance()...", end="")
    assert(distance(8, 8, -8, 8) == 16)
    assert(distance(0, 0, 5, 0) == 5)
    assert(distance(1, 2, 5, 5) == 5)
    assert(distance(4, 5, 7, 9) == 5)
    assert(distance(8, 8, 0, 2) == 10)
    print("Passed!")

def testisInsideTarget():
    pass
 
    
#cant test functions with random.randint 


##Call Test Functions    
def testAll():
   pass

def main():
    run(600, 400)
    #testAll()
   
    
if __name__ == '__main__':
    main()

