#CHAMA A TELA DE UM SLIDER PUZZLE 3X3

label SLIDER_PUZZLE_3X3_DIA02:

    #Variáveis que precisam ser determinadas antes de chamar a tela:
    python:
        #Teremos 8 peças
        slp_fim = False
        #Define o tamanho das peças
        slp_tam_peca = 200
        #Define as imagens das peças
        slp_img_pecas = ["images/teste/puzzle/9.png", "images/teste/puzzle/8.png", "images/teste/puzzle/7.png",
                         "images/teste/puzzle/6.png", "images/teste/puzzle/5.png", "images/teste/puzzle/4.png",
                         "images/teste/puzzle/3.png", "images/teste/puzzle/2.png", "images/teste/puzzle/1.png"]
        slp_configuracoes = [
           [[2, 2], [0, 1], [2, 1],
            [1, 1], [0, 0], [1, 0],
            [1, 2], [2, 0], [0, 2]]
        ]

        #[0, 0], [1, 0], [2, 0], [0, 1], [1, 1], [2, 1], [0, 2], [1, 2], [2, 2]
        #0       1       2       3       4       5       6       7       8

        slp_peca_faltante = [0, 2]
        slp_pecas = renpy.random.choice(slp_configuracoes)

    call screen slider_puzzle(dim=3) with dissolve
    return
