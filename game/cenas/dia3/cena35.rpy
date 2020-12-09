label CENA35:
    play sound "audio/sonoplastia/Passos.mp3"
    scene cidade
    with Fade(5, 2, 0.5)
    #Fazer continuacao aqui
    "Cheguei ao fim de mais um caso."
    "Deveras triste, confesso."
    "Mas acho que ficará na história."
    "Pelo menos na minha história..."
    play music "audio/musicas/OFim.mp3" fadein(6)
    scene fim
    with Dissolve(6)
    stop music fadeout(6)
    $renpy.pause(6, hard=hardPause)
label CREDITOS:
    call screen tela_creditos() with dissolve
