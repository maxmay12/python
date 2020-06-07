#!/usr/bin/env python3

import pgzrun
import random

WIDTH        = 1280
HEIGHT       = 960
CENTRE       = WIDTH/2, HEIGHT/2
FONT_COLOUR  = (255, 255, 255)
SPEED        = 2
SPEEDBALOON  = 8

spieler         = Actor("spieler")
spieler.pos     = WIDTH/2, HEIGHT/2
spieler_leben   = 3

gegnerId        = random.randint(2, 3)
gegner          = Actor("spieler" + str(gegnerId))
gegner.pos      = WIDTH/4, HEIGHT/4
gegner_leben    = 3

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
space_vorher    = False

neues_leben          = Actor("herz3")
neues_leben_sichtbar = False
x_neues_leben        = -10
y_neues_leben        = -10
neues_leben.pos      = x_neues_leben, y_neues_leben

# Das ist die Funktion zum Zeichnen
def draw():
    if spieler_leben > 0 and gegner_leben > 0:
        screen.fill((0, 0, 255))
        spieler.draw()
        gegner.draw()
        wasserbombe_rot.draw()
        wasserbombe_rot2.draw()
        screen.draw.text("Spieler", color=FONT_COLOUR, topleft=(10, 10))
        x_herz = 10
        for l in range(1, spieler_leben+1):
            screen.blit('herz', (x_herz, 30))
            x_herz += 60
        screen.draw.text("Gegner", color=FONT_COLOUR, topleft=(1100, 10))
        x_herz_gegner = 1100
        for l in range(1, gegner_leben+1):
            screen.blit('herz', (x_herz_gegner, 30))
            x_herz_gegner += 60
        if neues_leben_sichtbar:
            neues_leben.draw()
    elif gegner_leben <= 0:
        screen.fill((0, 255, 0))
        screen.draw.text("Du hast gewonnen!", fontsize=60, center=(WIDTH/2, HEIGHT/2), color=FONT_COLOUR)
        screen.draw.text("Drücke ESC, um neu zu starten.", center=(WIDTH/2, 4*HEIGHT/7), color=FONT_COLOUR)
    else:
        screen.fill((255, 0, 0))
        screen.draw.text("Du hast verloren!", fontsize=60, center=(WIDTH/2, HEIGHT/2), color=FONT_COLOUR)
        screen.draw.text("Drücke ESC, um neu zu starten.", center=(WIDTH/2, 4*HEIGHT/7), color=FONT_COLOUR)


def update():
    global wurf
    global wurf_gegner
    global dx
    global dy
    global spieler_leben
    global gegner_leben
    global space_vorher
    global neues_leben
    global neues_leben_sichtbar
    
    # Bewege Spieler    
    if keyboard.left:
        spieler.x -= SPEED

    if keyboard.right:
        spieler.x += SPEED

    if keyboard.up:
        spieler.y -= SPEED

    if keyboard.down:
        spieler.y += SPEED

    if keyboard.ESCAPE:
        if (spieler_leben <= 0 or gegner_leben <= 0):
            spieler_leben = 3
            gegner_leben = 3
            spieler.pos     = WIDTH/2, HEIGHT/2
            gegner.pos      = WIDTH/4, HEIGHT/4
            wurf_gegner     = False
            wurf            = False

    # Bewege Gegner    
    gegner.x += speed_gegner_x
    gegner.y += speed_gegner_y
    

    # Löse Wurf aus
    if keyboard.space and not space_vorher:
        wurf = True
    space_vorher = keyboard.space

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
        if wasserbombe_rot.collidepoint(gegner.pos):
            gegner_leben -= 1
            wurf = False

    # Falls der Rand getroffen wird, setze die Wasserbombe zurück (Position neben Spieler)
    if wasserbombe_rot.pos[0] < 0 or wasserbombe_rot.pos[0] > WIDTH or wasserbombe_rot.pos[1] < 0 or wasserbombe_rot.pos[1] > HEIGHT or (dx == 0 and dy == 0):
        wasserbombe_rot.pos = spieler.pos[0]+20, spieler.pos[1]+10
        dx = 0
        dy = 0
        wurf = False

    # Wasserbombe Gegner
    if wurf_gegner == False:
        wasserbombe_rot2.pos = gegner.pos[0]+20, gegner.pos[1]+10
    else:
        if wasserbombe_rot2.collidepoint(spieler.pos):
            spieler_leben -= 1
            wurf_gegner = False

    if neues_leben_sichtbar == True and neues_leben.collidepoint(spieler.pos):
        neues_leben_sichtbar = False
        clock.schedule(erzeuge_herz, 3.0)
        if spieler_leben < 3:
            spieler_leben += 1
            
if neues_leben_sichtbar == True and neues_leben.collidepoint(gegner.pos):
        neues_leben_sichtbar = False
        clock.schedule(erzeuge_herz, 3.0)
        if gegner_leben < 3:
            gegner_leben += 1
            
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


def erzeuge_herz():
    global neues_leben
    global neues_leben_sichtbar
    neues_leben_sichtbar = True
    x_neues_leben = random.randint(0, WIDTH)
    y_neues_leben = random.randint(0, HEIGHT)
    neues_leben.pos = x_neues_leben, y_neues_leben
    

aendere_bewegungsrichtung_gegner()
clock.schedule(werfe_wasserbombe_gegner, 5.0)
clock.schedule(erzeuge_herz, 1.0)

pgzrun.go()
