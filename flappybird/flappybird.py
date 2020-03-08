import pgzrun
import random

WIDTH        = 600
HEIGHT       = 800
GAP = 130
SPEED = 3
GRAVITY = 0.3
FLAP_VELOCITY = -6.5

bird = Actor("bird_one", (72, 200))
bird.dead = False
bird.vy = 0
pipe_top = Actor("pipe_down", anchor=("left", "bottom"))
pipe_bottom = Actor("pipe_up", anchor=("left", "top"))

def draw():
    screen.blit("skyline2", (0, 0))
    pipe_top.draw()
    pipe_bottom.draw()
    bird.draw()

def reset_pipes():
    pipe_gap_y = random.randint(200, HEIGHT - 200)
    pipe_top.pos = (WIDTH, pipe_gap_y - GAP // 2)
    pipe_bottom.pos = (WIDTH, pipe_gap_y + GAP // 2)

def update_pipes():
    pipe_top.left -= SPEED
    pipe_bottom.left -= SPEED
    if pipe_top.right < 0:
        reset_pipes()

def update():
   update_pipes()
   update_bird()

def update_bird():
    uy = bird.vy
    bird.vy += GRAVITY
    bird.y  += bird.vy
    bird.x   = 75
    if not bird.dead:
        if bird.vy < -3:
            bird.image = "bird_three"
        else:
            bird.image = "bird_one"

def on_key_down():
    if not bird.dead:
        bird.vy = FLAP_VELOCITY

pgzrun.go()
