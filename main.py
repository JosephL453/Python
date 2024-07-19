import pgzrun
from random import randint

TITLE = "Good Shot"

WIDTH = 800

HEIGHT = 600

message = ""

alien = Actor("alien.png")


def place_alien():
    alien.x = randint(50, WIDTH - 50)
    alien.y = randint(50, HEIGHT - 50)

def draw():
    screen.clear()
    screen.fill(color = (128, 0, 0))
    # place_alien()
    alien.draw()
    screen.draw.text(message, center = (400, 50), fontsize = 60)
    




def on_mouse_down(pos):
    global message
    if alien.collidepoint(pos):
        message = "Good Shot"
        place_alien()
    else:
        message = "You Missed"
    
place_alien()
pgzrun.go()
