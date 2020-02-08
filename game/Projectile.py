import pygame as pg


class Projectile(object):
    def __init__(self, x, y, radius, color, vel, damage, facing):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.damage = damage
        self.facing = facing
        self.vel = 8 * facing

    def draw(self, win):
        pg.draw.circle(win,
                       self.color,
                       (round(self.x),
                        round(self.y)),
                       self.radius)
