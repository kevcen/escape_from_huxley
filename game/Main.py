"""Import pygame module."""
import pygame as pg
from Colours import col
from Player import Player

# initialise pygame
pg.init()

# set display dimensions
DISPLAY_SIZE = (1000, 700)

# create display
display = pg.display.set_mode(DISPLAY_SIZE)
# set a caption for the display
pg.display.set_caption("ESCAPE FROM HUXLEY")

# create a clock object to control FPS.
clock = pg.time.Clock()

# create the player object
plyr = Player(500, 300, 50, 50, col.RED.value)

# create list to contain all sprites
sprites = []

# add player to sprites
sprites.append(plyr)


def draw_sprites():
    """Draw all sprites."""
    for sprite in sprites:
        sprite.draw(display)
    # Update the display
    pg.display.update()


run = True
# game loop
while run:
    # limit FPS 50
    clock.tick(50)

    # draw the sprites
    draw_sprites()

    # code to exit the window.
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
