label CENA21:

    "*Batidas apressadas à porta*"
    mrth "Senhor Rightclue!"

    call RANDOMIZE(ind_a_info,["Kamira","Joe"],True)
    call RANDOMIZE(ind_b_info,["Kamira","Joe"],False)
    $ind_a = Character(ind_a_info[0], callback=character_beeps)
    $ind_b = Character(ind_b_info[0], callback=character_beeps)

    mrth "Senhor Rightclue!"
    scene quarto
    drc "Sim Martha? São apenas três da manhã."
    mrth "É o Sheppard, senhor! Foi encontrado morto no chão de seu quarto!"
    drc "Não..."
    drc "Não. Não. Não"

    scene corredor
    with Fade(1, 1, 0.5)

    drc "Não. Não. Não. Não. Não"
    drc "Não..."

    play music "audio/musicas/Fim.mp3" fadeout 3.0 fadein 5.0

    scene sheppard morte
    with Fade(2, 2, 0.5)

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
