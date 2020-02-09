from Colours import col
from button import button


def Pause(display, pg):
    """Pause function."""
    resume = False
    resumeButton = button(pg, col.GREEN.value, display.get_width() // 2 - 300,
                          display.get_height()//2 + 150, 180, 100, "RESUME")
    quitButton = button(pg, col.RED.value, display.get_width() // 2 + 100,
                        display.get_height()//2 + 150, 180, 100, "QUIT")
    background = pg.image.load("images/insideBackground.png")
    background = pg.transform.scale(background, (display.get_width(), display.get_height()))
    title_font = pg.font.SysFont("papyrus", 180)
    title_text = title_font.render("PAUSED", 1, col.RED.value)
    enter_font = pg.font.SysFont("papyrus", 120)
    enter_text = enter_font.render("Press enter to resume", 1, col.BLUE.value)
    display.blit(background, (0, 0))
    display.blit(title_text, ((display.get_width() -
                               title_text.get_width()) // 2,
                              (display.get_height() - title_text.get_height())
                              // 2 - 100))

    display.blit(enter_text, ((display.get_width() -
                               enter_text.get_width()) // 2,
                              (display.get_height() - enter_text.get_height())
                              // 2))

    while not resume:

        resumeButton.draw(display)
        quitButton.draw(display)

        pg.display.update()

        keys = pg.key.get_pressed()

        if keys[pg.K_RETURN]:
            resume = True

        pos = pg.mouse.get_pos()

        # code to exit the window.
        for event in pg.event.get():
            if event.type == pg.QUIT:
                quit()
            if event.type == pg.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if resumeButton.isOver(pos):
                        resume = True
                    if quitButton.isOver(pos):
                        quit()
            if event.type == pg.MOUSEMOTION:
                if resumeButton.isOver(pos):
                    resumeButton.colour = col.DARKGREEN.value
                else:
                    resumeButton.colour = col.GREEN.value
                if quitButton.isOver(pos):
                    quitButton.colour = col.DARKRED.value
                else:
                    quitButton.colour = col.RED.value
