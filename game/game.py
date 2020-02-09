import sys
import pygame
from pygame.locals import *
from Menu import Menu
from Pause import Pause

class animation(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.step = 0

    def draw(self):
        if 5 - self.step > 0:
            pygame.draw.circle(display, (255, 255, 255), (round(self.x - scroll[0]), round(self.y - scroll[1])), 50 + self.step*3, 5 - self.step)
            self.step += 1
class projectile(object):

    def __init__(self, x, y, facing, image, damage):
        self.x = x
        self.y = y
        self.facing = facing
        self.vel = 20*facing
        self.damage = damage
        self.image = image
        # self.haskellShots = [pygame.image.load('images/java_this.png'),pygame.image.load('images/java_abstract.png'),pygame.image.load('images/java_final.png'),pygame.image.load('images/java_hash.png')]

    def draw(self, win):
        # self.haskellCount += 1
        # if self.haskellCount + 1 >= 40:
        #     self.haskellCount = 0
        # self.x += self.vel
        #
        # win.blit(self.haskellShots[self.haskellCount//10], (round(self.x - scroll[0]), round(self.y - scroll[1])))
        self.x += self.vel
        win.blit(self.image, (round(self.x - scroll[0]), round(self.y - scroll[1])))


class enemy(object):

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        #self.path = (self.x, self.end)
        self.walkCount = 0
        self.vel = 3
        #self.hitbox = (self.x + 17, self.y + 2, 31, 57)
        self.visible = False
        self.health = 10

        self.tenThousands = pygame.image.load('images/java_10k.png')
        self.shootCount = 0
        self.alive = True
        self.count = 0
        # self.walkRight = [pygame.image.load('images/boss_rightStep1.png'), pygame.image.load('images/boss_rightStep2.png')]
        # self.walkLeft = [pygame.image.load('images/boss_leftWalk1.png'),pygame.image.load('images/boss_leftWalk2.png')]

    def draw(self, win):
        # self.move()
        if self.visible:
            # if self.walkCount + 1 >= 6:
            #     self.walkCount = 0
            # if self.vel > 0:
            #     win.blit(self.walkRight[self.walkCount // 3] , (self.x- count[0], self.y- count[1]))
            #     self.walkCount += 1
            # else:
            #     win.blit(self.walkLeft[self.walkCount // 3] , (self.x- count[0], self.y- count[1]))
            #     self.walkCount += 1
            #self.hitbox = (self.x + 17, self.y + 2, 31, 57)
            if self.alive:
                win.blit(pygame.image.load('images/tony.png'),
                         (self.x - scroll[0], self.y - scroll[1]))
                pygame.draw.rect(win, (255, 0, 0), (self.x -
                                                    scroll[0], self.y - 20 - scroll[1], 64, 5))
                pygame.draw.rect(win, (0, 255, 0), (self.x -
                                                    scroll[0], self.y - 20 - scroll[1], 6.4 * (self.health), 5))
                if self.shootCount > 0:
                    self.shootCount += 1
                if self.shootCount >= 20:
                    self.shootCount = 0
                if self.shootCount == 0:
                    self.shoot(win)
                    self.shootCount = 1

            else:
                if self.count > 50:
                    self.visible = False
                else:
                    self.count += 1
                    if self.count//5 == 0:
                        win.blit(pygame.image.load('images/TonyWither1.png'),
                                 (self.x - scroll[0], self.y - scroll[1]))
                    elif self.count//5 == 1:
                        win.blit(pygame.image.load('images/TonyWither2.png'),
                                 (self.x - scroll[0], self.y - scroll[1]))
                    elif self.count//5 == 2:
                        win.blit(pygame.image.load('images/TonyWither3.png'),
                                 (self.x - scroll[0], self.y - scroll[1]))
                    elif self.count//5 == 3:
                        win.blit(pygame.image.load('images/TonyWither4.png'),
                                 (self.x - scroll[0], self.y - scroll[1]))
                    elif self.count//5 == 4:
                        win.blit(pygame.image.load('images/TonyWither5.png'),
                                 (self.x - scroll[0], self.y - scroll[1]))
                    elif self.count//5 == 5:
                        win.blit(pygame.image.load('images/TonyWither6.png'),
                                 (self.x - scroll[0], self.y - scroll[1]))
                    elif self.count//5 == 6:
                        win.blit(pygame.image.load('images/TonyWither7.png'),
                                 (self.x - scroll[0], self.y - scroll[1]))
                    elif self.count//5 == 7:
                        win.blit(pygame.image.load('images/TonyWither8.png'),
                                 (self.x - scroll[0], self.y - scroll[1]))
                    elif self.count//5 == 8:
                        win.blit(pygame.image.load('images/TonyWither9.png'),
                                 (self.x - scroll[0], self.y - scroll[1]))
                    elif self.count//5 == 9:
                        win.blit(pygame.image.load('images/TonyWither10.png'),
                                 (self.x - scroll[0], self.y - scroll[1]))
                        pygame.mixer.music.load('sounds/normal_bg.mp3')
                        pygame.mixer.music.play(-1)
        #pygame.draw.rect(win, (255,0,0), self.hitbox, 2)

    # def move(self):
    #     if self.vel > 0:
    #         if self.x + self.vel <= self.path[1]:
    #             self.x += self.vel
    #         else:
    #             self.vel = self.vel * -1
    #             self.walkCount = 0
    #     else:
    #         if self.x + self.vel >= self.path[0]: #is it plus?
    #             self.x += self.vel
    #         else:
    #             self.vel = self.vel * -1
    #             self.walkCount = 0

    def hit(self, damage):
        if self.health > 0:
            self.health -= damage
        else:
            self.die()

    def die(self):
        self.alive = False

    def shoot(self, win):
        enemyBullets.append(projectile(self.x, self.y, 1, self.tenThousands, 1))
        enemyBullets.append(projectile(self.x, self.y, -1, self.tenThousands, 1))


enemyBullets = []
clock = pygame.time.Clock()
shooting = False

pygame.init()  # initiates pygame

pygame.display.set_caption('ESCAPE FROM HUXLEY')

WINDOW_SIZE = (1200, 800)

TILE_SIZE = 48

AVATAR_SIZE = (118//4, 210//4)

# initiate the window
display = pygame.display.set_mode(WINDOW_SIZE)


moving_right = False
moving_left = False
gravity = 0
air_timer = 0
velocity = 25  # CHANGED FOR QUICK TESTING -
walkCount = 0
wasLeft = False
wasRight = True

walkLeft = [pygame.transform.scale(pygame.image.load('images/mainAvatar_Left1.png'), AVATAR_SIZE), pygame.transform.scale(pygame.image.load('images/mainAvatar_LeftJump2.png'), AVATAR_SIZE),
            pygame.transform.scale(pygame.image.load('images/mainAvatar_Left2.png'), AVATAR_SIZE), pygame.transform.scale(pygame.image.load('images/mainAvatar_LeftJump1.png'), AVATAR_SIZE)]
walkRight = [pygame.transform.scale(pygame.image.load('images/mainAvatar_Right1.png'), AVATAR_SIZE), pygame.transform.scale(pygame.image.load('images/mainAvatar_RightJump2.png'), AVATAR_SIZE),
             pygame.transform.scale(pygame.image.load('images/mainAvatar_Right2.png'), AVATAR_SIZE), pygame.transform.scale(pygame.image.load('images/mainAvatar_RightJump1.png'), AVATAR_SIZE)]
noWalkPlayer = walkRight[0]
bg_image = pygame.transform.scale(pygame.image.load('images/insideBackground.png'), WINDOW_SIZE)

bulletSound = pygame.mixer.Sound('sounds/code_shoot.wav')
hitSound = pygame.mixer.Sound('sounds/code_hit.wav')

pygame.mixer.music.load('sounds/normal_bg.mp3')
pygame.mixer.music.play(-1)


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
game_map2 = load_map('game/Map2')
game_map3 = load_map('game/Map3')

Carpet_Floor = pygame.image.load('images/huxley_top.png')
Carpet_Floor = pygame.transform.scale(Carpet_Floor, (TILE_SIZE, TILE_SIZE))
Carpet_Left = pygame.image.load('images/huxley_topleft.png')
Carpet_Left = pygame.transform.scale(Carpet_Left, (TILE_SIZE, TILE_SIZE))
Carpet_Right = pygame.image.load('images/huxley_topright.png')
Carpet_Right = pygame.transform.scale(Carpet_Right, (TILE_SIZE, TILE_SIZE))
dirt_img = pygame.image.load('images/huxley_mid.png')
dirt_img = pygame.transform.scale(dirt_img, (TILE_SIZE, TILE_SIZE))
Computer1 = pygame.image.load('images/Computer_1.png')
Computer1 = pygame.transform.scale(Computer1, (TILE_SIZE, TILE_SIZE))
Computer2 = pygame.image.load('images/Computer_2.png')
Computer2 = pygame.transform.scale(Computer2, (TILE_SIZE, TILE_SIZE))
Computer3 = pygame.image.load('images/Computer_3.png')
Computer3 = pygame.transform.scale(Computer3, (TILE_SIZE, TILE_SIZE))
Computer4 = pygame.image.load('images/Computer_4.png')
Computer4 = pygame.transform.scale(Computer4, (TILE_SIZE, TILE_SIZE))
CeilingLight = pygame.image.load('images/LowerCeiling.png')
CeilingLight = pygame.transform.scale(CeilingLight, (TILE_SIZE, TILE_SIZE))
CeilingNoLight = pygame.image.load('images/LowerCeiling2.png')
CeilingNoLight = pygame.transform.scale(CeilingNoLight, (TILE_SIZE, TILE_SIZE))
CeilingLeftTop = pygame.image.load('images/Ceiling_LeftTop.png')
CeilingLeftTop = pygame.transform.scale(CeilingLeftTop, (TILE_SIZE, TILE_SIZE))
CeilingRightTop = pygame.image.load('images/Ceiling_RightTop.png')
CeilingRightTop = pygame.transform.scale(CeilingRightTop, (TILE_SIZE, TILE_SIZE))
Roof = pygame.image.load('images/huxley_top.png')
Roof = pygame.transform.scale(Roof, (TILE_SIZE, TILE_SIZE))
WallLeftInner = pygame.image.load('images/huxley_right.png')
WallLeftInner = pygame.transform.scale(WallLeftInner, (TILE_SIZE, TILE_SIZE))
WallLeftOuter = pygame.image.load('images/huxley_left.png')
WallLeftOuter = pygame.transform.scale(WallLeftOuter, (TILE_SIZE, TILE_SIZE))
WallRightInner = pygame.image.load('images/huxley_left.png')
WallRightInner = pygame.transform.scale(WallRightInner, (TILE_SIZE, TILE_SIZE))
WallRightOuter = pygame.image.load('images/huxley_right.png')
WallRightOuter = pygame.transform.scale(WallRightOuter, (TILE_SIZE, TILE_SIZE))
WallBottom = pygame.image.load('images/huxley_bottom.png')
WallBottom = pygame.transform.scale(WallBottom, (TILE_SIZE, TILE_SIZE))
WallTopLeft = pygame.image.load('images/huxley_topleft.png')
WallTopLeft = pygame.transform.scale(WallTopLeft, (TILE_SIZE, TILE_SIZE))
WallTopRight = pygame.image.load('images/huxley_topright.png')
WallTopRight = pygame.transform.scale(WallTopRight, (TILE_SIZE, TILE_SIZE))
WallBotRight = pygame.image.load('images/huxley_botright.png')
WallBotRight = pygame.transform.scale(WallBotRight, (TILE_SIZE, TILE_SIZE))
WallBotLeft = pygame.image.load('images/huxley_botleft.png')
WallBotLeft = pygame.transform.scale(WallBotLeft, (TILE_SIZE, TILE_SIZE))
Window = pygame.image.load('images/window.png')
Window = pygame.transform.scale(Window, (TILE_SIZE, TILE_SIZE))
Mystical = pygame.image.load('images/Mystical.png')
Mystical = pygame.transform.scale(Mystical, (TILE_SIZE, TILE_SIZE))
phoneBoy1 = pygame.image.load('images/phoneBoy1.png')
phoneBoy1 = pygame.transform.scale(phoneBoy1, (TILE_SIZE, TILE_SIZE))
phoneBoy2 = pygame.image.load('images/phoneBoy2.png')
phoneBoy2 = pygame.transform.scale(phoneBoy2, (TILE_SIZE, TILE_SIZE))
blackboard_clean = pygame.image.load('images/blackboard_clean.png')
blackboard_clean = pygame.transform.scale(blackboard_clean, (TILE_SIZE*3, TILE_SIZE*2))
blackboard_drawn = pygame.image.load('images/blackboard_drawn.png')
blackboard_drawn = pygame.transform.scale(blackboard_drawn, (TILE_SIZE*3, TILE_SIZE*2))
Konstantinos = pygame.image.load('images/Konstantinos.png')
Konstantinos = pygame.transform.scale(Konstantinos, (TILE_SIZE*2, TILE_SIZE*2))
ICHack = pygame.image.load('images/ICHack.png')
ICHack = pygame.transform.scale(ICHack, (TILE_SIZE*2, TILE_SIZE))
ICCrest = pygame.image.load('images/ImperialCrest.png')
ICCrest = pygame.transform.scale(ICCrest, (TILE_SIZE, TILE_SIZE))
haskellLogo = pygame.image.load('images/haskellLogo.png')
haskellLogo = pygame.transform.scale(haskellLogo, (TILE_SIZE, TILE_SIZE))


player_img = pygame.image.load('images/player.png').convert()
player_img = pygame.transform.scale(player_img, (10, 26))
player_img.set_colorkey((255, 255, 255))

player_rect = pygame.Rect(100, 100, AVATAR_SIZE[0], AVATAR_SIZE[1])

bullets = []


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


Menu(display, pygame)


def gameover():
    global pygame
    gameover = pygame.transform.scale(pygame.image.load("images/gameOver.png"), WINDOW_SIZE)
    display.blit(gameover, (0, 0))
    pygame.display.update()
    pygame.time.delay(1500)
    quit()


health = 10


def takeDamage():
    global health
    health -= 5
    if health == 0:
        gameover()


shootLoop = 0
computerCount = 0
phoneBoyCount = 0
tony = enemy(3600 * 3/2, 860 * 3/2 + 78, 79, 160)
javaShots = [pygame.image.load('images/java_this.png'), pygame.image.load('images/java_abstract.png'),
             pygame.image.load('images/java_final.png'), pygame.image.load('images/java_hash.png')]
javaCount = 0
haskellCount = 0
haskellShots = [pygame.image.load('images/bullet_concat.png'), pygame.image.load('images/bullet_curry.png'), pygame.image.load('images/bullet_define.png'), pygame.image.load('images/bullet_filter.png'), pygame.image.load(
    'images/bullet_flip.png'), pygame.image.load('images/bullet_fold.png'), pygame.image.load('images/bullet_map.png'), pygame.image.load('images/bullet_scan.png'), pygame.image.load('images/bullet_uncurry.png')]
weapon = 'Java'
enterredBossRoom = False
enteredSecret = False
hitAnimations = []
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
    if player_rect.x >= (3000 - 630) * 3 / 2 and player_rect.y >= 860 * 3 / 2 and not enterredBossRoom :
        enterredBossRoom = True
        tony.visible = True
        game_map = game_map2
        weapon = 'Haskell'
        # pygame.mixer.music.unload()
        if(enteredSecret):
            pygame.mixer.music.load("sounds/tony_fight_music.mp3")
            pygame.mixer.music.play(-1)
    if player_rect.x <= 640 * 3 / 2 and player_rect.y >= (860-100) * 3 / 2 and not enteredSecret:
        enteredSecret = True
        game_map = game_map3

    for layer in game_map:
        x = 0
        for tile in layer:
            if tile == '1':
                display.blit(dirt_img, (x*TILE_SIZE-scroll[0], y*TILE_SIZE-scroll[1]))
            if tile == '2':
                display.blit(Carpet_Floor, (x*TILE_SIZE-scroll[0], y*TILE_SIZE-scroll[1]))
            if tile == '3':
                if computerCount//50 == 0:
                    Computer = Computer1
                elif computerCount//50 == 1:
                    Computer = Computer2
                elif computerCount // 50 == 2:
                    Computer = Computer3
                elif computerCount//50 == 3:
                    Computer = Computer4
                display.blit(Computer, (x*TILE_SIZE-scroll[0], y*TILE_SIZE-scroll[1]))

                computerCount += 1
                if computerCount + 1 >= 200:
                    computerCount = 0
            if tile == '4':
                display.blit(CeilingLight, (x*TILE_SIZE-scroll[0], y*TILE_SIZE-scroll[1]))
            if tile == '5':
                display.blit(CeilingNoLight, (x*TILE_SIZE-scroll[0], y*TILE_SIZE-scroll[1]))
            if tile == '6':
                display.blit(Roof, (x*TILE_SIZE-scroll[0], y*TILE_SIZE-scroll[1]))
            if tile == '7':
                display.blit(WallLeftInner, (x*TILE_SIZE-scroll[0], y*TILE_SIZE-scroll[1]))
            if tile == '8':
                display.blit(WallLeftOuter, (x*TILE_SIZE-scroll[0], y*TILE_SIZE-scroll[1]))
            if tile == '9':
                display.blit(WallRightInner, (x*TILE_SIZE-scroll[0], y*TILE_SIZE-scroll[1]))
            if tile == 'a':
                display.blit(WallRightOuter, (x*TILE_SIZE-scroll[0], y*TILE_SIZE-scroll[1]))
            if tile == 'b':
                display.blit(Window, (x*TILE_SIZE-scroll[0], y*TILE_SIZE-scroll[1]))
            if tile == 'c':
                display.blit(Carpet_Left, (x*TILE_SIZE-scroll[0], y*TILE_SIZE-scroll[1]))
            if tile == 'd':
                display.blit(Carpet_Right, (x*TILE_SIZE-scroll[0], y*TILE_SIZE-scroll[1]))
            if tile == 'e':
                display.blit(CeilingLeftTop, (x*TILE_SIZE-scroll[0], y*TILE_SIZE-scroll[1]))
            if tile == 'f':
                display.blit(CeilingRightTop, (x*TILE_SIZE-scroll[0], y*TILE_SIZE-scroll[1]))
            if tile == 'g':
                display.blit(blackboard_clean, (x*TILE_SIZE-scroll[0], y*TILE_SIZE-scroll[1]))
            if tile == 'h':
                display.blit(blackboard_drawn, (x*TILE_SIZE-scroll[0], y*TILE_SIZE-scroll[1]))
            if tile == 'k':
                display.blit(Konstantinos, (x*TILE_SIZE-scroll[0], y*TILE_SIZE-scroll[1]))
            if tile == 'l':
                display.blit(WallTopLeft, (x*TILE_SIZE-scroll[0], y*TILE_SIZE-scroll[1]))
            if tile == 'm':
                display.blit(WallTopRight, (x*TILE_SIZE-scroll[0], y*TILE_SIZE-scroll[1]))
            if tile == 'n':
                display.blit(WallBotLeft, (x*TILE_SIZE-scroll[0], y*TILE_SIZE-scroll[1]))
            if tile == 'o':
                display.blit(WallBotRight, (x*TILE_SIZE-scroll[0], y*TILE_SIZE-scroll[1]))
            if tile == 'p':
                display.blit(WallBottom, (x*TILE_SIZE-scroll[0], y*TILE_SIZE-scroll[1]))
            if tile == 'q':
                display.blit(ICHack, (x*TILE_SIZE-scroll[0], y*TILE_SIZE-scroll[1]))
            if tile == 'r':
                display.blit(ICCrest, (x*TILE_SIZE-scroll[0], y*TILE_SIZE-scroll[1]))
            if tile == 's':
                display.blit(haskellLogo, (x*TILE_SIZE-scroll[0], y*TILE_SIZE-scroll[1]))
            if tile == 'i':
                if phoneBoyCount//100 == 0:
                    phoneBoy = phoneBoy1
                elif computerCount//100 == 1:
                    phoneBoy = phoneBoy2
                display.blit(phoneBoy, (x*TILE_SIZE-scroll[0], y*TILE_SIZE-scroll[1]))

                phoneBoyCount += 1
                if phoneBoyCount + 1 >= 200:
                    phoneBoyCount = 0
            if tile == '?':
                display.blit(Mystical, (x*TILE_SIZE-scroll[0], y*TILE_SIZE-scroll[1]))
            if tile != '0' and tile != 'g' and tile != 'h' and tile != 'i' and tile != 'k' and tile != 'r' and tile != 's' and tile != 'q':
                tile_rects.append(pygame.Rect(x*TILE_SIZE, y*TILE_SIZE, TILE_SIZE, TILE_SIZE))
            x += 1

        y += 1
    # -- player movement
    player_movement = [0, 0]
    if moving_right:
        player_movement[0] += velocity
    if moving_left:
        player_movement[0] -= velocity
    player_movement[1] += gravity
    gravity += 1.5
    if gravity > 12:
        gravity = 12
    # --

    player_rect, collisions = move(player_rect, player_movement, tile_rects)

    if collisions['bottom'] == True:
        air_timer = 0
        gravity = 0
    else:
        air_timer += 1

    # draw player
    if walkCount + 1 >= 32:  # 4 * 8
        walkCount = 0

    if wasRight:
        display.blit(walkRight[walkCount//8], (player_rect.x -
                                               scroll[0], player_rect.y - scroll[1]))
    # display.blit(player_img, (player_rect.x - scroll[0], player_rect.y - scroll[1]))
    elif wasLeft:
        display.blit(walkLeft[walkCount//8], (player_rect.x - scroll[0], player_rect.y - scroll[1]))
    else:
        display.blit(noWalkPlayer, (player_rect.x - scroll[0], player_rect.y - scroll[1]))

    # draw tony
    tony.draw(display)

    # draw bullets
    if shootLoop > 0:
        shootLoop += 1
    if shootLoop > 10:
        shootLoop = 0

    if shooting and shootLoop == 0:
        bulletSound.play()
        if wasLeft:
            facing = -1
        else:
            facing = 1

        if weapon == 'Java':
            bullets.append(projectile(player_rect.x, player_rect.y,
                                      facing, javaShots[javaCount], 1))
            javaCount += 1
            if javaCount == len(javaShots):
                javaCount = 0
        if weapon == 'Haskell':
            bullets.append(projectile(player_rect.x, player_rect.y,
                                      facing, haskellShots[haskellCount], 2))
            haskellCount += 1
            if haskellCount == len(javaShots):
                haskellCount = 0

        shootLoop = 1  # to get out of zero state

    toRemove = []
    for bullet in bullets:
        bullet_img = bullet.image
        bullet_rect = pygame.Rect(round(bullet.x),
                                  round(bullet.y),
                                  bullet_img.get_width(),
                                  bullet_img.get_height())

        # wall collision
        hits = collision_test(bullet_rect, tile_rects)
        print(str(hits))
        bullet.draw(display)
        if hits:
            toRemove.append(bullet)

        tony_rect = pygame.Rect(tony.x, tony.y, tony.width, tony.height)
        tonyhits = collision_test(bullet_rect, [tony_rect])
        if tonyhits and tony.visible:

            hitSound.play()
            tony.hit(bullet.damage)
            toRemove.append(bullet)

            #play animation

            hitAnimations.append(animation(bullet.x, bullet.y))

    for hitAnimation in hitAnimations:
        hitAnimation.draw()

    enemyRemove = []
    for bullet in enemyBullets:
        bullet_img = bullet.image
        bullet_rect = pygame.Rect(round(bullet.x),
                                  round(bullet.y),
                                  bullet_img.get_width(),
                                  bullet_img.get_height())

        bullet.draw(display)

        tilehits = collision_test(bullet_rect, tile_rects)
        if tilehits:
            enemyRemove.append(bullet)

        hits = collision_test(bullet_rect, [player_rect])
        if hits:
            takeDamage()
            enemyRemove.append(bullet)

    for bullet in enemyRemove:
        enemyBullets.pop(enemyBullets.index(bullet))

    for bullet in toRemove:
        bullets.pop(bullets.index(bullet))

    for event in pygame.event.get():  # event loop
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                Pause(display, pygame)
                moving_right = False
                moving_left = False
                wasRight = False
                wasLeft = False
            if event.key == K_RIGHT:
                moving_right = True
                wasRight = True
                wasLeft = False
            if event.key == K_LEFT:
                moving_left = True
                wasRight = False
                wasLeft = True
            if event.key == K_UP:
                if air_timer < 6:
                    gravity = -22
            if event.key == K_SPACE:
                shooting = True

        if event.type == KEYUP:
            if event.key == K_RIGHT:
                moving_right = False
            if event.key == K_LEFT:
                moving_left = False
            if event.key == K_SPACE:
                shooting = False
            if event.key == K_q:
                if weapon == 'Java':
                    weapon = 'Haskell'
                elif weapon == 'Haskell':
                    weapon = 'Java'

    # screen.blit(pygame.transform.scale(display, WINDOW_SIZE), (0, 0))
    pygame.display.update()
    clock.tick(60)
