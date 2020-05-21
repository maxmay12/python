import pgzrun
import random
from math import sin,cos,pi

WIDTH        = 1280
HEIGHT       = 960

SPEED        = 2

spieler         = Actor("spieler", anchor=(32, 48))
spieler.pos     = WIDTH/2, HEIGHT/2

pfeil         = Actor("pfeil")
pfeil.pos     = WIDTH/2, HEIGHT/2

zombie         = Actor("zombie")
zombie.pos     = WIDTH/3, HEIGHT/3

# Das ist die Funktion zum Zeichnen
def draw():
    screen.fill((128, 128, 255))
    zombie.draw()
    spieler.draw()
    pfeil.draw()

def update():
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

    pfeil.y += sin((spieler.angle-90)/180*pi)*SPEED
    pfeil.x -= cos((spieler.angle-90)/180*pi)*SPEED

    

    
pgzrun.go()
