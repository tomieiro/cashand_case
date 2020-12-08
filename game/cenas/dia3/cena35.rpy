label CENA35:
    play music "audio/musicas/Ambiente.mp3" fadein 4.0
    play sound "audio/sonoplastia/Passos.mp3"
    scene cidade
    with Fade(5, 2, 0.5)
    #Fazer continuacao aqui
    "Cheguei ao fim de mais um caso."
    "Deveras triste, confesso."
    "Mas acho que ficará na história."
    "Pelo menos na minha história..."
    stop music fadeout(6)
    scene fim
    with Dissolve(5)
    $renpy.pause(6, hard=hardPause)
