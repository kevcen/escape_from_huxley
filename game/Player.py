"""Import pygame module."""
import pygame as pg


class Player(object):
    """Player object."""

    def __init__(self, x, y, width, height, weapon):
        """Construct."""
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.weapon = weapon
        # set player's speed
        self.velocity = 4
        self.floor = False

    def draw(self, display, image):
        """Draw the player."""
        display.blit(image, (self.x, self.y))

    def setVelocity(self, velocity):
        """Set the velocity of the player."""
        self.velocity = velocity

    def moveLeft(self):
        """Move the player left."""
        if self.x > 0:
            self.x -= self.velocity

    def moveRight(self, max):
        """Move the player right."""
        if self.x + self.width < max:
            self.x += self.velocity

    def fall(self, max, gravity):
        """Make the player fall."""
        if self.y + self.height < max:
            self.y += gravity
