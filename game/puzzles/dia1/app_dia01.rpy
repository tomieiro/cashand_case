label APP_DIA1:
    #Variáveis necessárias:
    python:
        app_fim = False
        app_resposta = ["_", "_", "_", "_", "_", "_", "_", "_", "_"]
        app_rod = 0
        app_vidas = 3
        app_erros = 0
        app_vidas_restantes = 3
        app_aux = ""
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
        app_qtd_letras = 5
        app_label_game_over = "APP_DIA1_GAME_OVER"
    #Chama a tela
    play music "audio/musicas/Palavras.mp3"
    call screen acertar_palavra_puzzle() with puzzle_transition8
    return


label APP_DIA1_GAME_OVER:
    hide screen acertar_palavra_puzzle with dissolve
    "Não era isso..."
    "Vou tentar novamente!"
    jump APP_TESTE
