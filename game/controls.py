from button import button


def controls(display, pg):

    back1 = pg.image.load("images/oback1.png")
    back2 = pg.image.load("images/oback2.png")

    backButton = button(pg, back1, display.get_width() // 2 + 250,
                        display.get_height()//2 - 300, 150, 80)
    background = pg.image.load("images/escape_from_huxley_open.png")
    background = pg.transform.scale(background, (display.get_width(), display.get_height()))
    display.blit(background, (0, 0))

    exit = False
    while not exit:

        backButton.draw(display)
        pg.display.update()

        keys = pg.key.get_pressed()

        if keys[pg.K_RETURN]:
            exit = True

        pos = pg.mouse.get_pos()

        # code to exit the window.
        for event in pg.event.get():
            if event.type == pg.QUIT:
                quit()
            if event.type == pg.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if backButton.isOver(pos):
                        exit = True
            if event.type == pg.MOUSEMOTION:
                if backButton.isOver(pos):
                    backButton.image = back2
                else:
                    backButton.image = back1
