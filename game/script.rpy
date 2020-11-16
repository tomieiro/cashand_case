#O jogo começa aqui
label start:

    #Para de tocar música do menu inicial:
    stop music fadeout(4)

    #Vai para a área de testagem de telas
    #jump INVENTARIO_DE_ESCOLHA_DIA01
    #jump LIGHTS_OUT_PUZZLE_3X3
    #jump CONCLUINDO_DIA1
    #call TESTES_TELAS

    #call CENA25
    #Vai para a primeira cena do dia 1

    jump CENA11

    #jump PROTOTIPO

    return
