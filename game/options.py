from Colours import col
from button import button


def options(display, pg):
    """Options function."""
    exit = False
    musicButton = button(pg, col.BLUE.value, display.get_width() // 2 - 420,
                         display.get_height()//2 + 150, 380, 150, "MUSIC")
    soundButton = button(pg, col.BLUE.value, display.get_width() // 2 + 20,
                         display.get_height()//2 + 150, 380, 150, "SOUND EFFECTS")
    backButton = button(pg, col.RED.value, display.get_width() // 2 + 400,
                        display.get_height()//2 - 300, 150, 80, "BACK")

    background = pg.image.load("images/insideBackground.png")
    background = pg.transform.scale(background, (display.get_width(), display.get_height()))
    title_font = pg.font.SysFont("papyrus", 200)
    title_text = title_font.render("OPTIONS", 1, col.RED.value)
    display.blit(background, (0, 0))
    display.blit(title_text, ((display.get_width() -
                               title_text.get_width()) // 2,
                              (display.get_height() - title_text.get_height())
                              // 2))

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
                        options(display, pg)
                    if backButton.isOver(pos):
                        exit = True
            if event.type == pg.MOUSEMOTION:
                if musicButton.isOver(pos):
                    musicButton.colour = col.DARKBLUE.value
                else:
                    musicButton.colour = col.BLUE.value
                if soundButton.isOver(pos):
                    soundButton.colour = col.DARKBLUE.value
                else:
                    soundButton.colour = col.BLUE.value
                if backButton.isOver(pos):
                    backButton.colour = col.DARKRED.value
                else:
                    backButton.colour = col.RED.value
