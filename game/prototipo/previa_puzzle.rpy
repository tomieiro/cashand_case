screen previa_puzzle(img_bg = "images/teste/bg_test.png", img_puzzle = "images/teste/puzzle_idle.png"):

    default bg = im.Scale(img_bg, 1280, 720)
    default puzzle = im.Scale(img_puzzle, 350, 350)

    frame:
        background bg
        xsize 1280
        ysize 720
        add puzzle xalign 0.5 yalign 0.2
