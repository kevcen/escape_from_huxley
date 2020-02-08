class Enemies(object):
    walkRight = ['pygame.image.load('')']
    walkLeft = ['pygame.image.load('')']

    def __init__(self, x, y, width, height, end):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.path = [x, end]
        self.walkCount = 0
        self.velocity = 2
        self.health = 5
        self.visible = True

    def move(self):
        if self.velocity > 0:
            if self.x + self.velocity < self.path[1]:
                self.x += self.velocity
            else:
                self.velocity = self.velocity * -1
                self.walkCount = 0
        else:
            if self.x - self.velocity > self.path[0]:
                self.x += self.velocity
            else:
                self.velocity = self.velocity * -1
                self.walkCount = 0

    def draw(self, display):
        self.move()
        if self.walkCount + 1 >= 33:
            self.walkCount = 0

        if self.velocity > 0:
            display.blit(self.walkRight[self.walkCount // 3], (self.x, self.y))
            self.walkCount += 1
        else:
            display.blit(self.walkLeft[self.walkCount // 3], (self.x, self.y))
            self.walkCount += 1

    def hit(self):
        if self.health > 0:
            self.health -= 1  # to do big weapon
        else:
            self.visible = False
        print('hit')