from Colours import col
from button import button


def Menu(display, pg):
    """Create main menu for the game."""
    play = False
    startButton = button(pg, col.GREEN.value, display.get_width() // 2 - 300,
                         display.get_height()//2 + 150, 180, 100, "PLAY")
    quitButton = button(pg, col.RED.value, display.get_width() // 2 + 100,
                        display.get_height()//2 + 150, 180, 100, "QUIT")
    background = pg.image.load("images/insideBackground.png")
    background = pg.transform.scale(background, (display.get_width(), display.get_height()))
    title_font = pg.font.SysFont("papyrus", 120)
    title_text = title_font.render("ESCAPE FROM HUXLEY", 1, col.RED.value)
    display.blit(background, (0, 0))
    display.blit(title_text, ((display.get_width() -
                               title_text.get_width()) // 2,
                              (display.get_height() - title_text.get_height())
                              // 2 - 100))

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
                    startButton.colour = col.DARKGREEN.value
                else:
                    startButton.colour = col.GREEN.value
                if quitButton.isOver(pos):
                    quitButton.colour = col.DARKRED.value
                else:
                    quitButton.colour = col.RED.value
