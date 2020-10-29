define img_puzzle = "images/teste/puzzle_%s.png"
define img_estante = "images/teste/estante_%s.png"
define img_copo = "images/teste/water_%s.png"
define img_inv_but = "images/teste/inv_but_%s.png"

define img_copo_idle = "images/teste/water_idle.png"
define img_cookie = "images/teste/cookie.png"

style fundo_tela:
    xsize 1280
    ysize 720

default copo_selecionado = False
default cookie_selecionado = False

screen point_and_click_test():

    sensitive(not renpy.get_screen("say"))

    frame:
        background "img_bg"
        style "fundo_tela"

        imagebutton:
            action Jump("SLIDER_TEST")
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

        if(not copo_selecionado):
            imagebutton:
                action Jump("SELECIONA_COPO")
                auto img_copo
                focus_mask True
                xalign 0.33
                yalign 0.24

        imagebutton:
            action Show("tela_de_inventario")
            auto img_inv_but
            xalign 0.0
            yalign 0.0


label SELECIONA_ESTANTE:
    if(not cookie_selecionado):
        show sheppard neutro onlayer screens at center with dissolve
        shp "Quer investigar esse criado mudo?"
        drc "Será que há algum item nele?"
        drc "Olha só!"
        $renpy.notify("Coletou cookie!")
        show screen mostra_item(img_cookie) with dissolve
        pause 0.3
        "Minha barriga estava roncando agora a pouco. Este cookie pode ser útil..."
        $cookie_selecionado = True
        $itens_no_inventario.append(img_cookie)
        hide screen mostra_item with dissolve
        shp "Mas eu tava deixando pra mais tar..."
        drc "Delicioso!"
        drc "O que? o senhor disse algo?"
        shp "Ah, deixa pra lá..."
        hide sheppard onlayer screens with dissolve
    else:
        "Acho que não há mais nada que eu possa pegar por aqui..."
        show sheppard neutro onlayer screens at center with dissolve
        shp "Ufa, ainda bem que ele não viu o burrito..."
        drc "Disse alguma coisa?"
        shp "Não, nada..."
        drc "Ok..."
        hide sheppard onlayer screens with dissolve
    jump PUZZLE_TESTE

label SELECIONA_COPO:
    $renpy.notify("Coletou copo com água!")
    show screen mostra_item(img_copo_idle) with dissolve
    pause 0.3
    "Estou com sede, acho que este copo pode ser útil!"
    $copo_selecionado = True
    $itens_no_inventario.append(img_copo_idle)
    hide screen mostra_item with dissolve
    jump PUZZLE_TESTE
