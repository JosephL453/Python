import pgzrun
from random import randint
from pygame import Rect


WIDTH = 300
HEIGHT = 300

def draw():
    screen.clear()
    r = randint(0,255)
    g = randint(0,255)
    b = randint(0,255)
    width = WIDTH
    height = HEIGHT - 200
    for i in range (15):
        rect = Rect((0,0), (width, height))
        rect.center = 150, 150
        screen.draw.rect(rect, (r,g,b))
        r -= 20
        g -= 5
        b += 10
        width -= 10
        height += 10
    
pgzrun.go()
