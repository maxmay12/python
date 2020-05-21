from math import sin,cos,pi
from pgzero.builtins import Actor

class Projektil:

    _speed = 0

    def __init__(self, imagepath, pos, angle, speed):
        self._actor = Actor(imagepath);
        self._actor.pos = pos
        self._actor.angle = angle
        self._speed = speed

    def draw(self):
        self._actor.draw()

    def update(self):
        self._actor.y += sin((self._actor.angle-90)/180*pi)*self._speed
        self._actor.x -= cos((self._actor.angle-90)/180*pi)*self._speed
