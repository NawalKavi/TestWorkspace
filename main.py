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
    "frog": transform.scale(image.load("Images//Frog.png"), (40, 40)),
    "frogWin": transform.scale(image.load("Images//Crowned Frog.png"), (60, 60)),
    "blueBike": transform.scale(image.load("Images//Blue Bike.png"), (70, 70)),
    "redCar": transform.scale(image.load("Images//Red Car.png"), (70, 70))
}

# Audio.
audioDictionary = {
    "widePutin": mixer.Sound("Audio//Song For Denise (Perfect Loop).mp3"),
    "breakingBad": mixer.Sound("Audio//Breaking Bad (Extended Theme).mp3")
}

# Background music decider.
mixer.Sound.play(audioDictionary["widePutin"])

# Blitting or something.
def blitImage(image, xCords, yCords):
    mainWindow.blit(image, (xCords, yCords))

xCords =
yCords = 

# Game loop.
oneSecondTick = 0
gameRunning = True
while gameRunning == True:
    for gameEvent in event.get():
        # Quits game.
        if gameEvent.type == QUIT:
            gameRunning = False
        # Handles keyboard movements.
        if gameEvent.type == KEYDOWN:
            if gameEvent.key == K_UP:
                pass
            elif gameEvent.key == K_DOWN:
                pass
            elif gameEvent.key == K_LEFT:
                pass
            elif gameEvent.key == K_RIGHT:
                pass
    mainWindow.fill((0, 0, 0))
    # Always blit images after drawing the initial background, because otherwise it'll just cover the images.
    blitImage(imageDictionary["frog"], width * 0.45, height * 0.8)
    display.flip()