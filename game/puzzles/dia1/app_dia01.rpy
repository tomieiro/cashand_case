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
                        ["H", "O", "E", "A", "M"],
                        ["A", "S", "M", "C", "E"],
                        ["P", "A", "H", "R", "F"],
                        ["O", "I", "E", "D", "R"],
                        ["E", "A", "H", "P", "O"],
                        ["P", "O", "G", "I", "S"],
                        ["N", "R", "E", "O", "A"],
                        ["S", "R", "D", "T", "O"],
                        ["A", "D", "O", "S", "I"],
                    ]
        app_qtd_letras = 5
        app_label_game_over = "APP_DIA1_GAME_OVER"
    #Chama a tela
    play sound "audio/musicas/Descobrimento.mp3"
    call screen acertar_palavra_puzzle() with puzzle_transition8
    return


label APP_DIA1_GAME_OVER:
    hide screen acertar_palavra_puzzle with dissolve
    "Não era isso..."
    "Vou tentar novamente!"
    jump APP_TESTE
