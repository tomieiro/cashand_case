label APP_TESTE:
    #Variáveis necessárias:
    python:
        app_fim = False
        app_resposta = ["_", "_", "_", "_", "_", "_", "_", "_"]
        app_rod = 0
        app_vidas = 3
        app_erros = 0
        app_vidas_restantes = 3
    #Chama a tela
    call screen acertar_palavra_puzzle() with dissolve
    return


label APP_TESTE_GAME_OVER:
    hide screen acertar_palavra_puzzle with dissolve
    drc "Droga, vamos lá denovo!"
    jump APP_TESTE
