label LIGHTS_OUT_TEST:
    #Variáveis necessárias:
    python:
        lop_fim = False
        lop_pecas = [False] * 9
        lop_x = 0
        lop_y = 0
    stop music
    play music "audio/musicas/Puzzles.ogg" fadeout 1
    show screen previa_puzzle() with dissolve
    "Hmmm, que interessante..."
    "Parece que temos que resolver um puzzle..."
    "Vamos lá!"
    hide screen previa_puzzle
    #Chama a tela
    call screen lights_out_puzzle(3) with dissolve
    hide screen point_and_click_test with dissolve
    
