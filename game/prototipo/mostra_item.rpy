screen mostra_item(img = "#000"):
    modal True

    default item = im.Scale(img, 200, 400)

    frame:
        background "#000"
        xsize 450
        ysize 450
        xalign 0.5
        yalign 0.2
        frame:
            background "#fff"
            xsize 440
            ysize 440
            at truecenter
            add item at truecenter

    key "mousedown_1" action Return()
    #timer 3.0 action Return()
