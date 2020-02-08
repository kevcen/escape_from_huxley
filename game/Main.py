"""Import pygame module."""
import pygame as pg
from Colours import col
from Player import Player
from Projectile import Projectile

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

#---------------------------------------------------
#Code for bullets
bullets = []
#Define weapon, [radius,color,vel,damage]
pistol = (2, (125,125,0), 6, 1)
#maybe change how often you can shoot, but this requires more code
bigGun = (4, (255,0,0), 3, 3)

#in while loop
for bullet in bullets:
    if bullet.x < 500 and bullet.x > 0:
        bullet.x += bullet.vel  # Moves the bullet by its vel
    else:
        bullets.pop(bullets.index(bullet))

#When space bar is pressed, the bullet is fired based on direction of Player
if keys[pygame.K_SPACE]:
    if man.left:
        facing = -1
    else:
        facing = 1

    if len(bullets) < 5:  # This will make sure we cannot exceed 5 bullets on the screen at once
        bullets.append(Projectile(round(man.x+man.width//2), round(man.y + man.height//2), man.weapon[0], man.weapon[1], man.weapon[2], man.weapon[3], facing))

#to draw the bullets
def redrawGameWindow():
    win.blit(bg, (0,0))
    man.draw(win)
    for bullet in bullets:
        bullet.draw(win)

    pygame.display.update()
#---------------------------------------------------


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
