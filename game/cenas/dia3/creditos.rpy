default crd_tempo = 10.0

screen tela_creditos():

    timer (crd_tempo+3.0) action Return()

    frame:
        xsize 1280
        ysize 720 * 4
        xalign 0.0
        yanchor 0.0
        ypos 720 * 4
        at subindo_tela(crd_tempo)
        text "Cashand Case":
            xalign 0.5
            style "estilo_creditos"

        text "Cashand Case":
            xalign 0.5
            style "estilo_creditos"

        text "Cashand Case":
            xalign 0.5
            style "estilo_creditos"



transform subindo_tela(tempo):
    subpixel True
    linear tempo ypos 0

style estilo_creditos:
    xalign 0.5
    color "#fff"
    size 72
