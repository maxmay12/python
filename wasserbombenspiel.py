import pgzrun
import random

wasserbombe_rot = Actor("wasserbombe_rot")

# Das ist die Funktion zum Zeichnen
def draw():
    screen.clear()
    wasserbombe_rot.draw()

pgzrun.go()
