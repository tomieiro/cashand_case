label SLIDER_TEST:
    #Variáveis necessárias:
    #python:

    stop music
    play music "audio/musicas/Puzzles.ogg" fadeout 1
    show screen previa_puzzle() with dissolve
    "Hmmm, que interessante..."
    "Parece que temos que resolver um puzzle..."
    "Vamos lá!"
    hide screen previa_puzzle
    #Chama a tela
    call screen slider_puzzle(3) with dissolve
    hide screen point_and_click_test with dissolve
    jump PROTOTIPO
