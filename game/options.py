from Colours import col
from button import button


def options(display, pg):
    """Options function."""
    exit = False
    music1 = pg.image.load("images/omusic1.png")
    music2 = pg.image.load("images/omusic2.png")
    sound1 = pg.image.load("images/osfx1.png")
    sound2 = pg.image.load("images/osfx2.png")
    back1 = pg.image.load("images/oback1.png")
    back2 = pg.image.load("images/oback2.png")
    musicButton = button(pg, music1, display.get_width() // 2 - 350,
                         display.get_height()//2 + 150, 380, 150)
    soundButton = button(pg, sound1, display.get_width() // 2 + 50,
                         display.get_height()//2 + 150, 380, 150)
    backButton = button(pg, back1, display.get_width() // 2 + 250,
                        display.get_height()//2 - 300, 150, 80)

    background = pg.image.load("images/options_page.png")
    background = pg.transform.scale(background, (display.get_width(), display.get_height()))
    title_font = pg.font.SysFont("papyrus", 200)
    display.blit(background, (0, 0))

    while not exit:

        musicButton.draw(display)
        soundButton.draw(display)
        backButton.draw(display)

        pg.display.update()

        pos = pg.mouse.get_pos()

        # code to exit the window.
        for event in pg.event.get():
            if event.type == pg.QUIT:
                quit()
            if event.type == pg.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if musicButton.isOver(pos):
                        pass
                    if soundButton.isOver(pos):
                        pass
                    if backButton.isOver(pos):
                        exit = True
            if event.type == pg.MOUSEMOTION:
                if musicButton.isOver(pos):
                    musicButton.image = music2
                else:
                    musicButton.image = music1
                if soundButton.isOver(pos):
                    soundButton.image = sound2
                else:
                    soundButton.image = sound1
                if backButton.isOver(pos):
                    backButton.image = back2
                else:
                    backButton.image = back1
