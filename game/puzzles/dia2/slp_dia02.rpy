default configuracoes_aux = []

#CHAMA A TELA DE UM SLIDER PUZZLE 3X3

label SLIDER_PUZZLE_3X3_DIA02:

    #Variáveis que precisam ser determinadas antes de chamar a tela:
    python:
        #Teremos 8 peças
        slp_fim = False
        #Define o tamanho das peças
        slp_tam_peca = 200
        lop_proximo_do_fim = False
        lop_proximo_do_fim2 = False
        #Define as imagens das peças
        slp_img_pecas = ["images/engler/itens/bilhete_slider/9.png", "images/engler/itens/bilhete_slider/8.png", "images/engler/itens/bilhete_slider/7.png",
                         "images/engler/itens/bilhete_slider/6.png", "images/engler/itens/bilhete_slider/5.png", "images/engler/itens/bilhete_slider/4.png",
                         "images/engler/itens/bilhete_slider/3.png", "images/engler/itens/bilhete_slider/2.png", "images/engler/itens/bilhete_slider/1.png"]

        slp_imagem_final = "images/engler/itens/bilhete.png"

        configuracoes_aux = [
            [5, 6, 8, 2, 4, 3, 9, 7, 1],
            [9, 1, 4, 5, 8, 3, 6, 2, 7],
            [5, 6, 8, 2, 4, 3, 9, 7, 1],
            [6, 4, 7, 5, 3, 1, 8, 9, 2],
            [9, 3, 6, 8, 1, 7, 2, 4, 5]
        ]

        # onde cada peça está no tabuleiro
        slp_configuracoes = [
            [ [2, 2], [0, 1], [2, 1], [1, 1], [0, 0], [1, 0], [1, 2], [2, 0], [0, 2], [0, 2] ],
            [ [2, 2], [0, 1], [2, 1], [1, 1], [0, 0], [1, 0], [1, 2], [2, 0], [0, 2], [0, 2] ],
            [ [2, 2], [0, 1], [2, 1], [1, 1], [0, 0], [1, 0], [1, 2], [2, 0], [0, 2], [0, 2] ],
            [ [2, 2], [0, 1], [2, 1], [1, 1], [0, 0], [1, 0], [1, 2], [2, 0], [0, 2], [0, 2] ],
            [ [2, 2], [0, 1], [2, 1], [1, 1], [0, 0], [1, 0], [1, 2], [2, 0], [0, 2], [0, 2] ]
        ]

        for i in range(len(configuracoes_aux)):
            for j in range(len(configuracoes_aux[i])):
                slp_configuracoes[i][(configuracoes_aux[i][j])-1][0] = j%3
                slp_configuracoes[i][(configuracoes_aux[i][j])-1][1] = int(j/3)
                if(configuracoes_aux[i][j] == 9):
                    slp_configuracoes[i][9][0] = j%3
                    slp_configuracoes[i][9][1] = int(j/3)

        slp_timer_total = 5 * 60.0
        slp_timer_quase = 30.0

        #[0, 0], [1, 0], [2, 0], [0, 1], s[1, 1], [2, 1], [0, 2], [1, 2], [2, 2]
        #0       1       2       3       4       5       6       7       8

        # posição no tabuleiro que está faltando
        slp_pecas = renpy.random.choice(slp_configuracoes)
        slp_peca_faltante = slp_pecas[9]

        slp_sucesso_label = "SUCESSO_SLP_3X3_DIA02"
        slp_game_over_label = "SLP_GAME_OVER_3X3_DIA02"

    play music "audio/musicas/Descobrimento.mp3"
    show screen slider_puzzle(dim=3) with dissolve
    jump POINT_AND_CLICK

label SLP_GAME_OVER_3X3_DIA02:
    stop music fadeout 5.0
    hide screen slider_puzzle with puzzle_transition8
    "Droga, vou tentar novamente..."
    jump SLIDER_PUZZLE_3X3_DIA02

label SUCESSO_SLP_3X3_DIA02:
    stop music fadeout 5.0
    hide screen slider_puzzle with puzzle_transition8
    return
