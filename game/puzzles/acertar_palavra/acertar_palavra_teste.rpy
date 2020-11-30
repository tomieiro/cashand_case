label APP_TESTE:
    #Variáveis necessárias:
    python:
        app_fim = False
        app_resposta = ["_", "_", "_", "_", "_", "_", "_", "_"]
        app_rod = 0
        app_vidas = 3
        app_erros = 0
        app_vidas_restantes = 3
        app_aux = ""
        app_pre_resposta = "Angra gosta muito de..."
        app_rodadas = 8
        app_gabarito = ["G", "E", "N", "G", "I", "B", "R", "E"]
        app_letras = [
                            ["E", "G", "M", "D", "W"],
                            ["A", "T", "U", "E", "S"],
                            ["N", "F", "A", "R", "M"],
                            ["G", "Q", "Z", "I", "O"],
                            ["R", "C", "I", "D", "A"],
                            ["B", "D", "N", "G", "L"],
                            ["E", "O", "V", "L", "R"],
                            ["A", "R", "I", "E", "U"],
                            ]
        app_qtd_letras = 5


    #Chama a tela
    call screen acertar_palavra_puzzle() with dissolve
    return


label APP_TESTE_GAME_OVER:
    hide screen acertar_palavra_puzzle with dissolve
    drc "Droga, vamos lá denovo!"
    jump APP_TESTE
