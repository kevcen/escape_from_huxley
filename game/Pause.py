from Colours import col
from button import button
from options import options


def Pause(display, pg):
    """Pause function."""
    resume = False
    resumeButton = button(pg, col.GREEN.value, display.get_width() // 2 - 550,
                          display.get_height()//2 - 200, 200, 100, "RESUME")
    quitButton = button(pg, col.RED.value, display.get_width() // 2 - 550,
                        display.get_height()//2 + 100, 200, 100, "QUIT")
    optionsButton = button(pg, col.BLUE.value, display.get_width() // 2 - 550,
                           display.get_height()//2 - 50, 200, 100, "OPTIONS")
    background = pg.image.load("images/insideBackground.png")
    background = pg.transform.scale(background, (display.get_width(), display.get_height()))
    title_font = pg.font.SysFont("papyrus", 200)
    title_text = title_font.render("PAUSED", 1, col.RED.value)
    display.blit(background, (0, 0))
    display.blit(title_text, ((display.get_width() -
                               title_text.get_width()) // 2,
                              (display.get_height() - title_text.get_height())
                              // 2))

    while not resume:

        resumeButton.draw(display)
        quitButton.draw(display)
        optionsButton.draw(display)

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
                    if optionsButton.isOver(pos):
                        options(display, pg)
                        display.blit(background, (0, 0))
                        display.blit(title_text, ((display.get_width() -
                                                   title_text.get_width()) // 2,
                                                  (display.get_height() - title_text.get_height())
                                                  // 2))

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
                if optionsButton.isOver(pos):
                    optionsButton.colour = col.DARKBLUE.value
                else:
                    optionsButton.colour = col.BLUE.value
