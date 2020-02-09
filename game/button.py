from Colours import col


class button():
    def __init__(self, pg, image, x, y, width, height, text=''):
        self.image = image
        self.x = x
        self.y = y
        self.width = image.get_width()
        self.height = image.get_height()
        self.text = text
        self.pg = pg

    def draw(self, display):
        display.blit(self.image, (self.x, self.y))

        if self.text != '':
            font = self.pg.font.SysFont('comicsans', 60)
            text = font.render(self.text, 1, (0, 0, 0))
            display.blit(text, (self.x + (self.width/2 - text.get_width()/2),
                                self.y + (self.height/2 - text.get_height()/2)))

    def isOver(self, pos):
        # Pos is the mouse position or a tuple of (x,y) coordinates
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                return True

        return False
