import pgzrun
import random

WIDTH        = 1280
HEIGHT       = 960
SPEED        = 2
SPEEDBALOON  = 8

spieler         = Actor("spieler")
spieler.pos     = WIDTH/2, HEIGHT/2

wasserbombe_rot = Actor("wasserbombe_rot")
wasserbombe_rot.pos = spieler.pos[0]+20, spieler.pos[1]+10

wurf            = False
dx              = 0
dy              = 0

# Das ist die Funktion zum Zeichnen
def draw():
    screen.fill((0, 0, 255))
    spieler.draw()
    wasserbombe_rot.draw()

def update():
    global wurf
    global dx
    global dy

    # Bewege Spieler    
    if keyboard.left:
        spieler.x -= SPEED

    if keyboard.right:
        spieler.x += SPEED

    if keyboard.up:
        spieler.y -= SPEED

    if keyboard.down:
        spieler.y += SPEED

    # Löse Wurf aus
    if keyboard.space:
        wurf = True

    # Ermittle Flugrichtung, falls noch nicht geworfen wurde (Bewegungsrichtung Spieler)
    if wurf == False:
        if keyboard.left:
            dx = -SPEEDBALOON
        elif keyboard.right:
            dx = SPEEDBALOON
        else:
            dx = 0
        if keyboard.up:
            dy = -SPEEDBALOON
        elif keyboard.down:
            dy = SPEEDBALOON
        else:
            dy = 0
        # Platziere Wasserbombe neben Spieler
        wasserbombe_rot.pos = spieler.pos[0]+20, spieler.pos[1]+10
    else:
        # Bewege Wasserbombe
        wasserbombe_rot.pos = wasserbombe_rot.pos[0]+dx, wasserbombe_rot.pos[1]+dy

    # Falls der Rand getroffen wird, setze die Wasserbombe zurück (Position neben Spieler)
    if wasserbombe_rot.pos[0] < 0 or wasserbombe_rot.pos[0] > WIDTH or wasserbombe_rot.pos[1] < 0 or wasserbombe_rot.pos[1] > HEIGHT:
        wasserbombe_rot.pos = spieler.pos[0]+30, spieler.pos[1]+10
        dx = 0
        dy = 0
        wurf = False
    

pgzrun.go()
