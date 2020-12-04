label QUARTO_HOUGIN:
    scene corredor quartos
    with Fade(1,1,0.5)

    shp "Bem, detetive, aqui estamos."
    shp "Peço perdão pela comoção, mas foi aqui, neste mesmo quarto, que o senhor Hougin encontrou seu fim."
    drc "Entendo. Mas peço que aguente, senhor Sheppard. Toda pista é importante aqui."
    shp "De fato..."

    play sound "audio/sonoplastia/AbrindoPorta.mp3"
    $renpy.pause(3, hard=hardPause)

    call CHAMA_TELA_PAC_DIA1 from _call_CHAMA_TELA_PAC_DIA1
    $cluepoints = cluepoints + 1

    play music "audio/musicas/Pistas.mp3" fadein 3.0

    drc "Parece que já vimos o bastante por aqui, senhor Sheppard. Vamos voltar."
    shp "Como quiser, detetive."

    play sound "audio/sonoplastia/Passos.mp3"

    if primeira_visita:
        $primeira_visita = False
        jump TRANSICAO1
    else:
        jump TRANSICAO2
