default slp_fim = False
default slp_tam_peca = 100
default slp_x = 0.0
default slp_y = 0.0

default slp_img_pecas = ["images/prototipo/tranca/row-1-col-1.png", "images/prototipo/tranca/row-1-col-2.png", "images/prototipo/tranca/row-1-col-3.png",
                         "images/prototipo/tranca/row-2-col-1.png", "images/prototipo/tranca/row-2-col-2.png", "images/prototipo/tranca/row-2-col-3.png",
                         "images/prototipo/tranca/row-3-col-1.png", "images/prototipo/tranca/row-3-col-2.png", "images/prototipo/tranca/row-3-col-3.png"]

# falta a ultima
# determina as coordenadas de cada peça
# slp_pecas[id] = [x, y]
default slp_pecas = [
[0, 0], [1, 0], [2, 0],
[0, 1], [1, 2], [1, 1],
[0, 2], [2, 1], [2, 2], [2, 2]
]

default slp_peca_faltante = [2, 2]

default slp_game_over_label = "SLP_GAME_OVER_3X3_DIA02"

default slp_sucesso_label = "SUCESSO_SLP_3X3_DIA02"

default slp_imagem_final = "images/prototipo/tranca/tranca.png"

default slp_timer_total = 180.0

default slp_timer_quase = 30.0

# no gabarito de um 3x3:
#   slp_pecas[0] = [0, 0],
#   slp_pecas[1] = [1, 0],
#   slp_pecas[4] = [1, 1]
#   ...

transform slp_img_tr(tam=200):
    size (tam, tam)
    xalign 0.5
    yalign 0.5

transform posicao_peca(x, y):
    subpixel True
    linear 0.5 xalign (x*0.5) yalign (y*0.5)


screen slider_puzzle(dim, img_bg = "#fff"):
    modal True

    #Sensível apenas quando o puzzle ainda não acabou
    sensitive (not slp_fim)

    key "h" action NullAction()
    key 'mouseup_2' action NullAction()
    key 'noshift_K_h' action NullAction()

    frame:
        style "slp_tela_cheia"
        background img_bg
        if(not slp_fim):
            add DynamicDisplayable( timer_puzzle,
                                    tempo_total=slp_timer_total,
                                    tempo_troca=slp_timer_quase,
                                    label_fim_tempo = slp_game_over_label,
                                    screen = 'slider_puzzle',
                                    style_ok = 'lop_text_timer_ok',
                                    style_acabando = 'lop_text_timer_acabando',
                                    fim = slp_fim
                                    ) at topright

        frame:
            at truecenter
            style "slp_margem"
            for i in range((dim*dim)-1):
                #if slp_pecas[i][0] != slp_peca_faltante[0] or slp_pecas[i][1] != slp_peca_faltante[1]:
                frame:
                    style "slp_botao_fundo"
                    at posicao_peca(slp_pecas[i][0], slp_pecas[i][1])
                    imagebutton:
                        action [Function(seleciona_e_desliza, slp_pecas[i], slp_peca_faltante),
                                Function(confere_fim_slider_puzzle, slp_pecas, dim),
                                renpy.restart_interaction]
                        idle slp_img_pecas[i]
                        at slp_img_tr(slp_tam_peca)


    if slp_fim:
        #chamar a screen de mostrar a resposta final pra ter um tempinho antes
        add slp_imagem_final maxsize (((slp_tam_peca+10)*3), ((slp_tam_peca+10)*3)) at truecenter
        timer 3.0 action Jump(slp_sucesso_label)


init python:
    def seleciona_e_desliza(coord_ant, coord_nov):
        #Confere se pode deslizar
        if(
            (coord_nov[0] == coord_ant[0] and
                (coord_nov[1] == coord_ant[1]+1 or
                coord_nov[1] == coord_ant[1]-1
                )
            )
            or
            (coord_nov[1] == coord_ant[1] and
                (coord_nov[0] == coord_ant[0]+1 or
                coord_nov[0] == coord_ant[0]-1
                )
            )
        ):
            #Desliza
            renpy.play("audio/sonoplastia/Slider.mp3")
            aux = [0, 0]
            aux[0] = coord_ant[0]
            aux[1] = coord_ant[1]
            coord_ant[0] = coord_nov[0]
            coord_ant[1] = coord_nov[1]
            coord_nov[0] = aux[0]
            coord_nov[1] = aux[1]

    def confere_fim_slider_puzzle(pecas, dim):
        global slp_fim
        for i in range((dim*dim)-1):
            y, x = converte_para_duas_dimensoes(i, dim)
            if (pecas[i][0] != x) or (pecas[i][1] != y):
                return
        slp_fim = True


style slp_tela_cheia:
    background Solid("#000000")
    xsize 1280
    ysize 720

style slp_margem:
    #padding (10, 10)
    #background Solid("#ff9900")
    background "#000"
    xsize 600
    ysize 600

style slp_botao_fundo:
    background Solid("#000")
    xsize 200
    ysize 200
