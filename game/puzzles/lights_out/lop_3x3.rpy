#CHAMA A TELA DE UM LIGHTS_OUT PUZZLE 3X3

label LIGHTS_OUT_PUZZLE_3X3:

    #Variáveis que precisam ser determinadas antes de chamar a tela:
    python:
        #Teremos 9 peças
        lop_fim = False
        lop_pecas = [False] * 9
        #Define o tamanho das peças
        lop_tam_peca = 200
        #Define as imagens das peças
        lop_img_pecas = ["images/teste/puzzle/9.png", "images/teste/puzzle/8.png", "images/teste/puzzle/7.png",
                         "images/teste/puzzle/6.png", "images/teste/puzzle/5.png", "images/teste/puzzle/4.png",
                         "images/teste/puzzle/3.png", "images/teste/puzzle/2.png", "images/teste/puzzle/1.png"]
        lop_configuracoes = [
        [False, False, False, False, False, False, False, False, False],
        [False, True,  False, False, True,  False, False, False, True]
        ]

        lop_pecas = renpy.random.choice(lop_configuracoes)

    #Chama a tela
    call screen lights_out_puzzle(3) with dissolve
    return
