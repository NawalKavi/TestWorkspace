# Initialising.
from pygame import *
init()

# Game window parameters.
width = 1200
height = 700
mainWindow = display.set_mode((width, height))
display.set_caption("The Chronicles of Big Poppa")

# Images.
imageDictionary = {
    "frog": transform.scale(image.load("Images//Frog.png"), (50, 50)),
    "frogWin": transform.scale(image.load("Images//Crowned Frog.png"), (70, 70)),
    "blueBike": transform.scale(image.load("Images//Blue Bike.png"), (100, 100)),
    "redCar": transform.scale(image.load("Images//Red Car.png"), (100, 100))
}

# Audio.
audioDictionary = {
    "widePutin": mixer.Sound("Audio//Song For Denise (Perfect Loop).mp3"),
    "breakingBad": mixer.Sound("Audio//Breaking Bad (Extended Theme).mp3")
}

# Music whatnot.
mixer.Sound.play(audioDictionary["widePutin"])

# Finds the top-left corner coordinates of an image.
def centreImageX(xTarget, xSize):
    return xTarget - xSize / 2

def centreImageY(yTarget, ySize):
    return yTarget - ySize / 2

def centreImageXFrog(xTargetFrog, xSizeFrog):
    return xTargetFrog - xSizeFrog / 2

def centreImageY(yTargetFrog, ySizeFrog):
    return yTargetFrog - ySizeFrog / 2

def centreImageYFrog(yTargetFrog, ySizeFrog):
    return yTargetFrog - ySizeFrog / 2

# Blitting or something.
def blitImage(image, xyValues):
    mainWindow.blit(image, xyValues)

frogX = centreImageXFrog(600, 40)
frogY = centreImageYFrog(600, 40)
xChangeFrog = 0
yChangeFrog = 0

# Game loop.
gameRunning = True
while gameRunning == True:
    for gameEvent in event.get():
        # Quits game.
        if gameEvent.type == QUIT:
            gameRunning = False
        # Handles player movements.
        if gameEvent.type == KEYDOWN:
            if gameEvent.key == K_UP:
                yChangeFrog -= 25
            if gameEvent.key == K_DOWN:
                yChangeFrog += 25
            if gameEvent.key == K_LEFT:
                xChangeFrog -= 25
            if gameEvent.key == K_RIGHT:
                xChangeFrog += 25
            # Background music control.
            if gameEvent.key == K_p:
                mixer.pause()
            if gameEvent.key == K_u:
                mixer.unpause()

    mainWindow.fill((0, 0, 0))
    # Always blit images after drawing the initial background, because otherwise it'll just cover the images.
    blitImage(imageDictionary["frog"], ((centreImageXFrog(600, 40) + xChangeFrog), (centreImageYFrog(600, 40) + yChangeFrog)))
    # Renders the game.
    display.flip()