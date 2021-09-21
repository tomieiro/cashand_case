label APP_DIA1:
    #Variáveis necessárias:
    python:
        app_fim = False
        app_resposta = []
        app_pre_resposta = ""
        app_rodadas = 0
        app_gabarito = []
        app_letras = []

        if config.language == 'english':
            #inheritors
            app_resposta = ["_", "_", "_", "_", "_", "_", "_", "_", "_", "_"]
            app_pre_resposta = "The culprit is one of the..."
            app_rodadas = 10
            app_gabarito = ["I", "N", "H", "E", "R", "I", "T", "O", "R", "S"]
            app_letras = [
                            ["M", "S", "E", "F", "I"],
                            ["C", "D", "M", "N", "A"],
                            ["H", "C", "T", "S", "F"],
                            ["E", "I", "U", "O", "A"],
                            ["R", "S", "T", "F", "D"],
                            ["I", "A", "P", "C", "E"],
                            ["V", "M", "C", "D", "T"],
                            ["O", "A", "E", "I", "T"],
                            ["N", "U", "R", "E", "D"],
                            ["T", "O", "I", "S", "A"],
                        ]

        else:
            #herdeiros
            app_resposta = ["_", "_", "_", "_", "_", "_", "_", "_", "_"]
            app_pre_resposta = "O culpado é um dos..."
            app_rodadas = 9
            app_gabarito = ["H", "E", "R", "D", "E", "I", "R", "O", "S"]
            app_letras = [
                            ["H", "S", "E", "F", "V"],
                            ["A", "O", "I", "U", "E"],
                            ["P", "A", "S", "R", "T"],
                            ["O", "I", "E", "D", "P"],
                            ["E", "A", "U", "I", "O"],
                            ["P", "A", "G", "I", "S"],
                            ["N", "R", "M", "T", "V"],
                            ["E", "R", "N", "T", "O"],
                            ["M", "R", "U", "S", "Z"],
                        ]

        app_rod = 0
        app_vidas = 3
        app_erros = 0
        app_vidas_restantes = 3
        app_aux = ""
        app_qtd_letras = 5
        app_label_game_over = "APP_DIA1_GAME_OVER"
        app_label_sucesso= "APP_DIA1_SUCESSO"

    #Chama a tela
    play music "audio/musicas/Palavras.mp3" fadein 5.0
    show screen acertar_palavra_puzzle() with puzzle_transition8
    jump POINT_AND_CLICK

label APP_DIA1_GAME_OVER:
    stop music fadeout 5.0
    hide screen acertar_palavra_puzzle with puzzle_transition8
    "Não era isso..."
    "Vou tentar novamente!"
    jump APP_DIA1

label APP_DIA1_SUCESSO:
    stop music fadeout 5.0
    hide screen acertar_palavra_puzzle with puzzle_transition8
    return
