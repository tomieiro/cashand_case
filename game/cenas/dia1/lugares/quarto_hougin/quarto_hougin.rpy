label QUARTO_HOUGIN:
    "*Entram pela porta*"
    shp "Bem, detetive, aqui estamos."
    shp "Peço perdão pela comoção, mas foi aqui, nesta mesma cama, que o senhor Hougin encontrou seu fim."
    drc "Entendo. Mas peço que aguente, senhor Sheppard. Toda pista é importante aqui."
    shp "De fato..."

    call CHAMA_TELA_PAC_DIA1

    drc "Parece que já vimos o bastante por aqui, senhor Sheppard. Vamos voltar."
    shp "Como quiser, detetive."

    if primeira_visita:
        $primeira_visita = False
        jump TRANSICAO1
    else:
        jump TRANSICAO2
