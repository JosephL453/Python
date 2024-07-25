import pgzrun
from random import randint

TITLE = "Good Shot"

WIDTH = 800

HEIGHT = 600

message = ""

bullseye = Actor("bullseye.png")


def place_bullseye():
    bullseye.x = randint(50, WIDTH - 400)
    bullseye.y = randint(50, HEIGHT - 300)

def draw():
    screen.clear()
    screen.fill(color = (128, 0, 0))

    bullseye.draw()
    screen.draw.text(message, center = (400, 50), fontsize = 60)
    




def on_mouse_down(pos):
    global message
    if bullseye.collidepoint(pos):
        message = "Good Shot"
        place_bullseye()
    else:
        message = "You Missed"
    
place_bullseye()
pgzrun.go()
