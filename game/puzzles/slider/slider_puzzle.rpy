default slp_fim = False
default slp_tam_peca = 200
default slp_x = 0.0
default slp_y = 0.0

default slp_img_pecas = ["images/teste/puzzle/9.png", "images/teste/puzzle/8.png", "images/teste/puzzle/7.png",
                         "images/teste/puzzle/6.png", "images/teste/puzzle/5.png", "images/teste/puzzle/4.png",
                         "images/teste/puzzle/3.png", "images/teste/puzzle/2.png", "images/teste/puzzle/1.png"]

#falta a ultima
# slp_pecas[id] = [x, y, img]
default slp_pecas = [
[1, 2, "images/teste/puzzle/9.png"],
[0, 2, "images/teste/puzzle/8.png"],
[2, 0, "images/teste/puzzle/7.png"],
[0, 1, "images/teste/puzzle/6.png"],
[1, 1, "images/teste/puzzle/5.png"],
[2, 1, "images/teste/puzzle/4.png"],
[1, 0, "images/teste/puzzle/3.png"],
[0, 0, "images/teste/puzzle/2.png"]
]

default slp_peca_faltante = [2, 2]

# no gabarito de um 3x3:
#   slp_pecas[0] = [0, 0, ...],
#   slp_pecas[1] = [1, 0, ...],
#   slp_pecas[4] = [1, 1, ...]
#   ...

transform slp_img_tr:
    size (200, 200)
    xalign 0.5
    yalign 0.5

init python:
    def slide_function(trans, st, at):
        if st > 1.0:
            trans.xalign = 1.0
            return None
        else:
            trans.xalign = st
            return 0

transform posicao_peca(x, y):
    subpixel True
    linear 0.5 xalign (x*0.5) yalign (y*0.5)

screen slider_puzzle(dim,
img_bg = "#fff"):

    modal True

    sensitive (not slp_fim)

    frame:
        style "slp_tela_cheia"
        background img_bg
        frame:
            at truecenter
            style "slp_margem"
            for i in range(8):
                frame:
                    style "slp_botao_fundo"
                    at posicao_peca(slp_pecas[i][0], slp_pecas[i][1])
                    imagebutton:
                        action [Function(seleciona_e_desliza, slp_pecas[i], slp_peca_faltante),
                                Function(confere_fim_slider_puzzle, slp_pecas),
                                renpy.restart_interaction]
                        idle lop_img_pecas[i]
                        at slp_img_tr


    if slp_fim:
        #chamar a screen de mostrar a resposta final pra ter um tempinho antes
        add "images/teste/puzzle/cc.png" maxsize (630, 630) at truecenter
        timer 3.0 action Return()


init python:
    def seleciona_e_desliza(coord_ant, coord_nov):
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
            aux = [0, 0]
            aux[0] = coord_ant[0]
            aux[1] = coord_ant[1]
            coord_ant[0] = coord_nov[0]
            coord_ant[1] = coord_nov[1]
            coord_nov[0] = aux[0]
            coord_nov[1] = aux[1]

    def confere_fim_slider_puzzle(pecas):
        global slp_fim
        for i in range(8):
            y, x = converte_para_duas_dimensoes(i, 3)
            if (pecas[i][0] != x) or (pecas[i][1] != y):
                return
        slp_fim = True


style slp_tela_cheia:
    background Solid("#000000")
    xsize 1280
    ysize 720

style slp_margem:
    #padding (10, 10)
    background Solid("#ff9900")
    xsize 600
    ysize 600

style slp_botao_fundo:
    background Solid("#fff")
    xsize 200
    ysize 200
