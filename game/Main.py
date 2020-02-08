"""Import pygame module."""
import pygame as pg
from Colours import col
from Player import Player

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
plyr = Player(100, 100, 20, 50)

# create list to contain all sprites
sprites = []

# load and scale images

# load player image
player_image = pg.image.load("images/player.png").convert()
# transform players size
player_image = pg.transform.scale(player_image, (plyr.width, plyr.height))
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


def check_keys():
    """Check for key presses."""
    keys = pg.key.get_pressed()

    if keys[pg.K_LEFT]:
        plyr.moveLeft()
    if keys[pg.K_RIGHT]:
        plyr.moveRight(DISPLAY_SIZE[0])


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
    check_collisions(tiles)


def check_collisions(rects):
    """Check for collisions between sprites."""
    player_rect = pg.Rect(plyr.x, plyr.y, plyr.width, plyr.height)
    for rect in rects:
        if player_rect.colliderect(rect):
            plyr.setFloor(True)


run = True
# game loop
while run:
    # limit FPS 50
    clock.tick(50)

    # draw the sprites
    draw_sprites()

    # check for key presses
    check_keys()

    # code to exit the window.
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
