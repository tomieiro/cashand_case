label TRANSICAO2:

    scene hall
    with Fade(2, 1, 0.5)

    show sheppard neutro with dissolve:
        xzoom 0.9 yzoom 0.9 xalign 0.5 yalign 0.99999

    shp "Bom, peço que aguarde um momento, detetive."
    drc "Tudo bem, senhor Sheppard."

    play sound "audio/sonoplastia/Passos.mp3"
    hide sheppard neutro

    "..."
    $renpy.pause(3, hard=hardPause)

    show sheppard neutro with dissolve:
        xzoom 0.9 yzoom 0.9 xalign 0.5 yalign 0.99999

    shp "Detetive, estou garantindo que o senhor possa passar a noite por aqui e evitar despesas extras. Já conversei com os Cashand e te dou essa oportunidade."
    drc "Agradeço, senhor Sheppard, mas acho que minha presença não é bem vinda."
    shp "Eu insisto, detetive. Passarei esta noite aqui também, no quarto ao lado do seu."
    drc "Bom, se o senhor insiste, creio que seja prudente, já que posso começar meu trabalho logo pela manhã."
    shp "De fato. Fico feliz em ouvir isso."
    shp "Então venha. Vou te mostrar seu quarto. Um bom banho e um descanso serão benéficos antes de continuarmos."

    play sound "audio/sonoplastia/Passos.mp3"
    stop music fadeout(4)
    scene corredor quartos
    with Fade(2,1,0.5)

    show sheppard neutro at center with dissolve

    play sound "audio/sonoplastia/AbrindoPorta.mp3"
    $renpy.pause(3, hard=hardPause)

    shp "Este é seu quarto. Fique à vontade."
    drc "Fico muito agradecido, senhor Sheppard."
    shp "Gostaria de conversar com o senhor após o jantar que, claro, providenciarei para que Martha leve ao seu quarto."
    drc "Agradeço, senhor Sheppard, e claro, terei algo a dizer sobre toda essa situação."
    shp "Certo. Seu quarto é o segundo desse primeiro andar. Logo ali."
    shp "Nos encontramos mais tarde então, senhor Rightclue."
    drc "Tudo bem, até mais, senhor Sheppard."

    hide sheppard with dissolve

    scene quarto
    with Fade(5,2,0.5)

    play sound "audio/sonoplastia/SentandoNaCama.mp3"
    $renpy.pause(3, hard=hardPause)

    "Foi um excelente banho. Também já estou satisfeito com o jantar."

    if cluepoints >= 2:
        call CONCLUINDO_DIA1 from _call_CONCLUINDO_DIA1

    jump CENA14
