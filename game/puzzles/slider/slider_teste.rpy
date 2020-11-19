label SLIDER_TEST:
    #Variáveis necessárias:
    python:
        slp_fim = False
        slp_tam_peca = 200
        slp_x = 0.0
        slp_y = 0.0
        slp_pecas = [
        [0, 0], [1, 0], [2, 0],
        [0, 1], [1, 2], [1, 1],
        [0, 2], [2, 1]
        ]
    "Hmmm, que interessante..."
    "Parece que temos que resolver um puzzle..."
    "Vamos lá!"
    stop music
    play music "audio/musicas/Descobrimento.mp3" fadeout 1
    #Chama a tela
    call screen slider_puzzle(dim=3, img_bg="#534f4b") with dissolve
    hide screen point_and_click_prototipo with dissolve
    jump PROTOTIPO
