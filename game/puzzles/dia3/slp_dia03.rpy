#CHAMA A TELA DE UM SLIDER PUZZLE 4X4

label SLIDER_PUZZLE_4X4_DIA03:

    #Variáveis que precisam ser determinadas antes de chamar a tela:
    python:
        #Teremos 8 peças
        slp_fim = False
        #Define o tamanho das peças
        slp_tam_peca = 150
        lop_proximo_do_fim = False
        lop_proximo_do_fim2 = False
        #Define as imagens das peças
        slp_img_pecas = ["images/engler/itens/cofre_slider/row-1-col-1.png", "images/engler/itens/cofre_slider/row-1-col-2.png", "images/engler/itens/cofre_slider/row-1-col-3.png", "images/engler/itens/cofre_slider/row-1-col-4.png",
                         "images/engler/itens/cofre_slider/row-2-col-1.png", "images/engler/itens/cofre_slider/row-2-col-2.png", "images/engler/itens/cofre_slider/row-2-col-3.png", "images/engler/itens/cofre_slider/row-2-col-4.png",
                         "images/engler/itens/cofre_slider/row-3-col-1.png", "images/engler/itens/cofre_slider/row-3-col-2.png", "images/engler/itens/cofre_slider/row-3-col-3.png", "images/engler/itens/cofre_slider/row-3-col-4.png",
                         "images/engler/itens/cofre_slider/row-4-col-1.png", "images/engler/itens/cofre_slider/row-4-col-2.png", "images/engler/itens/cofre_slider/row-4-col-3.png", "images/engler/itens/cofre_slider/row-4-col-4.png"]

        slp_imagem_final = "images/engler/itens/4x4 final.png"

        configuracoes_aux = [
            [16, 1, 9, 3, 13, 5, 4, 2, 12, 6, 8, 11, 10, 15, 7, 14],
            [7, 1, 5, 10, 12, 8, 15, 9, 13, 2, 3, 6, 16, 4, 11, 14],
            [5, 7, 12, 8, 9, 16, 6, 4, 10, 15, 13, 2, 3, 1, 11, 14],
            [5, 4, 11, 7, 12, 8, 14, 15, 1, 6, 16, 2, 9, 3, 10, 13],
            [2, 7, 1, 5, 4, 9, 13, 6, 11, 8, 12, 3, 14, 10, 16, 15],
            [5, 1, 6, 7, 14, 2, 3, 15, 4, 12, 10, 11, 8, 16, 9, 13],
            [15, 3, 4, 16, 10, 8, 2, 9, 5, 12, 6, 11, 14, 13, 7, 1],
            [14, 11, 12, 5, 1, 10, 2, 4, 6, 3, 7, 15, 16, 13, 9, 8],
            [5, 13, 7, 3, 9, 11, 12, 14, 2, 6, 10, 4, 8, 15, 16, 1],
            [14, 3, 11, 12, 8, 16, 13, 1, 6, 2, 4, 7, 5, 10, 9, 15]
        ]

        # onde cada peça está no tabuleiro
        slp_configuracoes = [
            [ [2, 2], [0, 1], [2, 1], [1, 1], [0, 0], [1, 0], [1, 2], [2, 0], [0, 2], [0, 2], [0, 2], [0, 2], [0, 2], [0, 2], [0, 2], [0, 2], [0, 2] ],
            [ [2, 2], [0, 1], [2, 1], [1, 1], [0, 0], [1, 0], [1, 2], [2, 0], [0, 2], [0, 2], [0, 2], [0, 2], [0, 2], [0, 2], [0, 2], [0, 2], [0, 2] ],
            [ [2, 2], [0, 1], [2, 1], [1, 1], [0, 0], [1, 0], [1, 2], [2, 0], [0, 2], [0, 2], [0, 2], [0, 2], [0, 2], [0, 2], [0, 2], [0, 2], [0, 2] ],
            [ [2, 2], [0, 1], [2, 1], [1, 1], [0, 0], [1, 0], [1, 2], [2, 0], [0, 2], [0, 2], [0, 2], [0, 2], [0, 2], [0, 2], [0, 2], [0, 2], [0, 2] ],
            [ [2, 2], [0, 1], [2, 1], [1, 1], [0, 0], [1, 0], [1, 2], [2, 0], [0, 2], [0, 2], [0, 2], [0, 2], [0, 2], [0, 2], [0, 2], [0, 2], [0, 2] ],
            [ [2, 2], [0, 1], [2, 1], [1, 1], [0, 0], [1, 0], [1, 2], [2, 0], [0, 2], [0, 2], [0, 2], [0, 2], [0, 2], [0, 2], [0, 2], [0, 2], [0, 2] ],
            [ [2, 2], [0, 1], [2, 1], [1, 1], [0, 0], [1, 0], [1, 2], [2, 0], [0, 2], [0, 2], [0, 2], [0, 2], [0, 2], [0, 2], [0, 2], [0, 2], [0, 2] ],
            [ [2, 2], [0, 1], [2, 1], [1, 1], [0, 0], [1, 0], [1, 2], [2, 0], [0, 2], [0, 2], [0, 2], [0, 2], [0, 2], [0, 2], [0, 2], [0, 2], [0, 2] ],
            [ [2, 2], [0, 1], [2, 1], [1, 1], [0, 0], [1, 0], [1, 2], [2, 0], [0, 2], [0, 2], [0, 2], [0, 2], [0, 2], [0, 2], [0, 2], [0, 2], [0, 2] ],
            [ [2, 2], [0, 1], [2, 1], [1, 1], [0, 0], [1, 0], [1, 2], [2, 0], [0, 2], [0, 2], [0, 2], [0, 2], [0, 2], [0, 2], [0, 2], [0, 2], [0, 2] ]
        ]

        for i in range(len(configuracoes_aux)):
            for j in range(len(configuracoes_aux[i])):
                slp_configuracoes[i][(configuracoes_aux[i][j])-1][0] = j%4
                slp_configuracoes[i][(configuracoes_aux[i][j])-1][1] = int(j/4)
                if(configuracoes_aux[i][j] == 16):
                    slp_configuracoes[i][16][0] = j%4
                    slp_configuracoes[i][16][1] = int(j/4)

        slp_timer_total = 6 * 60.0
        slp_timer_quase = 60.0

        #[0, 0], [1, 0], [2, 0], [0, 1], s[1, 1], [2, 1], [0, 2], [1, 2], [2, 2]
        #0       1       2       3       4       5       6       7       8

        # posição no tabuleiro que está faltando
        slp_pecas = renpy.random.choice(slp_configuracoes)
        slp_peca_faltante = slp_pecas[16]

        slp_sucesso_label = "SUCESSO_SLP_4X4_DIA03"
        slp_game_over_label = "SLP_GAME_OVER_4X4_DIA03"

    "Ao clicar em uma peça, posso deslizá-la para um espaço vazio."
    "Preciso descobrir o que cada símbolo significa."
    "E posicionar as peças na ordem correta."

    play music "audio/musicas/Descobrimento.mp3"
    show screen slider_puzzle(dim=4, img_bg="#636363", style_margem="slp_margem2", style_fundo="slp_botao_fundo2") with puzzle_transition8
    jump POINT_AND_CLICK

label SLP_GAME_OVER_4X4_DIA03:
    stop music fadeout 5.0
    hide screen slider_puzzle with puzzle_transition8
    "Droga, vou tentar novamente..."
    "Acho que todas as peças representam números."
    "Mas parecem estar em sistemas numéricos diferentes."
    "Acho que cada peça fica na posição correspondente ao seu número..."
    "Talvez se eu alinhasse as peças corretas na primeira linha e depois a primeira coluna, e seguir assim, reduzindo em quadrados menores..."
    "Tenho certeza que resolverei."
    jump SLIDER_PUZZLE_4X4_DIA03

label SUCESSO_SLP_4X4_DIA03:
    stop music fadeout 5.0
    hide screen slider_puzzle with puzzle_transition8
    return

style slp_margem2:
    padding (0, 0)
    #background Solid("#ff9900")
    background "#000"
    xsize 150 * 4
    ysize 150 * 4
    #xalign 0.3
    #yalign 0.3


style slp_botao_fundo2:
    background Solid("#000")
    xsize 150
    ysize 150
