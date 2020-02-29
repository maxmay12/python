import pgzrun
import random

WIDTH        = 1280
HEIGHT       = 960
SPEED        = 2
SPEEDBALOON  = 8

spieler         = Actor("spieler")
spieler.pos     = WIDTH/2, HEIGHT/2

gegnerId        = random.randint(2, 3)
gegner          = Actor("spieler" + str(gegnerId))
gegner.pos      = WIDTH/4, HEIGHT/4
speed_gegner_x  = 0
speed_gegner_y  = 0
wasserbombe_rot = Actor("wasserbombe_rot")
wasserbombe_rot.pos = spieler.pos[0]+20, spieler.pos[1]+10


wasserbombe_rot2 = Actor("wasserbombe_rot")
wasserbombe_rot2.pos = gegner.pos[0]+20, gegner.pos[1]+10

wurf            = False
wurf_gegner     = False
wurf_pos        = spieler.pos
dx              = 0
dy              = 0

# Das ist die Funktion zum Zeichnen
def draw():
    screen.fill((0, 0, 255))
    spieler.draw()
    gegner.draw()
    wasserbombe_rot.draw()
    wasserbombe_rot2.draw()

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

    # Bewege Gegner    
    gegner.x += speed_gegner_x
    gegner.y += speed_gegner_y
    

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
    if wasserbombe_rot.pos[0] < 0 or wasserbombe_rot.pos[0] > WIDTH or wasserbombe_rot.pos[1] < 0 or wasserbombe_rot.pos[1] > HEIGHT or (dx == 0 and dy == 0):
        wasserbombe_rot.pos = spieler.pos[0]+20, spieler.pos[1]+10
        dx = 0
        dy = 0
        wurf = False

    # Wasserbombe Gegner
    if wurf_gegner == False:
        wasserbombe_rot2.pos = gegner.pos[0]+20, gegner.pos[1]+10


# Berechne eine zufällige Bewegungsrichtung für den Gegner
def aendere_bewegungsrichtung_gegner():
    global speed_gegner_x
    global speed_gegner_y
    global gegner
    speed_gegner_x = random.randint(-SPEED, SPEED)
    speed_gegner_y = random.randint(-SPEED, SPEED)
    if((gegner.x < 100 and speed_gegner_x < 0) or (gegner.x>WIDTH-100 and speed_gegner_x > 0)):
        speed_gegner_x = -speed_gegner_x
    if((gegner.y < 100 and speed_gegner_y < 0) or (gegner.y>HEIGHT-100 and speed_gegner_y > 0)):
        speed_gegner_y = -speed_gegner_y
    clock.schedule(aendere_bewegungsrichtung_gegner, 1.0)

def ruecksetzen_wasserbombe_gegner():
    global wurf_gegner
    wurf_gegner = False
    

def werfe_wasserbombe_gegner():
    global wurf_gegner
    global wurf_pos
    dx = spieler.x - gegner.x
    dy = spieler.y - gegner.y
    wurf_pos = gegner.pos[0] + dx * 1.5, gegner.pos[1] + dy * 1.5
    wurf_gegner = True
    animate(wasserbombe_rot2, tween='linear', pos=wurf_pos, duration=1.2, on_finished=ruecksetzen_wasserbombe_gegner)
    clock.schedule(werfe_wasserbombe_gegner, 5.0)

aendere_bewegungsrichtung_gegner()
clock.schedule(werfe_wasserbombe_gegner, 5.0)


pgzrun.go()
