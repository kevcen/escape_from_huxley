"""Import pygame module."""
import pygame as pg
from Colours import col
from Player import Player
from Tile import Tile
from Weapons import Weapon
from Projectile import Projectile

# initialise pygame
pg.init()

# define fonts
big_font = pg.font.SysFont("comicsans", 30)
small_font = pg.font.SysFont("papyrus", 15)
# bullet lag for one projectile at once
bullet_lag = 0
# only change weapon slowly when holding question
weapons_lag = 0


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
pistol = Weapon("Pistol", 20, col.BLACK.value, 6, 1)
# maybe change how often you can shoot, but this requires more code
big_gun = Weapon("Big gun", 4, col.RED.value, 3, 3)

# create the player object
plyr = Player(70, 70, 50, 50, pistol)

# create list to contain all sprites
sprites = []

# load and scale images

# load player image
# player_image = pg.image.load("images/mainAvatar_Left1.png").convert()
# # transform players size
# player_image = pg.transform.scale(player_image, (plyr.width, plyr.height))
# # set the pixels behind the player to white.
# player_image.set_colorkey((255, 255, 255))

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
    #--- bullets v
    for bullet in bullets:
        bullet.draw(display)

    # Displays current weaon used
    weapon_text = big_font.render("Weapon: " + plyr.weapon.name, 1, col.BLACK.value)
    switch_text = small_font.render("Press q to switch to next weapon", 1, col.BLACK.value)

    display.blit(weapon_text, (10, 10))
    display.blit(switch_text, (10, 30))
    #----- bullets ^
    plyr.draw(display)
    draw_tiles()
    plyr.fall(DISPLAY_SIZE[0], 3)

    for sprite in sprites:
        sprite.draw(display)

    pg.display.update()


