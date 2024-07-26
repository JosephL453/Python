import pgzrun
from random import randint


WIDTH = 600
HEIGHT = 500

score = 0
gameover = False

bee = Actor("bee.png")
bee.pos = (100,100)

flower = Actor("flower.png")

def draw():
    screen.blit("background.png", (0,0))
    bee.draw()
    flower.draw()
    screen.draw.text("Score: " + str(score), color = "Black", topleft = (10,10))

    if gameover:
        screen.fill("pink")
        screen.draw.text("TIME UP, FINAL SCORE: " + str(score), color = "Red", fontsize = 50, midtop = (300,25))


def place_flower():
    flower.x = (randint(70, WIDTH - 70))
    flower.y = (randint(70, HEIGHT - 70))

def time_up():
    global gameover
    gameover = True


def update():
    global score
    if keyboard.left:
        bee.x -= 2
    
    if keyboard.right:
        bee.x += 2

    if keyboard.up:
        bee.y -= 2
    
    if keyboard.down:
        bee.y += 2
    
    flower_collected = bee.colliderect(flower)

    if flower_collected:
        score += 10
        place_flower()


clock.schedule(time_up, 60.0)
pgzrun.go()



