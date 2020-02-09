from button import button
from options import options


def Pause(display, pg, sounds):
    """Pause function."""
    resume1 = pg.image.load("images/presume1.png")
    resume2 = pg.image.load("images/presume2.png")
    quit1 = pg.image.load("images/pquit1.png")
    quit2 = pg.image.load("images/pquit2.png")
    options1 = pg.image.load("images/poptions1.png")
    options2 = pg.image.load("images/poptions2.png")

    resume = False
    resumeButton = button(pg, resume1, display.get_width() // 2 - 550,
                          display.get_height()//2 - 200, 200, 100)
    quitButton = button(pg, quit1, display.get_width() // 2 - 550,
                        display.get_height()//2 + 100, 200, 100)
    optionsButton = button(pg, options1, display.get_width() // 2 - 550,
                           display.get_height()//2 - 50, 200, 100)
    background = pg.image.load("images/game_paused.png")
    background = pg.transform.scale(background, (display.get_width(), display.get_height()))
    display.blit(background, (0, 0))

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
                        options(display, pg, sounds)
                        display.blit(background, (0, 0))
                        optionsButton.image = options1
                    if quitButton.isOver(pos):
                        quit()

            if event.type == pg.MOUSEMOTION:
                if resumeButton.isOver(pos):
                    resumeButton.image = resume2
                else:
                    resumeButton.image = resume1
                if quitButton.isOver(pos):
                    quitButton.image = quit2
                else:
                    quitButton.image = quit1
                if optionsButton.isOver(pos):
                    optionsButton.image = options2
                else:
                    optionsButton.image = options1
