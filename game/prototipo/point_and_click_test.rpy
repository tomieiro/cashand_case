style fundo_tela:
    xsize 1280
    ysize 720


screen point_and_click_test():

    window:
        style "fundo_tela"
        background "#fff"

        imagebutton:
            action Call("LIGHTS_OUT_TEST")
            auto "images/teste/dogbutton_%s.jpg"
            focus_mask True
            at truecenter
