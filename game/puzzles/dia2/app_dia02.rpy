label APP_DIA2:
    #Variáveis necessárias:
    python:
        app_fim = False
        app_resposta = ["_", "_", "_", "_", "_", "_", "_", "_"]
        app_rod = 0
        app_vidas = 3
        app_erros = 0
        app_vidas_restantes = 3
        app_aux = ""
        app_pre_resposta = "A Kamira é..."
        app_rodadas = 8
        app_gabarito = ["I", "N", "O", "C", "E", "N", "T", "E"]
        app_letras = [
                        ["I", "A", "E", "M", "D"],
                        ["D", "R", "T", "N", "M"],
                        ["A", "O", "E", "I", "T"],
                        ["C", "N", "M", "L", "S"],
                        ["O", "A", "U", "I", "E"],
                        ["D", "R", "N", "M", "P"],
                        ["A", "C", "S", "T", "V"],
                        ["E", "A", "O", "I", "U"]
                    ]
        app_qtd_letras = 5
        app_label_game_over = "APP_DIA2_GAME_OVER"
        app_label_sucesso= "APP_DIA2_SUCESSO"

    #Chama a tela
    play music "audio/musicas/Palavras.mp3" fadein 5.0
    show screen acertar_palavra_puzzle() with puzzle_transition8
    jump POINT_AND_CLICK

label APP_DIA2_GAME_OVER:
    stop music fadeout 5.0
    hide screen acertar_palavra_puzzle with puzzle_transition8
    "Não era isso..."
    "Vou tentar novamente!"
    jump APP_DIA2

label APP_DIA2_SUCESSO:
    stop music fadeout 5.0
    hide screen acertar_palavra_puzzle with puzzle_transition8
    return
