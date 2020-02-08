"""Import pygame module."""
import pygame as pg
from Colours import col
from Player import Player
from Projectile import Projectile

# initialise pygame
pg.init()

# set display dimensions
DISPLAY_SIZE = (600, 400)

# set the size of the tile images
TILE_SIZE = 32

# create display
display = pg.display.set_mode(DISPLAY_SIZE)
# set a caption for the display
pg.display.set_caption("ESCAPE FROM HUXLEY")

# create a clock object to control FPS.
clock = pg.time.Clock()

# create the player object
plyr = Player(100, 100, 50, 20)

# create list to contain all sprites
sprites = []

# load and scale images

# load player image
player_image = pg.image.load("images/player.png").convert()
# transform players size
player_image = pg.transform.scale(player_image, (plyr.height, plyr.width))
# set the pixels behind the player to white.
player_image.set_colorkey((255, 255, 255))

dirt = pg.image.load("images/dirt.png")
dirt = pg.transform.scale(dirt, (TILE_SIZE, TILE_SIZE))
grass = pg.image.load("images/grass.png")
grass = pg.transform.scale(dirt, (TILE_SIZE, TILE_SIZE))

# array to represent tiles.
game_map = [['0', '0', '0', '0', '0', '0', '0', '0', '0', '0',
             '0', '0', '0', '0', '0', '0', '0', '0', '0'],
            ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0',
                '0', '0', '0', '0', '0', '0', '0', '0', '0'],
            ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0',
                '0', '0', '0', '0', '0', '0', '0', '0', '0'],
            ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0',
                '0', '0', '0', '0', '0', '0', '0', '0', '0'],
            ['0', '0', '0', '0', '0', '0', '0', '2', '2', '2',
                '2', '2', '0', '0', '0', '0', '0', '0', '0'],
            ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0',
                '0', '0', '0', '0', '0', '0', '0', '0', '0'],
            ['2', '2', '0', '0', '0', '0', '0', '0', '0', '0',
                '0', '0', '0', '0', '0', '0', '0', '2', '2'],
            ['1', '1', '2', '2', '2', '2', '2', '2', '2', '2',
                '2', '2', '2', '2', '2', '2', '2', '1', '1'],
            ['1', '1', '1', '1', '1', '1', '1', '1', '1', '1',
                '1', '1', '1', '1', '1', '1', '1', '1', '1'],
            ['1', '1', '1', '1', '1', '1', '1', '1', '1', '1',
                '1', '1', '1', '1', '1', '1', '1', '1', '1'],
            ['1', '1', '1', '1', '1', '1', '1', '1', '1', '1',
                '1', '1', '1', '1', '1', '1', '1', '1', '1'],
            ['1', '1', '1', '1', '1', '1', '1', '1', '1', '1',
                '1', '1', '1', '1', '1', '1', '1', '1', '1'],
            ['1', '1', '1', '1', '1', '1', '1', '1', '1', '1',
                '1', '1', '1', '1', '1', '1', '1', '1', '1']]


def draw_sprites():
    """Draw all sprites."""
    display.fill(col.BACKGROUND.value)
    plyr.fall(DISPLAY_SIZE[0], 3)
    plyr.draw(display, player_image)
    draw_tiles()
    for sprite in sprites:
        sprite.draw(display)
    # Update the display
    pg.display.update()


#Code for bullets
bullets = []
#Define weapon, [radius,color,vel,damage]
pistol = (2, (125,125,0), 6, 1)
#maybe change how often you can shoot, but this requires more code
bigGun = (4, (255,0,0), 3, 3)


#to draw the bullets
def redrawGameWindow():
    display.blit(bg, (0,0))
    plyr.draw(display)
    for bullet in bullets:
        bullet.draw(display)
    pygame.display.update()


def check_keys():
    """Check for key presses."""
    keys = pg.key.get_pressed()

    if keys[pg.K_LEFT]:
        plyr.moveLeft()
    if keys[pg.K_RIGHT]:
        plyr.moveRight(DISPLAY_SIZE[0])

        # When space bar is pressed, the bullet is fired based on direction of Player
    if keys[pygame.K_SPACE]:
        if plyr.left:
            facing = -1
        else:
            facing = 1

        if len(bullets) < 5:  # This will make sure we cannot exceed 5 bullets on the screen at once
            bullets.append(
                Projectile(round(plyr.x + plyr.width // 2), round(plyr.y + plyr.height // 2), plyr.weapon[0], plyr.weapon[1],
                           plyr.weapon[2], plyr.weapon[3], facing))





def draw_tiles():
    """Code to draw the tiles."""
    tiles = []
    y = 0
    for layer in game_map:
        x = 0
        for tile in layer:
            if tile == '1':
                display.blit(dirt, (x*TILE_SIZE, y*TILE_SIZE))
            if tile == '2':
                display.blit(grass, (x*TILE_SIZE, y*TILE_SIZE))
            if tile != '0':
                tiles.append(pg.Rect(x*TILE_SIZE, y*TILE_SIZE, TILE_SIZE, TILE_SIZE))
            x += 1
        y += 1
    pg.display.update()
    # check_collisions(tiles)


def check_collisions(rects):
    """Check for collisions between sprites."""
    player_rect = pg.Rect(plyr.x, plyr.y, plyr.width, plyr.height)
    # for rect in rects:
    #    if player_rect.colliderect(rect):

    # add collision checking logic here

def move_bullets():
    global bullets
    for bullet in bullets:
        if bullet.x < 500 and bullet.x > 0:
            bullet.x += bullet.vel  # Moves the bullet by its vel
        else:
            bullets.pop(bullets.index(bullet))

run = True
# game loop
while run:
    # limit FPS 50
    clock.tick(50)

    # draw the sprites
    draw_sprites()

    # check for key presses
    check_keys()

    #moves bullets
    move_bullets()

    # code to exit the window.
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
