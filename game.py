##Kayla Votkt (kgv) 15-112 Section H 
# events-example0.py
# Barebones timer, mouse, and keyboard events from 15-112 course website 
from tkinter import *
import random

# Term Project! PyCat

#complexity games affect levels 
#cat AI how to move around? 
#decision tree based on certain factors 
#happiness is percentage chance it listens to the player 
#lots of probability, so that it feels more real, you don't know what its going to do 
#what can the cat
#update cat location 

####################################
# dispatches modes inspired by starter code on 112 website
####################################

def init(data):
    #mode variable, can be "welcome", "play" many others 
    data.mode = "welcome"
    
    #variables used in welcome mode 
    data.welcomeX = 10 
    data.welcomeY = data.height//3
    data.filename = "cat1.gif"
    data.playButtonColor = rgbString(249,194,209)
   
    #variables in backyard mode
    data.timer = 0
    data.happy = 10
    data.hungry = 10
    data.sleepy = 10
    data.catX = data.width//2
    data.catY = data.height//2
    data.timeAlive = 0
    data.collide = False
    data.playGame = ""
    
    #food game variables
    data.feedCountdown = 10 
    data.feedTimer = 0
    data.bowlX = data.width//2
    data.bowlY  = data.height - 100 
    data.fishes = [] #y pos, y pos
    data.feedScore = 0
    
    #brush game variables
    data.brushCountdown = 10
    data.brushTimer = 0
    data.brushX = data.width//2
    data.brushY = data.width//2
    data.brushScore = 0
    
    #cat nap variables
    data.napLives = 3
    data.sheepX = data.width//4
    data.sheepY = data.height-100
    data.napTimer = 0
    data.fences = []
    data.randomTimeNap = 0
    
    loadCat(data) # always load images in init!
    loadImage(data, data.filename)
    

def mousePressed(event, data):
    #redirects to proper mouse pressed function depending on mode 
    if (data.mode == "welcome"): 
        welcomeMousePressed(event, data)
    elif (data.mode == "backyard"):   
        backyardMousePressed(event, data)
    elif (data.mode == "setupFeed"):       
        setupFeedMousePressed(event, data)
    elif (data.mode == "feedGame"):       
        feedGameMousePressed(event, data)
    elif (data.mode == "setupNap"):       
        setupNapMousePressed(event, data)
    elif (data.mode == "napGame"):       
        napGameMousePressed(event, data)
    elif (data.mode == "setupBrush"):       
        setupBrushMousePressed(event, data)
    elif (data.mode == "brushGame"):       
        brushGameMousePressed(event, data)
        
def mouseMoved(event, data):
    data.xPos = event.x
    data.yPos = event.y
    if (data.mode == "welcome"): 
        welcomeMouseMoved(event, data)
    if (data.mode == "brushGame"): 
        brushGameMouseMoved(event, data)
    
def keyPressed(event, data):
    #direct to correct keypressed mode function
    if (data.mode == "welcome"): 
        welcomeKeyPressed(event, data)
    elif (data.mode == "backyard"):   
        backyardKeyPressed(event, data)
    elif (data.mode == "setupFeed"):       
        setupFeedKeyPressed(event, data)
    elif (data.mode == "feedGame"):       
        feedGameKeyPressed(event, data)
    elif (data.mode == "setupNap"):       
        setupNapKeyPressed(event, data)
    elif (data.mode == "napGame"):       
        napGameKeyPressed(event, data)
    elif (data.mode == "setupBrush"):       
        setupBrushKeyPressed(event, data)
    elif (data.mode == "brushGame"):       
        brushGameKeyPressed(event, data)

def timerFired(data):
    #directed to correct keypressed timer fired
    if (data.mode == "welcome"): 
        welcomeTimerFired(data)
    elif (data.mode == "backyard" or data.mode == "inside"):    #INSIDE STUFF 
        backyardTimerFired(data)
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
    elif (data.mode == "backyard"):   
        backyardRedrawAll(canvas, data)
    elif (data.mode == "setupFeed"):       
        setupFeedRedrawAll(canvas, data)
    elif (data.mode == "feedGame"):       
        feedGameRedrawAll(canvas, data)
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
    
    filenames = ["tree.gif","food.gif","brush.gif","bed.gif", "fish.gif", "bowl.gif", "petcat.gif","fence.gif", "sheep.gif"] #images labeled for reuse from google.com 
    
    for filename in filenames:
        data.gameImages[filename] = PhotoImage(file=filename)
    
   
    

####################################
# welcome screen
####################################

