label CENA34:
    scene hall
    with Fade(7, 2, 0.5)

    play music "audio/musicas/Onde.mp3"

    show hugo sadico with dissolve
    show carlo neutro behind hugo with dissolve:
        xalign 0.36 yalign 0.999999 xzoom 0.9 yzoom 0.9
    hugo "Meus parabéns, seu maldito! Salvou o dia. Desgraçado!"

    show hugo neutro with dissolve

    hugo "Quem iria desconfiar do pobre Hugo?"

    show hugo neutro reflexo with dissolve

    hugo "Não é mesmo, detetive?"

    show hugo assassino with dissolve:
        xzoom 1.005 yzoom 1.005

    hugo "Era melhor que nunca tivesse aparecido, sua peste!"

    hugo "O senhor pensa que acabou?"
    hugo "O senhor acha que está resolvido?"
    hugo "Ahahahahaha"
    hugo "Engano o seu. Eu irei buscá-lo, detetive..."
    hugo "Irei sim."
    vnc "Cale a boca."
    vnc "Teremos muito o que conversar ainda hoje."

    show hugo sadico with hpunch

    hugo "Aaaaaaaaahhhhhhhh!"

    show hugo assassino with hpunch:
        xzoom 1.005 yzoom 1.005

    hugo "Me larguem, seus porcos."
    hugo "Vou acabar com vocês."
    hugo "Acham que conseguem me matar?"
    hugo "Pois veremos."
    hugo "Veremos..."
    hugo "Ahahahahahahaha..."

    play sound "audio/sonoplastia/Thorn.mp3"
    $renpy.pause(3, hard=hardPause)

    show hugo neutro reflexo with hpunch

    hugo "Thorn, não!"
    "*Thorn tenta atacar Carlo Venchinni.*"
    vnc "Vira-lata imundo. Matem-no."
    hugo "Thorn! Fuja! Agora!"
    hugo "GUNIS ATENDUM KFVOK."
    "*Som de tiro*"
    "*Thorn foge*"
    vnc "Maldito cão. Fugiu."
    "Mas o que foi isso? Parece um código."
    "Bom, mas já não importa mais."

    show hugo assassino with dissolve:
        xzoom 1.005 yzoom 1.005

    vnc "Levem-no."
    hugo "Ahahahaha."

    show hugo assassino with hpunch:
        xzoom 1.005 yzoom 1.005

    hugo "Isso! Me levem. Me levem."

    hide hugo with dissolve

    show carlo neutro at center with moveinright

    vnc "Assim, me despeço do senhor, detetive Rightclue."
    drc "Fico grato, senhor Venchinni."
    drc "Garantirei sigilo de tudo que ocorreu aqui. Tem minha palavra."
    vnc "Excelente."
    vnc "Sheppard confiou em você. Fiz certo ao confiar também."
    drc "Até mais, senhor Venchinni."

    hide carlo with dissolve

    "Acabei me exaltando. Realmente um péssimo hábito..."

    show joe neutro with dissolve:
        xalign 0.3 yalign 0.9999999

    joe "..."

    show catherine neutra with dissolve:
        xalign 0.7 yalign 0.9999999

    cth "..."
    drc "Bom, meu trabalho termina aqui."
    joe "Senhor Rightclue. Eu nem sei o que dizer. Sinto que recebemos o senhor de forma tão áspera."
    joe "Mas se não fosse o senhor, não conseguiríamos nos salvar."
    cth "O senhor provou ser leal, honrado."
    cth "Permaneceu. Nos salvou."
    cth "Me parece até um cara legal agora..."
    "Como diria Sheppard: \"Ela está elogiando... Acredite, ela seria mais áspera...\""
    drc "É meu trabalho. Sinto tanto por vocês, de verdade."
    drc "Estou arrasado. Perderam mais duas pessoas no período que estive aqui. Eu realmente sinto muito."
    cth "A justiça foi feita, senhor. Estamos arrasados. Joe e eu temos apenas um ao outro agora."
    cth "Mas saberemos que estamos seguros."
    joe "..."
    cth "Sairemos daqui. Esse lugar está manchado demais com o sangue de nossa família."
    joe "Eu irei para outro lugar. Recomeçar. Mas parece que ainda estou em um pesadelo."
    cth "Eu também irei. Esse lugar, essa vida. Acho que está na hora de recomeçar. Em outro lugar."
    drc "Entendo."
    cth "Aquilo, Joe..."
    cth "Uma padaria, quem sabe?"
    drc "Uma padaria?"
    "Acho que dei uma breve sorriso..."
    drc "Não parece muito sua cara."
    cth "Meu bem, você realmente não me conhece."
    joe "Hahaha"
    "Um riso. Depois de tanto sofrimento..."
    "Eles estão tentando superar tudo isso. Será difícil, mas tenho certeza que juntos conseguirão."
    drc "Bom. Desejo toda a sorte do mundo aos dois."
    joe "Muito obrigado ao senhor."
    cth "Obrigada."
    drc "É meu trabalho."
    drc "Bom, me despeço por aqui."
    drc "Até mais a vocês."
    cth "Apareça na padaria algum dia."
    cth "Quem sabe cobro menos que o dobro de você."
    joe "Será sempre um prazer, senhor Rightclue."
    drc "Então nos veremos novamente."
    drc "Não é um adeus. É algo mais como um até logo."
    "Não consegui controlar o sorriso."
    joe "Até mais, senhor Rightclue."
    cth "Até mais, detetive, e obrigada."
    drc "Até."
    hide Joe with dissolve
    hide Catherine with dissolve

    play sound "audio/sonoplastia/AbrindoPorta.mp3"
    $renpy.pause(2, hard=hardPause)

    play sound "audio/sonoplastia/Passos.mp3"
    scene jardim with Fade(1, 2, 0.5)

    jump CENA35
