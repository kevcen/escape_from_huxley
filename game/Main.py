"""Import pygame module."""
import pygame as pg
from Colours import col
from Player import Player
from Tile import Tile
# from Projectile import Projectile

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

# set a value to scroll the screen by
SCROLL = [0, 0]

# Code for bullets
bullets = []
# Define weapon, [radius,color,vel,damage]
pistol = (2, (125, 125, 0), 6, 1)
# maybe change how often you can shoot, but this requires more code
bigGun = (4, (255, 0, 0), 3, 3)

# create the player object
plyr = Player(100, 150, 20, 50, pistol)

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
with open("game/Map.txt", "r") as f:
    mapData = f.read()

mapData = mapData.split("\n")
map = []
for row in mapData:
    map.append(list(row))


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

    # # When space bar is pressed, the bullet is fired based on direction of Player
    # if keys[pg.K_SPACE]:
    #     facing = 1
    #
    #     if len(bullets) < 5:  # This will make sure we cannot exceed 5 bullets on the screen at once
    #         bullets.append(
    #             Projectile(round(plyr.x + plyr.width // 2), round(plyr.y + plyr.height // 2), round(plyr.weapon[0]), plyr.weapon[1],
    #                        plyr.weapon[2], plyr.weapon[3], facing))

        # sprites.extend(bullets)


def draw_tiles():
    """Code to draw the tiles."""
    SCROLL[0] += (plyr.x - SCROLL[0])

    tiles = []
    y = 0
    for layer in map:
        x = 0
        for tile in layer:
            if tile == '1':
                display.blit(dirt, (x*TILE_SIZE - SCROLL[0], y*TILE_SIZE - SCROLL[1]))
            if tile == '2':
                display.blit(grass, (x*TILE_SIZE - SCROLL[0], y*TILE_SIZE - SCROLL[1]))
            if tile != '0':
                tiles.append(
                    Tile(x*TILE_SIZE - SCROLL[0], y*TILE_SIZE - SCROLL[1], TILE_SIZE, TILE_SIZE))
            x += 1
        y += 1

    check_floor(tiles)
    pg.display.update()


def check_floor(tiles):
    """Check for collisions between sprites."""
    floor = False
    for tile in tiles:
        if plyr.y + plyr.height >= tile.y and plyr.y + plyr.height <= tile.y + tile.height:
            if ((plyr.x >= tile.x and plyr.x <= tile.x + tile.width) or
                    (plyr.x + plyr.width >= tile.x and plyr.x + plyr.width <= tile.x + tile.width)):

                floor = True

    plyr.setFloor(floor)


# def move_bullets():
#     global bullets
#     for bullet in bullets:
#         if bullet.x < 500 and bullet.x > 0:
#             bullet.x += bullet.vel  # Moves the bullet by its vel
#         else:
#             bullets.pop(bullets.index(bullet))


run = True
# game loop
while run:
    # limit FPS 50
    clock.tick(50)

    # draw the sprites
    draw_sprites()

    # check for key presses
    check_keys()

    # moves bullets
    # move_bullets()

    # code to exit the window.
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
