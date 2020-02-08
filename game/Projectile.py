import pygame as pg


class Projectile(object):
    def __init__(self, x, y, radius, color, vel, damage, facing):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.damage = damage
        self.facing = facing
        self.vel = vel * facing

    def draw(self, display):
        pg.draw.circle(display,
                       self.color,
                       (round(self.x),
                        round(self.y)),
                       self.radius)