def check_keys():
    """Check for key presses."""
    # one bullet at a time:
    global bullet_lag
    global weapons_lag
    if weapons_lag > 0:
        weapons_lag += 1
    if weapons_lag == 30:
        weapons_lag = 0

    if bullet_lag > 0:
        bullet_lag += 1
    if bullet_lag == 10:
        bullet_lag = 0

    keys = pg.key.get_pressed()

    if keys[pg.K_LEFT]:
        plyr.moveLeft()
    elif keys[pg.K_RIGHT]:
        plyr.moveRight(DISPLAY_SIZE[0])
    else:
        plyr.standing = True
    if keys[pg.K_UP] or plyr.isJump:
        plyr.jump()

    # When space bar is pressed, the bullet is fired based on direction of Player
    if keys[pg.K_SPACE]:
        if bullet_lag == 0:
            bullet_lag += 1
            facing = 1

            if len(bullets) < 5:  # This will make sure we cannot exceed 5 bullets on the screen at once
                bullets.append(
                    Projectile(round(plyr.x + plyr.width // 2), round(plyr.y + plyr.height // 2), plyr.weapon.radius, plyr.weapon.color,
                               plyr.weapon.vel, plyr.weapon.damage, facing))

    if keys[pg.K_q]:
        if weapons_lag == 0:
            weapons_lag += 1
            if plyr.weapon == pistol:
                plyr.weapon = big_gun
            else:
                plyr.weapon = pistol


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


    #plyr1 = pg.Rect(plyr.hitbox[0], plyr.hitbox[1], plyr.hitbox[2], plyr.hitbox[3])
    plyr1 = pg.Rect(plyr.x, plyr.y, plyr.width, plyr.height)
    belowCollisions = []
    aboveCollisions = []
    rightCollisions = []
    leftCollisions = []
    plyr.floor = False
    plyr.y += 1
    for tile in tiles:
        tile1 = pg.Rect(tile.x, tile.y, tile.width, tile.height)
        if plyr1.colliderect(tile1):
            #vertical collisions
            if plyr.upwards:
                aboveCollisions.append(tile)
            elif plyr.falling:
                belowCollisions.append(tile)

            #horizontal collisions
            if plyr.right:
                rightCollisions.append(tile)
            elif plyr.left:
                leftCollisions.append(tile)
    if len(belowCollisions) != 0 and len( rightCollisions) !=0 and len(leftCollisions) !=0:
        tile = belowCollisions[0]
        plyr.y = tile.y - plyr.height
        plyr.floor = True
        plyr.rightCol = False
        plyr.leftCol = False
        plyr.topCol = False
    elif len(aboveCollisions) !=0 and len(rightCollisions) !=0 and len(leftCollisions) !=0:
        tile = aboveCollisions[0]
        plyr.y = tile.y + tile.height
        plyr.floor = False
        plyr.rightCol = False
        plyr.leftCol = False
        plyr.topCol = True
    elif len(rightCollisions) !=0:
        tile = rightCollisions[0]
        plyr.x = tile.x - plyr.width
        plyr.rightCol = True
        plyr.leftCol = False
    elif len(leftCollisions) !=0:
        tile = leftCollisions[0]
        plyr.x = tile.x + tile.width
        plyr.rightCol = False
        plyr.leftCol = True




    # rCollisionTile = check_right(tiles)
    #
    #
    # lCollisionTile = check_left(tiles)
    #
    # tCollisionTile = check_top(tiles)
    #
    #fCollisionTile = check_floor(tiles)
    # print(plyr.x, plyr.y)
    #
    # if rCollisionTile is None or lCollisionTile is None:
    #     print(plyr.x, plyr.y)
    #     boostleft(rCollisionTile)
    #     print(plyr.x, plyr.y)
    #     boostRight(lCollisionTile)
    #
    # print(plyr.x, plyr.y)
    #boostUp(fCollisionTile)
    # print(plyr.x, plyr.y)
    # #boostDown(tCollisionTile)




    pg.display.update()



# def boostLeft(tile):
#     ##boostleft
#     if tile is not None:
#         plyr.x = tile.x - plyr.width
# def boostRight(tile):
#     ##boostRight
#     if tile is not None:
#         plyr.x = tile.x + tile.width
# def boostUp(tile):
#     print(str(plyr.y))
#     if tile is not None:
#         plyr.y = tile.y - plyr.height
#         print(str(plyr.y))
# def boostDown(tile):
#     if tile is not None:
#         plyr.y = tile.y + tile.height




def check_floor(tiles):
    """Check if the player is standing on the floor."""
    collision = False
    collidingTile = None
    for tile in tiles:
        rightBoundary = plyr.hitbox[0] + plyr.hitbox[2]
        bottomBoundary = plyr.hitbox[1] + plyr.hitbox[3]
        leftBoundary = plyr.hitbox[0]
        if bottomBoundary >= tile.y and bottomBoundary < tile.y + tile.height and ((leftBoundary > tile.x and leftBoundary < tile.x + tile.width) or (rightBoundary > tile.x and rightBoundary < tile.x + tile.width)):
            collision = True
            collidingTile = tile


    plyr.setFloor(collision)

    return tile


def check_top(tiles):
    """Check if top of player is hitting tile."""
    collision = False
    collidingTile = None
    for tile in tiles:
        rightBoundary = plyr.hitbox[0] + plyr.hitbox[2]
        topBoundary = plyr.hitbox[1]
        leftBoundary = plyr.hitbox[0]
        if topBoundary <= tile.y + tile.height and topBoundary > tile.y and ((leftBoundary > tile.x and leftBoundary < tile.x + tile.width) or (rightBoundary > tile.x and rightBoundary < tile.x + tile.width)):
            collision = True
            collidingTile = tile


    plyr.setTopCol(collision)
    return tile


def check_right(tiles):
    """Check if right of player is hitting tile."""
    collision = False
    collidingTile = None
    for tile in tiles:
        rightBoundary = plyr.hitbox[0] + plyr.hitbox[2]
        topBoundary = plyr.hitbox[1]
        bottomBoundary = plyr.hitbox[1] + plyr.hitbox[3]
        if rightBoundary >= tile.x and rightBoundary < tile.x + tile.width and ((bottomBoundary > tile.y and bottomBoundary < tile.y + tile.height) or (topBoundary > tile.y and topBoundary < tile.y + tile.height)):
            collision = True
            collidingTile = tile


    plyr.setRightCol(collision)
    return tile


def check_left(tiles):
    """Check if left of player is hitting tile."""
    collision = False
    collidingTile = None
    for tile in tiles:
        leftBoundary = plyr.hitbox[0]
        topBoundary = plyr.hitbox[1]
        bottomBoundary = plyr.hitbox[1] + plyr.hitbox[3]
        if leftBoundary <= tile.x + tile.width and leftBoundary > tile.x and ((bottomBoundary > tile.y and bottomBoundary < tile.y + tile.height) or (topBoundary > tile.y and topBoundary < tile.y + tile.height)):
            collision = True
            collidingTile = tile


    plyr.setLeftCol(collision)
    return tile


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
    clock.tick(60)

    # draw the sprites
    draw_sprites()
    move_bullets()

    # check for key presses
    check_keys()

    # moves bullets
    # move_bullets()

    # code to exit the window.
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