def welcomeMousePressed(event, data):
    clickX = event.x
    clickY = event.y
    
    if data.width//2-(150//2)+150 > clickX and clickX > data.width//2-(150//2) and data.height*(3/4)+50 > clickY and clickY > data.height*(3/4):
        data.mode = "backyard"
    pass

def welcomeKeyPressed(event, data):
    #only respond to the "p" key
    if (event.char == "p"):
        #go into play mode
        data.mode = "play"
        
def welcomeMouseMoved(event, data):
    if data.width//2-(150//2)+150 > data.xPos and data.xPos > data.width//2-(150//2) and data.height*(3/4)+50 > data.yPos and data.yPos > data.height*(3/4):
        data.playButtonColor = rgbString(161,66,68)
    else:
        data.playButtonColor = rgbString(249,194,209)

def welcomeTimerFired(data):
    if data.filename == "cat1.gif":
         data.filename = "cat2.gif"
    else:
        data.filename = "cat1.gif"
        
    data.welcomeX -= 10
    if data.welcomeX < 0:
        data.welcomeX = data.width 

def rgbString(red, green, blue):
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
    
    image = getCat(data)
    canvas.create_image(left, top, anchor=NW, image=image)
    
    
   
    
####################################
# backyard game mode 
####################################

def backyardMousePressed(event, data):
    pass
        
