screen mostra_item2(img="#000"):
    #modal True

    sensitive(not renpy.get_screen("say"))

    frame:
        background "#b9503c"
        xsize 450
        ysize 450
        xalign 0.75
        yalign 0.2
        frame:
            background "#d6b377"
            xsize 430
            ysize 430
            at truecenter
            add img maxsize (360, 360) at truecenter

    #key "mousedown_1" action Return()
