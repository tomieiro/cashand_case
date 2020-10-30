label QUARTO_HOUGIN:
    "*Entram pela porta*"
    shp "Bem, detetive, aqui estamos. Peço perdão pela comoção. Mas foi aqui, nesta mesma cama, que o senhor Hougin encontrou seu fim."
    drc "Entendo. Mas peço que aguente, senhor Sheppard. Toda pista é importante aqui."
    drc "De fato..."

    call PUZZLE_QUARTO_HOUGIN from _call_PUZZLE_QUARTO_HOUGIN

    drc "Parece que já vimos o bastante por aqui, senhor Sheppard. Vamos voltar."
    shp "Como quiser detetive."

    if primeira_visita:
        $primeira_visita = False
        jump TRANSICAO1
    else:
        jump TRANSICAO2
