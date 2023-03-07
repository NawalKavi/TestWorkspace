# Initialising.
from pygame import *

init()

# Game window parameters.
width = 1200
height = 700
mainWindow = display.set_mode((width, height))
display.set_caption("HE CAN'T KEEP GETTING AWAY WITH THIS")

# Dictionary for images.
imageDictionary = {
    "frogWin": transform.scale(image.load("Images//Crowned Frog.png"), (40, 40))

}

# Game loop.
oneSecondTick = 0
gameRunning = True
while gameRunning == True:
    for gameEvent in event.get():
        # Quits game.
        if gameEvent.type == QUIT:
            gameRunning = False
    display.flip()
