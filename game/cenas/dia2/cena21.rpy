label CENA21:

    scene quarto
    with Fade(4,2,0.5)

    scene quarto with hpunch
    play sound "audio/sonoplastia/BatidaRapidaPorta.mp3"
    $renpy.pause(1, hard=hardPause)
    mrth "Senhor Rightclue!"

    $randomize(ind_a_info,["Kamira","Joe"],True)
    $randomize(ind_b_info,["Kamira","Joe"],False)
    $ind_a = Character(ind_a_info[0], callback=character_beeps)
    $ind_b = Character(ind_b_info[0], callback=character_beeps)

    scene quarto with hpunch
    play sound "audio/sonoplastia/BatidaRapidaPorta.mp3"
    $renpy.pause(1, hard=hardPause)
    mrth "Senhor Rightclue!"

    drc "Sim Martha? São apenas três da manhã."
    mrth "É o Sheppard, senhor! Está morto no chão de seu quarto!"
    mrth "Céus, venha de pressa."
    drc "Não..."

    play sound "audio/sonoplastia/LevantandoDaCama.mp3"
    $renpy.pause(1, hard=hardPause)

    drc "Não. Não. Não"

    play sound "audio/sonoplastia/TrancandoPorta.mp3"
    $renpy.pause(1, hard=hardPause)

    play sound "audio/sonoplastia/AbrindoPorta.mp3"
    $renpy.pause(1, hard=hardPause)

    scene corredor hall
    with Fade(1, 1, 0.5)

    drc "Não. Não. Não. Não. Não"
    drc "Não..."

    play music "audio/musicas/Fim.mp3" fadein 5.0

    scene sheppard morte
    with Fade(0.2, 0.2, 0.5)

    pause(3)

    drc "Não... Não..."

    window hide

    pause (3)

    drc "Sheppard.... Por que? Por que?"
    drc "*Por que?"
    drc "Por que eu tomei aquela decisão em relação a contá-lo. Me desculpe Sheppard. Me desculpe..."
    "Meu deus. Meu deus."
    "Por que?"
    "Ele segurava um lenço."
    #Coleta lenço e coloca "..." quando ele clicar.
    "*Rightclue guarda o lenço*"
    "Me desculpe senhor Sheppard.."
    "Eu não cheguei a tempo."
    "Não cheguei..."
    "..."

    window hide

    pause(3)

    jump CENA22
