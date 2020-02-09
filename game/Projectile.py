import pygame as pg
from Weapons import weapon_type
import random


class Projectile(object):

    def __init__(self, x, y, type, vel, damage, facing):
        self.x = x
        self.lagTimer = 0
        self.y = y
        self.images = None
        self.image = None
        if type == weapon_type.HASKELL:
            self.images = [pg.image.load('images/bullet_!!.png'), pg.image.load('images/bullet_concat.png'), pg.image.load('images/bullet_curry.png'),  pg.image.load('images/bullet_define.png'),  pg.image.load('images/bullet_filter.png'),
                           pg.image.load('images/bullet_flip.png'),  pg.image.load('images/bullet_fold.png'),  pg.image.load('images/bullet_map.png'),  pg.image.load('images/bullet_scan.png'),  pg.image.load('images/bullet_uncurry.png')]
        self.damage = damage
        self.facing = facing
        self.vel = vel * facing

    def draw(self, display):
        if self.lagTimer == 0:
            self.lagTimer = 10
            self.image = random.choice(self.images)
        else:
            self.lagTimer -= 1
        display.blit(self.image, (self.x, self.y))
