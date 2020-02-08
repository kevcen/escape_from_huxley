import pygame as pg

class Weapon(object):
    def __init__(self, radius, color, vel, damage):

        self.radius = radius
        self.color = color
        self.damage = damage
        self.vel = vel

    def draw(self, win):
        pg.draw.circle(win,
                       self.color,
                       (round(self.x),
                        round(self.y)),
                       self.radius)
