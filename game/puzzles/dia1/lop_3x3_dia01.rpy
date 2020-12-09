#CHAMA A TELA DE UM LIGHTS_OUT PUZZLE 3X3

label LIGHTS_OUT_PUZZLE_3X3_DIA01:

    #Variáveis que precisam ser determinadas antes de chamar a tela:
    python:
        #Teremos 9 peças
        lop_fim = False
        lop_pecas = [False] * 9
        lop_proximo_do_fim = False
        lop_proximo_do_fim2 = False
        #Define o tamanho das peças
        lop_tam_peca = 200
        #Define as imagens das peças
        lop_img_peca_ligada = "images/engler/lights_out_sheppard/botao apertado.png"
        lop_img_peca_desligada = "images/engler/lights_out_sheppard/botao normal.png"
        lop_img_final = "#ffffff00"

        lop_configuracoes = [
        [True, True, True, True, False, False, True, False, False],
        [False, False, False, True, True, True, False, False, True],
        [True, False, False, False, True, True, True, False, False],
        [True, False, False, False, True, True, False, False, True],
        [False, True, False, True, True, True, True, False, True],
        ]

        lop_pecas = renpy.random.choice(lop_configuracoes)
        lop_game_over_label = "FIM_LOP_3x3_DIA01"
        lop_sucesso_label = "SUCESSO_LOP_3X3_DIA01"
        lop_timer_total = 4 * 60.0
        lop_timer_quase = 60.0

        lop_rapido = True
        lop_timer_rapido = 3 * 60.0


    "Aparentemente, há 9 botões que podem estar, ou não, pressionados."
    "Eles ativam quando estão pressionados."
    "Parece que, ao clicá-los, eles mudam de estado."
    "E isso pode influenciar outros botões próximos..."
    "Preciso deixar todos eles ativados."
    play music "audio/musicas/Descobrimento.mp3" fadein 5.0
    #Chama a tela
    show screen lights_out_puzzle(3, img_bg="#8f8d8c") with puzzle_transition8
    jump POINT_AND_CLICK
    #return

label FIM_LOP_3x3_DIA01:
    stop music fadeout 5.0
    hide screen lights_out_puzzle with puzzle_transition8
    "Droga, vou tentar novamente..."
    jump LIGHTS_OUT_PUZZLE_3X3_DIA01

label SUCESSO_LOP_3X3_DIA01:
    stop music fadeout 5.0
    #hide scree previa_puzzle
    python:
        if lop_rapido:
            persistent.rapido1 = True
            renpy.notify("Conquista - Relógio Falso!")
            conferir_todas_conquistas()
    hide screen lights_out_puzzle with puzzle_transition8
    return
