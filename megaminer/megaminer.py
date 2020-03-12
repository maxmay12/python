import pgzrun
import random

WIDTH        = 1000
HEIGHT       = 800
zaehler      = 0
inc          = 1
bird = Actor("bird_one", (72, 200))
  


def update():
    global zaehler
    global inc
    zaehler += inc
    if zaehler % 255 == 0:
        inc *= -1
    bird.x += 1

def draw():
    screen.fill((zaehler, 0, 0))
    bird.draw()
  
pgzrun.go()
