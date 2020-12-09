#CHAMA A TELA DE UM LIGHTS_OUT PUZZLE 4X4

label LIGHTS_OUT_PUZZLE_4X4_DIA02:

    #Variáveis que precisam ser determinadas antes de chamar a tela:
    python:
        #Teremos 16 peças
        lop_fim = False
        lop_pecas = [False] * 16
        lop_proximo_do_fim = False
        lop_proximo_do_fim2 = False
        #Define o tamanho das peças
        lop_tam_peca = 150
        #Define as imagens das peças
        lop_img_peca_ligada = "images/engler/itens/botao_ligado.png"
        lop_img_peca_desligada = "images/engler/itens/botao_desligado.png"
        lop_img_final = "#ffffff00"

        lop_configuracoes = [
        [False, False, True, False, True, True, True, True, True, True, True, False, True, False, False, False],
        [True, True, True, True, True, False, True, False, False, True, True, False, False, True, False, False],
        [True, True, True, False, False, False, False, True, True, False, True, True, True, True, False, False],
        [True, False, True, True, True, False, True, True, True, True, True, False, False, False, False, False],
        [True, True, False, False, False, False, False, True, True, True, False, True, True, True, True, False],
        ]

        lop_pecas = renpy.random.choice(lop_configuracoes)
        lop_game_over_label = "FIM_LOP_4X4_DIA02"
        lop_sucesso_label = "SUCESSO_LOP_4X4_DIA02"
        lop_timer_total = 3 * 60.0
        lop_timer_quase = 60.0

    "Aparentemente, há 16 peças luminosas."
    "Ao clicá-las, posso ativar ou desativar."
    "E isso influencia nas peças em volta."
    "Preciso deixar todas ligadas."

    play music "audio/musicas/Descobrimento.mp3" fadein 5.0
    #Chama a tela
    show screen lights_out_puzzle(4, img_bg="#787abf") with puzzle_transition8
    jump POINT_AND_CLICK
    #return

label FIM_LOP_4X4_DIA02:
    stop music fadeout 5.0
    hide screen lights_out_puzzle with puzzle_transition8
    "Droga, vou tentar novamente..."
    jump LIGHTS_OUT_PUZZLE_4X4_DIA02

label SUCESSO_LOP_4X4_DIA02:
    stop music fadeout 5.0
    hide screen lights_out_puzzle with puzzle_transition8
    return
