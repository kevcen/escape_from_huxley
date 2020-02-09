from button import button

music_playing = True
sfx_playing = True


def options(display, pg, sounds):
    """Options function."""
    global music_playing
    global sfx_playing
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
                        if music_playing:
                            pg.mixer.music.pause()
                        else:
                            pg.mixer.music.unpause()
                        music_playing = not music_playing
                    if soundButton.isOver(pos):
                        if sfx_playing:
                            for sound in sounds:
                                sound.set_volume(0)
                        else:
                            for sound in sounds:
                                sound.set_volume(1)
                        sfx_playing = not sfx_playing
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


def music():
    return music_playing


def sfx():
    return sfx_playing
