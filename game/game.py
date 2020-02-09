import sys
import pygame
from pygame.locals import *


clock = pygame.time.Clock()

pygame.init()  # initiates pygame

pygame.display.set_caption('Pygame Platformer')

WINDOW_SIZE = (1200, 800)

TILE_SIZE = 32

display = pygame.display.set_mode(WINDOW_SIZE)  # initiate the window


# display = pygame.Surface((600, 400))  # used as the surface for rendering, which is scaled

moving_right = False
moving_left = False
gravity = 0
air_timer = 0
velocity = 4
walkCount = 0
walkLeft = [pygame.transform.scale(pygame.image.load('images/mainAvatar_Left1.png'), (64,64)),pygame.transform.scale(pygame.image.load('images/mainAvatar_LeftJump2.png'), (64,64)),pygame.transform.scale(pygame.image.load('images/mainAvatar_Left2.png'), (64,64)),pygame.transform.scale(pygame.image.load('images/mainAvatar_LeftJump1.png'), (64,64))]
walkRight = [pygame.transform.scale(pygame.image.load('images/mainAvatar_Right1.png'), (64,64)),pygame.transform.scale(pygame.image.load('images/mainAvatar_RightJump2.png'), (64,64)),pygame.transform.scale(pygame.image.load('images/mainAvatar_Right2.png'), (64,64)),pygame.transform.scale(pygame.image.load('images/mainAvatar_RightJump1.png'), (64,64))]
noWalkPlayer = pygame.transform.scale(pygame.image.load('images/mainAvatarStand.png'), (64,64))

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


player_img = pygame.image.load('images/player.png').convert()
player_img = pygame.transform.scale(player_img, (10, 26))
player_img.set_colorkey((255, 255, 255))


player_rect = pygame.Rect(100, 100, 64, 64)


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


while True:  # game loop
    display.fill((146, 244, 255))  # clear screen by filling it with blue

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

    #draw player
    if walkCount + 1 >= 32: # 4 * 8
        walkCount = 0

    if moving_right:
        display.blit(walkRight[walkCount//8],(player_rect.x - scroll[0], player_rect.y - scroll[1]))
    # display.blit(player_img, (player_rect.x - scroll[0], player_rect.y - scroll[1]))
    elif moving_left:
        display.blit(walkLeft[walkCount//8],(player_rect.x - scroll[0], player_rect.y - scroll[1]))
    else:
        display.blit(noWalkPlayer, (player_rect.x - scroll[0], player_rect.y - scroll[1]))

    for event in pygame.event.get():  # event loop
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
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
