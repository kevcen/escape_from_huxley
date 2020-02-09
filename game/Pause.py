from Colours import col


def Pause(display, pg):
    """Pause function."""
    resume = False
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
    pg.display.update()

    while not resume:

        keys = pg.key.get_pressed()

        if keys[pg.K_RETURN]:
            resume = True

        # code to exit the window.
        for event in pg.event.get():
            if event.type == pg.QUIT:
                quit()
