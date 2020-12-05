#CHAMA A TELA DE UM SLIDER PUZZLE 3X3

label SLIDER_PUZZLE_3X3_DIA02_2:

    #Variáveis que precisam ser determinadas antes de chamar a tela:
    python:
        #Teremos 8 peças
        slp_fim = False
        #Define o tamanho das peças
        slp_tam_peca = 200
        lop_proximo_do_fim = False
        lop_proximo_do_fim2 = False
        #Define as imagens das peças
        slp_img_pecas = ["images/engler/itens/gravador_slider/9.png", "images/engler/itens/gravador_slider/8.png", "images/engler/itens/gravador_slider/7.png",
                         "images/engler/itens/gravador_slider/6.png", "images/engler/itens/gravador_slider/5.png", "images/engler/itens/gravador_slider/4.png",
                         "images/engler/itens/gravador_slider/3.png", "images/engler/itens/gravador_slider/2.png", "images/engler/itens/gravador_slider/1.png"]

        slp_imagem_final = "images/engler/itens/trava gravador.png"

        configuracoes_aux = [
            [7, 3, 5, 8, 4, 2, 9, 1, 6],
            [6, 8, 5, 2, 4, 9, 1, 3, 7],
            [6, 3, 7, 5, 9, 8, 4, 2, 1],
            [3, 1, 9, 5, 4, 7, 8, 6, 2],
            [5, 6, 9, 2, 7, 3, 8, 4, 1]
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

        slp_timer_total = 2 * 60.0
        slp_timer_quase = 30.0

        #[0, 0], [1, 0], [2, 0], [0, 1], s[1, 1], [2, 1], [0, 2], [1, 2], [2, 2]
        #0       1       2       3       4       5       6       7       8

        # posição no tabuleiro que está faltando
        slp_pecas = renpy.random.choice(slp_configuracoes)
        slp_peca_faltante = slp_pecas[9]

        slp_sucesso_label = "SUCESSO_SLP_3X3_DIA02_2"
        slp_game_over_label = "SLP_GAME_OVER_3X3_DIA02_2"

    play music "audio/musicas/Descobrimento.mp3"
    show screen slider_puzzle(dim=3, img_bg="#787abf") with dissolve
    jump POINT_AND_CLICK

label SLP_GAME_OVER_3X3_DIA02_2:
    stop music fadeout 5.0
    hide screen slider_puzzle with puzzle_transition8
    "Droga, vou tentar novamente..."
    jump SLIDER_PUZZLE_3X3_DIA02_2

label SUCESSO_SLP_3X3_DIA02_2:
    stop music fadeout 5.0
    hide screen slider_puzzle with puzzle_transition8
    return