def backyardKeyPressed(event, data):
    
    #move cat around backyard 
    if event.keysym == "Right" and data.catX < data.width-60:
        data.catX += 20
    elif event.keysym == "Left" and data.catX > 0:
        data.catX -= 20
    elif event.keysym == "Up" and data.catY > 0:
        data.catY -= 20
    elif event.keysym == "Down" and data.catY < data.height-60:
        data.catY += 20
        
    #check for food collision
    if imageCollide(data.imageCat, data.imageFood, data.catX, data.catY, data.width-data.imageFood.width()//2, data.height-data.imageFood.height()//2):
        data.collide = True
        data.playGame = "Food Game"
    #check for brush collision
    elif imageCollide(data.imageCat, data.imageBrush, data.catX, data.catY, data.width//2, data.height-data.imageBrush.height()//2):
        data.collide = True
        data.playGame = "Brush Game"
    #check for bed collision
    elif imageCollide(data.imageCat, data.imageBed, data.catX, data.catY, data.imageBed.width()//2, data.height-data.imageBrush.height()//2): 
        data.collide = True
        data.playGame = "Cat Nap"
    else:
        data.collide = False
        data.playGame = ""
    
    #SWITCH TO FOOD GAME 
    if data.playGame == "Food Game" and (event.keysym == "Enter" or event.keysym == "Return"):
        data.mode = "setupFeed"    
        
    #SWITCH TO BRUSH GAME setup
    if data.playGame == "Brush Game" and (event.keysym == "Enter" or event.keysym == "Return"):
        data.mode = "setupBrush"
            
    #SWITCH TO NAP GAME setup
    if data.playGame == "Cat Nap" and (event.keysym == "Enter" or event.keysym == "Return"):
        data.mode = "setupNap"  
    
def backyardTimerFired(data):
    if data.hungry > 10:
        data.hungry = 10
    if data.sleepy > 10:
        data.sleepy = 10
    if data.happy > 10:
        data.happy = 10
        
    data.timer += 1
    
    if data.timer % 50 == 0:
        data.happy -= 1
    if data.timer % 25 == 0:
        data.sleepy -= 1
    if data.timer % 40 == 0:
        data.hungry -= 1
 

def backyardRedrawAll(canvas, data):
    
    data.filename = "cathead.gif"
    canvas.create_rectangle(0, 0, data.width+10, data.height+10, fill=rgbString(0,181,240))
    canvas.create_rectangle(50,50,data.width-50, data.height-50, fill=rgbString(0,198,62))

    #tree image 
    data.imageTree = getImage(data, "tree.gif")
    canvas.create_image(data.width//2-data.imageTree.width()//2, 0, anchor=NW, image=data.imageTree)
    
    #food image 
    data.imageFood = getImage(data, "food.gif")
    canvas.create_image(data.width-data.imageFood.width()//2, data.height-data.imageFood.height()//2, image=data.imageFood)
    
    #brush image 
    data.imageBrush = getImage(data, "brush.gif")
    canvas.create_image(data.width//2, data.height-data.imageBrush.height()//2, image=data.imageBrush)
    
    #bed image 
    data.imageBed = getImage(data, "bed.gif")
    canvas.create_image(data.imageBed.width()//2, data.height-data.imageBrush.height()//2, image=data.imageBed)
    
    #print out scores and timer at top left 
    canvas.create_text(10, 0, 
                       text = "Time: "+str(data.timer//7), 
                       font="Arial 25 bold", anchor="nw")
    
    canvas.create_text(10,100, #data.height 
                       text = "Happy: "+str(data.happy), 
                       font="Arial 25 bold", anchor="sw")
    canvas.create_text(10,150, 
                       text = "Sleepy: "+str(data.sleepy), 
                       font="Arial 25 bold", anchor="sw")
    canvas.create_text(10,200, 
                       text = "Hungry: "+str(data.hungry), 
                       font="Arial 25 bold", anchor="sw")
                       
    data.imageCat = getCat(data)
    canvas.create_image(data.catX, data.catY, image=data.imageCat)
    
    if data.collide:
        canvas.create_text(data.width, 0, text="Press Enter to Play %s" % data.playGame, anchor=NE)

    
    
    
def imageCollide(image1, image2, x1, y1, x2, y2): #from 15-112 Lab 1
    w1 = image1.width()
    w2 = image2.width()//2 #this works better for some reason
    h1 = image1.height()
    h2 = image2.height()
    
    if (x2 >= x1 and x2 <= x1+w1 and y2 >= y1 and y2 <= y1+h1):
        return True 
    if (x2+w2 >= x1 and x2+w2 <= x1+w1 and y2+h2 >= y1 and y2+h2 <= y1+h1):
        return True
    if (x2+w2 >= x1 and x2+w2 <= x1+w1 and y2 >= y1 and y2 <= y1+h1):
        return True 
    if (x2 >= x1 and x2 <= x1+w1 and y2+h2 >= y1 and y2+h2 <= y1+h1):
        return True 
        
    if (x1 >= x2 and x1 <= x2+w2 and y1 >= y2 and y1 <= y2+h2):
        return True 
    if (x1+w1 >= x2 and x1+w1 <= x2+w2 and y1+h1 >= y2 and y1+h1 <= y2+h2):
        return True
    if (x1+w1 >= x2 and x1+w1 <= x2+w2 and y1 >= y2 and y1 <= y2+h2):
        return True 
    if (x1 >= x2 and x1 <= x2+w2 and y1+h1 >= y2 and y1+h1 <= y2+h2):
        return True 
    else:
        return False

#distance formula to find distance between 
#mouse pressed and center of each target
def distance(x1, y1, x2, y2):
    return ((x2 - x1)**2 + (y2 - y1)**2)**(1/2)
            

####################################
# set up feed
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
    canvas.create_text(data.width//2, data.height//2, text="Welcome to the feeding game! \n Try to catch as many fish as you can! \n Press Enter to Begin")
    pass 
    
####################################
# feed game
####################################

def feedGameMousePressed(event, data):
    pass

def feedGameKeyPressed(event, data):
    
    if event.keysym == "Right" and data.bowlX < data.width-150:
        data.bowlX += 20
    elif event.keysym == "Left" and data.bowlX > 0:
        data.bowlX -= 20
    
    #move left and right with keys 
    #if fish reaches bottom, remove from list

    pass

def feedGameTimerFired(data):
    data.feedTimer += 1
    if data.feedTimer % 10 == 0:
        data.feedCountdown -= 1 
        
    if data.feedTimer % 25 == 0:
        createNewFish(data)
        
        
    if data.feedCountdown < 1: 
        data.hungry += data.feedScore
        data.mode = "backyard"
        
    #fish falling every second 
    for i in range(len(data.fishes)):
        data.fishes[i][1] += 10
        
    #if time runs out and score > 10, data.hungry = 10 
    #def imageCollide(image1, image2, x1, y1, x2, y2) 
        if imageCollide(data.imageBowl, getImage(data, "fish.gif"), data.bowlX, data.bowlY, data.fishes[i][0], data.fishes[i][1]):
            #remove it, add to score
            data.fishes.remove(data.fishes[i])
            data.feedScore += 1
       
    

def feedGameRedrawAll(canvas, data):
    data.imageBowl = getImage(data, "bowl.gif")
    canvas.create_image(data.bowlX, data.bowlY, image=data.imageBowl)
    drawFishes(canvas, data)
    canvas.create_text(30,40,text="Score: "+str(data.feedScore))
    canvas.create_text(30,20,text="Timer: "+str(data.feedCountdown))
    pass 
    
def drawFish(canvas, data, x , y): #from lab6 HW 
    imageFish = getImage(data, "fish.gif")
    canvas.create_image(x, y, image=imageFish)
    
def createNewFish(data):

    fishX = random.randint(0,data.width-100)
    fishY = 0
  
    # 2D list stores data as [fishX, fishY] 
    data.fishes.append([fishX, fishY])

#print out all fish in list 
def drawFishes(canvas, data):
    for i in range(len(data.fishes)):
        #index 0 is x coord, index 1 is y coord
        #draws fish with correct design 
        drawFish(canvas, data, data.fishes[i][0],
                data.fishes[i][1])
    

####################################
# setup brush
####################################

def setupBrushMousePressed(event, data):
    pass

def setupBrushKeyPressed(event, data):
    if event.keysym == "Return":
        data.mode = "brushGame"

def setupBrushTimerFired(data):
    pass

def setupBrushRedrawAll(canvas, data):
    canvas.create_rectangle(0,0, data.width+10, data.height+10, fill="lightgreen")
    canvas.create_text(data.width//2, data.height//2, text="Welcome to the Grooming Game! \n Sooth your cat by brushing its fur \n Press Enter to Begin") 
    
####################################
# brushGame
####################################

def brushGameMousePressed(event, data):
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
    
    if imageCollide(data.imagePetCat, data.imageBrush, data.width//2, data.height//2, data.brushX, data.brushY): 
        data.brushScore += .1
        
    if data.brushCountdown < 1: 
        data.happy += data.brushScore
        data.mode = "backyard"
    

def brushGameRedrawAll(canvas, data):
    canvas.create_text(50,40,text="Score: %.1f" % (data.brushScore))
    canvas.create_text(50,20,text="Timer: "+str(data.brushCountdown))
    data.imagePetCat = getImage(data, "petcat.gif")
    canvas.create_image(data.width//2, data.height//2, image=data.imagePetCat)
    
    canvas.create_image(data.brushX, data.brushY, image=data.imageBrush)
    
    
    #draw a giant cat in the center of screen
    
    pass 
    
####################################
# setupNap
####################################

def setupNapMousePressed(event, data):
    pass

def setupNapKeyPressed(event, data):
    if event.keysym == "Return":
        data.mode = "napGame"
  
def setupNapTimerFired(data):
    pass

def setupNapRedrawAll(canvas, data):
    canvas.create_rectangle(0,0, data.width+10, data.height+10, fill="lavender")
    canvas.create_text(data.width//2, data.height//2, text="Welcome to the Cat Nap Game! \n As your cat dreams, jump over the fences to get points! \n Press Enter to Begin") 
    
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
        
    #eventually space bar is jump 
    pass
  
def napGameTimerFired(data):
    data.napTimer += 1
    
    if data.napTimer % 50 == data.randomTimeNap:
        createNewFence(data)
        data.randomTimeNap = random.randint(0,50)
        #update random number % 25 at least every 25 seconds 
        
    for i in range(len(data.fences)):
        data.fences[i][0] -= 10
        
        if imageCollide(data.imageSheep, getImage(data, "fence.gif"), data.sheepX, data.sheepY, data.fences[i][0], data.fences[i][1]):
            #remove it, add to score
            data.fences = [] #ERROR HERE OUT OF RANGE 
            data.sheepX = data.width//4
            data.sheepY = data.height-100
            
            data.napLives -= 1
    if data.napLives < 1:
        data.mode = "backyard"
        data.sleepy += 10 #data.napScore 
        
        

    
    #position continually moves forward 
    #if collision, stop game, give 3 lives 
    #if fences are removed from list, add to data.sleep score 
    pass

def napGameRedrawAll(canvas, data):
    canvas.create_rectangle(0,0,data.width, data.height, fill="blue")
    #put in little yellow stars!!
    data.imageSheep = getImage(data, "sheep.gif")
    canvas.create_image(data.sheepX, data.sheepY, image=data.imageSheep)
    canvas.create_text(30,30,text="Lives Left: "+ str(data.napLives))
    drawFences(canvas, data)
    
    #sky background, need sheep and repeating fence images 
    pass 
    
def drawFence(canvas, data, x , y):
    imageFence = getImage(data, "fence.gif")
    canvas.create_image(x, y, image=imageFence)
    
def createNewFence(data):

    fenceX = data.width
    fenceY = data.height-75
  
    # 2D list stores data as [fishX, fishY] 
    data.fences.append([fenceX, fenceY])

#print out all fish in list 
def drawFences(canvas, data):
    for i in range(len(data.fences)):
        #index 0 is x coord, index 1 is y coord
        #draws fish with correct design 
        drawFence(canvas, data, data.fences[i][0],
                data.fences[i][1])
    
#def sheepJump():
    #sheepVelocity = 5 positive value 
    #update velocity/position in timer fired 

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

