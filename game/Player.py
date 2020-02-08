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

        # set player defaults
        self.velocity = 4
        self.floor = False
        self.isJump = False
        self.gravity = 9
        self.jumpCount = self.gravity
        self.topCol = False
        self.leftCol = False
        self.rightCol = False
        self.walkRight = [pg.transform.scale(pg.image.load('images/mainAvatar_Right1.png'), (self.width, self.height)),pg.transform.scale(pg.image.load('images/mainAvatar_RightJump1.png'),(self.width, self.height)), pg.transform.scale(pg.image.load('images/mainAvatar_Right2.png'), (self.width, self.height)) ,pg.transform.scale(pg.image.load('images/mainAvatar_RightJump2.png'), (self.width, self.height))]
        self.walkLeft = [pg.transform.scale(pg.image.load('images/mainAvatar_Left1.png'), (self.width, self.height)),pg.transform.scale(pg.image.load('images/mainAvatar_LeftJump1.png'), (self.width, self.height)),pg.transform.scale(pg.image.load('images/mainAvatar_Left2.png'), (self.width, self.height)),pg.transform.scale(pg.image.load('images/mainAvatar_LeftJump1.png'),(self.width, self.height))]
        self.walkCount = 0
        self.left = False
        self.right = False
        self.standing = True
        self.rightJump = False
        self.leftJump = False

    def draw(self, display):
        """Draw the player."""
        if self.walkCount + 1 >= 40:
            self.walkCount = 0

        if not(self.standing):
            if self.left:
                display.blit(self.walkLeft[self.walkCount//10], (self.x, self.y))
                self.walkCount += 1
            elif self.right:
                display.blit(self.walkRight[self.walkCount//10], (self.x, self.y))
                self.walkCount += 1

        else:
            if self.right:
                display.blit(self.walkRight[0], (self.x, self.y))
            else:
                display.blit(self.walkLeft[0], (self.x, self.y))


    def setVelocity(self, velocity):
        """Set the velocity of the player."""
        self.velocity = velocity

    def moveLeft(self):
        """Move the player left."""
        if self.x > 0:
            self.x -= self.velocity
        self.right = False
        self.left = True
        self.standing = False

    def moveRight(self, max):
        """Move the player right."""
        if self.x + self.width < max:
            self.x += self.velocity
        self.right = True
        self.left = False
        self.standing = False

    def setFloor(self, floor):
        """Set floor to true or false."""
        self.floor = floor

    def setTopCol(self, col):
        """Set topCol."""
        self.topCol = col

    def setRightCol(self, col):
        """Set rightCol."""
        self.rightCol = col

    def setLeftCol(self, col):
        """Set leftCol."""
        self.leftCol = col

    def fall(self, max, gravity):
        """Make the player fall."""
        if not self.floor:
            self.y += 10

    def jump(self):
        if self.isJump:
            if self.jumpCount >= -self.gravity:
                if self.jumpCount < 0:  # going downwards
                    if not(self.floor):
                        self.y -= (self.jumpCount ** 2) * 0.5 * -1
                    else:  # reset stuff if hits floor
                        self.resetJump()
                else: ## going upwards
                    if not(self.topCol):
                        self.y -= (self.jumpCount ** 2) * 0.5 * 1
                    else:
                        self.resetJump()
                self.jumpCount -= 0.5
            else:
                self.resetJump()
        else:
            self.isJump = True
            if self.right:
                self.rightJump = True
            elif self.left:
                self.leftJump = True
            self.walkCount = 0
            # right, left walkcount sets

    def resetJump(self):
        self.isJump = False
        self.jumpCount = self.gravity
