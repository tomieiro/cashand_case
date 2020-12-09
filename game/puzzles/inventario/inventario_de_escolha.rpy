#TELA DE INVENTARIO DE ESCOLHA: contém todos os itens coletados em um point-and-click
# e funciona como um puzzle onde alguns itens precisam ser coletados, na ordem, para resolvê-lo.

#Gabarito das sequências de itens que devem ser selecionados(identificados pelo ID)
default ide_seq_gabarito = [1, 0]

default ide_itens_no_inventario = []

default ide_aux_count = 0

default ide_aux_item = []

default ide_fim = False

default ide_tempo = 3.0

default ide_item_outro = []

default ide_sensivel = False

default ide_item_mostrado = ""
default ide_descricao = ""

default ide_label_repetir = "IDE_01_ESCOLHE_FRASE"

image ide_img_inventario:
    "images/inventario/inventario4.png"

default ide_label_fim = "IDE_01_FIM"

transform ide_bot_tr:
    maxsize (140, 140)
    xalign 0.5
    yalign 0.5

transform ide_botao_abrir:
    size (50, 250)
    xanchor 0.0
    xpos -5
    yanchor 0.0
    ypos 60

transform ide_botao_sair:
    size (50, 250)
    xanchor 0.0
    xpos 1128
    rotate 180.0
    yanchor 0.0
    ypos 60

transform ide_botao_fechar:
    xanchor 0.0
    yanchor 0.0
    xpos 335
    ypos 60
    size (50, 250)
    #xzoom -1.0

#Usando itens coletados do point-and-click
#Estrutura do item: [string de imagem, string de descrição, boolean que indica se já foi coletado,
#                    ID, boolean que indica se já foi escolhido, label chamada quando o item é escolhido]
screen inventario_de_escolha():

    #Sensível a cliques apenas quando não há diálogo acontecendo
    #sensitive(not renpy.get_screen("say"))
    #sensitive(ide_sensivel)

    key "h" action NullAction()
    key 'mouseup_2' action NullAction()
    key 'noshift_K_h' action NullAction()

    sensitive(  not renpy.get_screen("say") and
                not renpy.get_screen("mostra_item") and
                not renpy.get_screen("mostra_item2") and
                not ide_fim)

    #modal True

    if(ide_fim):
        timer ide_tempo action Jump(ide_label_fim)
        #key "mousedown_1" action Jump("FIM_IDE_TESTE")

    frame:
        background "#b3b3b380"
        xalign 0.0
        yalign 0.0
        xsize 1280
        ysize 720

    imagebutton:
        action Jump(ide_label_repetir)
        auto "images/inventario/refletir_%s.png"
        #idle pac1_img_saida
        at ide_botao_sair
        focus_mask True

    frame:
        yalign 0.0
        xalign 0.0
        xsize 400
        ysize 720
        background "idc_img_inventario"
        #xpadding 0.1
        #ypadding 0.03
        vpgrid:
            rows 4
            cols 2
            xspacing 21
            yspacing 25
            transpose True
            for item in ide_itens_no_inventario:
                frame:
                    background "#d7b883"
                    xsize 155
                    ysize 155
                    imagebutton:
                        idle "#d7b883"
                        hover "#d7c29d"
                        xsize 1.0
                        ysize 1.0
                        action [SetVariable("ide_item_mostrado", item),
                                Jump("MOSTRA_ITEM_INVENTARIO_ESCOLHA")]
                        at truecenter
                    add item[0]:
                        at ide_bot_tr

        imagebutton:
            idle "images/inventario/bg_seta_idle.png"
            at idc_botao_fechar
            #idle "images/teste/exit_but.png"
            action [NullAction()]



label MOSTRA_ITEM_INVENTARIO_ESCOLHA:
    show screen mostra_item2(ide_item_mostrado[0]) with dissolve
    pause 1.0
    $ide_descricao = ide_item_mostrado[1]
    "[ide_descricao]"
    menu:
        "Esta é a pista de que eu preciso?"
        "Sim":
            python:
                ide_sensivel = False
                ide_item_outro = ide_item_mostrado
                renpy.jump(ide_item_mostrado[5])

        "Não":
            hide screen mostra_item2 with dissolve
            jump POINT_AND_CLICK


init python:

    def ide_nao_escolhido(item):
        return (item[4] == False)

    def ide_proximo_correto(item):
        global ide_seq_gabarito
        return (len(ide_seq_gabarito) != 0 and item[3] == ide_seq_gabarito[0])

    def ide_escolheu_item(item):
        global ide_seq_gabarito
        global ide_aux_count
        item[4] = True
        ide_seq_gabarito.pop(0)
        ide_aux_count += 1
