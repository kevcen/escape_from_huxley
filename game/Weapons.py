import pygame as pg
from enum import Enum

class weapon_type(Enum):
    HASKELL = 1
    SQL = 2


class Weapon(object):
    def __init__(self, name, type, vel, damage):
        self.name = name
        self.image = []
        self.type = weapon_type.HASKELL
        self.vel = vel
        self.damage = damage
