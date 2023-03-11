# Initialising.
from pygame import *
init()

# Game window parameters.
width = 1200
height = 700
mainWindow = display.set_mode((width, height))
display.set_caption("HE CAN'T KEEP GETTING AWAY WITH THIS")

# Images.
imageDictionary = {
    "frog": transform.scale(image.load("Images//Frog.png"), (30, 30)),
    "frogWin": transform.scale(image.load("Images//Crowned Frog.png"), (40, 40)),
    "blueBike": transform.scale(image.load("Images//Blue Bike.png"), (50, 50)),
    "redCar": transform.scale(image.load("Images//Red Car.png"), (50, 50))
}

# Audio.
audioDictionary = {
    "widePutin": mixer.Sound("Audio//Song For Denise (Perfect Loop).mp3"),
    "breakingBad": mixer.Sound("Audio//Breaking Bad (Extended Theme).mp3")
}

# Background music decider.
mixer.Sound.play(audioDictionary["widePutin"])
pass

# Game loop.
oneSecondTick = 0
gameRunning = True
while gameRunning == True:
    for gameEvent in event.get():
        # Quits game.
        if gameEvent.type == QUIT:
            gameRunning = False
    mainWindow.fill((0, 0, 0))
    display.flip()