from Colours import col
from button import button


def Menu(display, pg):
    """Create main menu for the game."""
    play1 = pg.image.load("images/play1.png")
    play2 = pg.image.load("images/play2.png")
    quit1 = pg.image.load("images/quit1.png")
    quit2 = pg.image.load("images/quit2.png")

    play = False
    startButton = button(pg, play1, display.get_width() // 2 - 350,
                         display.get_height()//2 + 150, 180, 100)
    quitButton = button(pg, quit1, display.get_width() // 2 + 100,
                        display.get_height()//2 + 150, 180, 100)
    background = pg.image.load("images/escape_from_huxley_open.png")
    background = pg.transform.scale(background, (display.get_width(), display.get_height()))
    title_font = pg.font.SysFont("papyrus", 120)
    display.blit(background, (0, 0))

    while not play:

        startButton.draw(display)
        quitButton.draw(display)

        pg.display.update()

        keys = pg.key.get_pressed()

        if keys[pg.K_RETURN]:
            play = True

        pos = pg.mouse.get_pos()

        # code to exit the window.
        for event in pg.event.get():
            if event.type == pg.QUIT:
                quit()
            if event.type == pg.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if startButton.isOver(pos):
                        play = True
                    if quitButton.isOver(pos):
                        quit()
            if event.type == pg.MOUSEMOTION:
                if startButton.isOver(pos):
                    startButton.image = play2
                else:
                    startButton.image = play1
                if quitButton.isOver(pos):
                    quitButton.image = quit2
                else:
                    quitButton.image = quit1
