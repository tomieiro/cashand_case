#TELA DE INVENTARIO DE COLETA: reserva todos os itens coletados por um point-and-click
#LEMBRAR DE RESETAR O VETOR

default idc_item_mostrado = ""
default idc_descricao = ""

image idc_img_inventario:
    "images/inventario/inventario4.png"
    #xzoom 2.0

transform idc_bot_tr:
    maxsize (120, 120)
    xalign 0.5
    yalign 0.5

transform idc_botao_abrir:
    size (50, 250)
    xanchor 0.0
    xpos -5
    yanchor 0.0
    ypos 60

transform idc_botao_sair:
    size (50, 250)
    xalign 1.108
    rotate 180.0
    yalign 0.1

transform idc_botao_fechar:
    xanchor 0.0
    yanchor 0.0
    xpos 335
    ypos 60
    size (50, 250)
    #xzoom -1.0

transform idc_aparece:
    on show:
        xpos -340
        linear 0.3 xpos 0
    on hide:
        linear 0.3 xpos -340

#itens_no_inventario precisa ter itens na seguinte configuração:
# [string_de_imagem, string_de_descrição, ...]
screen inventario_de_coleta(itens_no_inventario=[]):
    #modal True

    sensitive(  not renpy.get_screen("say") and
                not renpy.get_screen("mostra_item") and
                not renpy.get_screen("mostra_item2")
                )

    frame:
        background "#b3b3b380"
        xalign 0.0
        yalign 0.0
        xsize 1280
        ysize 720
    frame:
        xanchor 0.0
        yanchor 0.0
        at idc_aparece
        xsize 340
        ysize 720
        background "idc_img_inventario"
        #xpadding 0.1
        #ypadding 0.03
        vpgrid:
            #xinitial 0.1
            #yinitial 0.1
            rows 4
            cols 2
            xspacing 21
            yspacing 25
            transpose True
            for item in itens_no_inventario:
                frame:
                    #background "#4d260050"
                    #background "#ffffff50"
                    background "#b33a2e"
                    xsize 155
                    ysize 155
                    imagebutton:
                        idle "#d7b883"
                        hover "#d7c29d"
                        xsize 1.0
                        ysize 1.0
                        action [SetVariable("idc_item_mostrado", item[0]),
                                SetVariable("idc_descricao", item[1]),
                                Jump("MOSTRA_ITEM_INVENTARIO_COLETA")]
                        at truecenter
                    add item[0]:
                        at idc_bot_tr
        imagebutton:
            auto "images/inventario/bg_seta_%s.png"
            #idle pacp_img_inv_but
            at idc_botao_fechar
            action Jump("FECHAR_TELA_INVENTARIO")




label FECHAR_TELA_INVENTARIO:
    hide screen inventario_de_coleta with moveoutleft
    jump POINT_AND_CLICK

label MOSTRA_ITEM_INVENTARIO_COLETA:
    show screen mostra_item2(idc_item_mostrado) with dissolve
    pause 1.0
    "[idc_descricao]"
    hide screen mostra_item2 with dissolve
    jump POINT_AND_CLICK
