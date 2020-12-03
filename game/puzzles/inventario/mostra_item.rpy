screen mostra_item(img="#000"):
    #modal True

    sensitive(not renpy.get_screen("say"))

    frame:
        background "#b3b3b380"
        xalign 0.0
        yalign 0.0
        xsize 1280
        ysize 720

    frame:
        background "#b9503c"
        xsize 450
        ysize 450
        xalign 0.5
        yalign 0.2
        frame:
            background "#d6b377"
            xsize 440
            ysize 440
            at truecenter
            add img maxsize (420, 420) at truecenter

    #key "mousedown_1" action Return()
