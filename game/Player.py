"""Import pygame module."""
import pygame as pg


class Player(object):
    """Player object."""

    def __init__(self, x, y, width, height, colour):
        """Construct."""
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.colour = colour

    def draw(self, display):
        """Draw the player."""
        pg.draw.rect(display, self.colour,
                     (self.x, self.y, self.width, self.height))
