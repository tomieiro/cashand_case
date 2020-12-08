label APP_DIA3:
    #Variáveis necessárias:
    python:
        app_fim = False
        app_resposta = ["_", "_", "_", "_", "_", "_", "_", "_"]
        app_rod = 0
        app_vidas = 3
        app_erros = 0
        app_vidas_restantes = 3
        app_aux = ""
        app_pre_resposta = "Isso é pelo de..."
        app_rodadas = 8
        app_gabarito = ["C", "A", "C", "H", "O", "R", "R", "O"]
        app_letras = [
                        ["H", "M", "C", "E", "D"],
                        ["O", "I", "O", "A", "E"],
                        ["N", "C", "R", "F", "S"],
                        ["I", "A", "R", "H", "O"],
                        ["O", "A", "U", "I", "E"],
                        ["N", "S", "R", "A", "P"],
                        ["R", "S", "V", "D", "O"],
                        ["I", "E", "A", "U", "O"]
                    ]
        app_qtd_letras = 5
        app_label_game_over = "APP_DIA3_GAME_OVER"
        app_label_sucesso= "APP_DIA3_SUCESSO"

    #Chama a tela
    play music "audio/musicas/Palavras.mp3" fadein 5.0
    show screen acertar_palavra_puzzle() with puzzle_transition8
    jump POINT_AND_CLICK

label APP_DIA3_GAME_OVER:
    stop music fadeout 5.0
    hide screen acertar_palavra_puzzle with puzzle_transition8
    "Não era isso..."
    "Vou tentar novamente!"
    jump APP_DIA2

label APP_DIA3_SUCESSO:
    stop music fadeout 5.0
    hide screen acertar_palavra_puzzle with puzzle_transition8
    return
