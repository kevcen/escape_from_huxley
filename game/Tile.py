import pygame as pg


class Tile(object):
    """Class to create tiles."""

    def __init__(self, x, y, width, height):
        """Construct."""
        self.x = x
        self.y = y
        self.width = width
        self.height = height
