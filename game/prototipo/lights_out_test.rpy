label LIGHTS_OUT_TEST:
    #Variáveis necessárias:
    python:
        lop_fim = False
        lop_pecas = [False] * 9
        lop_x = 0
        lop_y = 0
    #Chama a tela
    call screen lights_out_puzzle(3)
    return
