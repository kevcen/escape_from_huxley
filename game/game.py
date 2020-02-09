import sys
import pygame
from pygame.locals import *
from Menu import Menu
from Pause import Pause

clock = pygame.time.Clock()

pygame.init()  # initiates pygame

pygame.display.set_caption('ESCAPE FROM HUXLEY')

WINDOW_SIZE = (1200, 800)

TILE_SIZE = 32
AVATAR_SIZE = (118//4, 210//4)

# initiate the window
display = pygame.display.set_mode(WINDOW_SIZE)


moving_right = False
moving_left = False
gravity = 0
air_timer = 0
velocity = 10  # CHANGED FOR QUICK TESTING -
walkCount = 0

walkLeft = [pygame.transform.scale(pygame.image.load('images/mainAvatar_Left1.png'), AVATAR_SIZE), pygame.transform.scale(pygame.image.load('images/mainAvatar_LeftJump2.png'), AVATAR_SIZE),
            pygame.transform.scale(pygame.image.load('images/mainAvatar_Left2.png'), AVATAR_SIZE), pygame.transform.scale(pygame.image.load('images/mainAvatar_LeftJump1.png'), AVATAR_SIZE)]
walkRight = [pygame.transform.scale(pygame.image.load('images/mainAvatar_Right1.png'), AVATAR_SIZE), pygame.transform.scale(pygame.image.load('images/mainAvatar_RightJump2.png'), AVATAR_SIZE),
             pygame.transform.scale(pygame.image.load('images/mainAvatar_Right2.png'), AVATAR_SIZE), pygame.transform.scale(pygame.image.load('images/mainAvatar_RightJump1.png'), AVATAR_SIZE)]
noWalkPlayer = pygame.transform.scale(pygame.image.load('images/mainAvatarStand.png'), AVATAR_SIZE)
bg_image = pygame.transform.scale(pygame.image.load('images/insideBackground.png'), WINDOW_SIZE)


true_scroll = [0, 0]


def load_map(path):
    f = open(path + '.txt', 'r')
    data = f.read()
    f.close()
    data = data.split('\n')
    game_map = []
    for row in data:
        game_map.append(list(row))
    return game_map


game_map = load_map('game/Map')

Carpet_Floor = pygame.image.load('images/Carpet_Floor.png')
Carpet_Floor = pygame.transform.scale(Carpet_Floor, (TILE_SIZE, TILE_SIZE))
dirt_img = pygame.image.load('images/dirt.png')
dirt_img = pygame.transform.scale(dirt_img, (TILE_SIZE, TILE_SIZE))
Computer1 = pygame.image.load('images/Computer_1.png')
Computer1 = pygame.transform.scale(Computer1, (TILE_SIZE, TILE_SIZE))
Computer2 = pygame.image.load('images/Computer_2.png')
Computer2 = pygame.transform.scale(Computer2, (TILE_SIZE, TILE_SIZE))


player_img = pygame.image.load('images/player.png').convert()
player_img = pygame.transform.scale(player_img, (10, 26))
player_img.set_colorkey((255, 255, 255))


player_rect = pygame.Rect(100, 100, AVATAR_SIZE[0], AVATAR_SIZE[1])


def collision_test(rect, tiles):
    hit_list = []
    for tile in tiles:

        if rect.colliderect(tile):
            hit_list.append(tile)
    return hit_list


def move(rect, movement, tiles):
    collision_types = {'top': False, 'bottom': False, 'right': False, 'left': False}
    rect.x += movement[0]
    hit_list = collision_test(rect, tiles)
    for tile in hit_list:
        if movement[0] > 0:
            rect.right = tile.left
            collision_types['right'] = True
        elif movement[0] < 0:
            rect.left = tile.right
            collision_types['left'] = True
    rect.y += movement[1]
    hit_list = collision_test(rect, tiles)
    for tile in hit_list:
        if movement[1] > 0:
            rect.bottom = tile.top
            collision_types['bottom'] = True
        elif movement[1] < 0:
            rect.top = tile.bottom
            collision_types['top'] = True
    return rect, collision_types


# def gameover():
#     """Display the game over screen."""
#     gameover = pg.image.load("images/gameOver.png")
#     gameover = pg.transform.scale(gameover, WINDOW_SIZE)
#     display.blit(gameover, (0, 0))
#     pg.display.update()
#     pg.time.delay(1500)


Menu(display, pygame)

while True:  # game loop
    # display.fill((146, 244, 255))  # clear screen by filling it with blue
    display.blit(bg_image, (0, 0))

    true_scroll[0] += (player_rect.x-true_scroll[0]-300)/20
    true_scroll[1] += (player_rect.y-true_scroll[1]-500)/20
    scroll = true_scroll.copy()
    scroll[0] = int(scroll[0])
    scroll[1] = int(scroll[1])

    tile_rects = []
    y = 0
    for layer in game_map:
        x = 0
        for tile in layer:
            if tile == '1':
                display.blit(dirt_img, (x*TILE_SIZE-scroll[0], y*TILE_SIZE-scroll[1]))
            if tile == '2':
                display.blit(Carpet_Floor, (x*TILE_SIZE-scroll[0], y*TILE_SIZE-scroll[1]))
            if tile == '3':
                display.blit(Computer1, (x*TILE_SIZE-scroll[0], y*TILE_SIZE-scroll[1]))
            if tile == '4':
                display.blit(Computer2, (x*TILE_SIZE-scroll[0], y*TILE_SIZE-scroll[1]))
            if tile != '0':
                tile_rects.append(pygame.Rect(x*TILE_SIZE, y*TILE_SIZE, TILE_SIZE, TILE_SIZE))
            x += 1
        y += 1

    player_movement = [0, 0]
    if moving_right:
        player_movement[0] += velocity
    if moving_left:
        player_movement[0] -= velocity
    player_movement[1] += gravity
    gravity += 0.6
    if gravity > 6:
        gravity = 6

    player_rect, collisions = move(player_rect, player_movement, tile_rects)

    if collisions['bottom'] == True:
        air_timer = 0
        gravity = 0
    else:
        air_timer += 1

    # draw player
    if walkCount + 1 >= 32:  # 4 * 8
        walkCount = 0

    if moving_right:
        display.blit(walkRight[walkCount//8], (player_rect.x -
                                               scroll[0], player_rect.y - scroll[1]))
    # display.blit(player_img, (player_rect.x - scroll[0], player_rect.y - scroll[1]))
    elif moving_left:
        display.blit(walkLeft[walkCount//8], (player_rect.x - scroll[0], player_rect.y - scroll[1]))
    else:
        display.blit(noWalkPlayer, (player_rect.x - scroll[0], player_rect.y - scroll[1]))

    for event in pygame.event.get():  # event loop
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                Pause(display, pygame)
                moving_right = False
                moving_left = False
            if event.key == K_RIGHT:
                moving_right = True
            if event.key == K_LEFT:
                moving_left = True
            if event.key == K_UP:
                if air_timer < 6:
                    gravity = -12
        if event.type == KEYUP:
            if event.key == K_RIGHT:
                moving_right = False
            if event.key == K_LEFT:
                moving_left = False

    # screen.blit(pygame.transform.scale(display, WINDOW_SIZE), (0, 0))
    pygame.display.update()
    clock.tick(60)
