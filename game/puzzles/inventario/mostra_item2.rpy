screen mostra_item2(img="#000"):
    #modal True

    key "h" action NullAction()
    key 'mouseup_2' action NullAction()
    key 'noshift_K_h' action NullAction()

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
        xalign 0.75
        yalign 0.2
        frame:
            background "#d6b377"
            xsize 440
            ysize 440
            at truecenter
            add img maxsize (420, 420) at truecenter

    #key "mousedown_1" action Return()
