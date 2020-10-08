image img_bg = "images/teste/bg_test.png"
define img_puzzle = "images/teste/puzzle_%s.png"
define img_estante = "images/teste/estante_%s.png"
define img_copo = "images/teste/water_%s.png"
define img_copo_idle = "images/teste/water_idle.png"

style fundo_tela:
    xsize 1280
    ysize 720

screen point_and_click_test():

    window:
        background "img_bg"
        style "fundo_tela"

        imagebutton:
            action Jump("LIGHTS_OUT_TEST")
            auto img_puzzle
            focus_mask True
            xalign 0.8
            yalign 0.3

        imagebutton:
            action Jump("SELECIONA_ESTANTE")
            auto img_estante
            focus_mask True
            xalign 0.30
            yalign 0.50

        imagebutton:
            action Jump("SELECIONA_COPO")
            auto img_copo
            focus_mask True
            xalign 0.33
            yalign 0.24


label SELECIONA_ESTANTE:
    "É só uma estante normal"
    jump PUZZLE_TESTE

label SELECIONA_COPO:
    show screen mostra_item(img_copo_idle) with dissolve
    pause 0.3
    "Apenas um copo comum"
    hide screen mostra_item with dissolve
    jump PUZZLE_TESTE
