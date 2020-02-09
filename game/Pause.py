from Colours import col


def Pause(display, pg):
    """Pause function."""
    resume = False
    title_font = pg.font.SysFont("papyrus", 65)
    title_text = title_font.render("PAUSED", 1, col.RED.value)
    enter_font = pg.font.SysFont("papyrus", 40)
    enter_text = enter_font.render("Press enter to resume", 1, col.BLUE.value)
    display.fill(col.BLACK.value)
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
