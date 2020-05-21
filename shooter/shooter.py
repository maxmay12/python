import pgzrun
import random
from math import pi, sin, cos
from projektil import Projektil

WIDTH        = 1280
HEIGHT       = 960

SPEED        = 2

spieler         = Actor("spieler", anchor=(32, 48))
spieler.pos     = WIDTH/2, HEIGHT/2

_projektile = []
_keyboard_space_previous = False

zombie         = Actor("zombie")
zombie.pos     = WIDTH/3, HEIGHT/3

# Das ist die Funktion zum Zeichnen
def draw():
    screen.fill((128, 128, 255))
    zombie.draw()
    spieler.draw()
    for projektil in _projektile:
        projektil.draw()

def update():
    global _keyboard_space_previous
    
    if keyboard.left:
        spieler.angle += SPEED

    if keyboard.right:
        spieler.angle -= SPEED

    if keyboard.up:
        spieler.y += sin((spieler.angle-90)/180*pi)*SPEED
        spieler.x -= cos((spieler.angle-90)/180*pi)*SPEED

    if keyboard.down:
        spieler.y -= sin((spieler.angle-90)/180*pi)*SPEED
        spieler.x += cos((spieler.angle-90)/180*pi)*SPEED

    if (keyboard.space and not _keyboard_space_previous):
        _projektile.append(Projektil("pfeil", (spieler.x, spieler.y), spieler.angle, 10))
    _keyboard_space_previous = keyboard.space

    for projektil in _projektile:
        projektil.update()  

    
pgzrun.go()
