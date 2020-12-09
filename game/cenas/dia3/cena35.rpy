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
    if(not persistent.terminou_game):
        $renpy.notify("Desbloqueou tela de Conquistas!")
    $persistent.terminou_game = True
    stop music fadeout(6)
    $renpy.pause(6, hard=hardPause)

    play music "audio/musicas/Menu.mp3" fadein 2.0
    $credits_speed = 25
    scene black
    show credits_image at Move((0.5, 1.0), (0.5, -1.0), credits_speed,
                  xanchor=0.5, yanchor=0)
    with Pause(credits_speed+10)
