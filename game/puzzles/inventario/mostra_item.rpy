screen mostra_item(img="#000"):
    modal True

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
            add img maxsize (400, 400) at truecenter

    key "mousedown_1" action Return()
