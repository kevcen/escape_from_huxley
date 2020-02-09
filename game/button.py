from Colours import col


class button():
    def __init__(self, pg, colour, x, y, width, height, text=''):
        self.colour = colour
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.pg = pg

    def draw(self, display, outline=None):
        # Call this method to draw the button on the screen
        if outline:
            self.pg.draw.rect(display, outline, (self.x-2, self.y -
                                                 2, self.width+4, self.height+4), 0)

        self.pg.draw.rect(display, self.colour, (self.x, self.y, self.width, self.height), 0)

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
