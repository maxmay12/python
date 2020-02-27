import pgzrun
import random

WIDTH  = 1280
HEIGHT = 960
SPEED  = 2

spieler         = Actor("spieler")
spieler.pos     = WIDTH/2, HEIGHT/2
wasserbombe_rot = Actor("wasserbombe_rot")

# Das ist die Funktion zum Zeichnen
def draw():
    screen.fill((0, 255, 0))
    spieler.draw()

def update():
    if keyboard.left:
        spieler.x -= SPEED

    if keyboard.right:
        spieler.x += SPEED

    if keyboard.up:
        spieler.y -= SPEED

    if keyboard.down:
        spieler.y += SPEED

pgzrun.go()
