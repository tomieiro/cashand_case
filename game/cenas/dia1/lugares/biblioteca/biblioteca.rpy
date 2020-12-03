label BIBLIOTECA:

    play sound "audio/sonoplastia/Passos.mp3"
    scene biblioteca
    with Fade(2, 1, 0.5)
    play sound "audio/sonoplastia/AbrindoPorta.mp3"
    $renpy.pause(2, hard=hardPause)

    show sheppard neutro:
        xalign 0.5 yalign 0.99999

    shp "O que exatamente deveríamos procurar por aqui, detetive?"
    drc "Pistas, senhor Sheppard. Pequenos traços que mostram algo sobre a pessoa que procuramos."
    drc "O que você pode me dizer sobre este lugar?"
    shp "Bom, este cômodo é onde o senhor Hougin passava boas horas, acompanhado de seus livros. Ele costuma ler muito."
    drc "Era frequente?"
    shp "Bom, sim. Quando o senhor Hougin não tinha assuntos a tratar fora da cidade, ele vinha até aqui e passava algumas horas em leitura intensa."
    drc "Um homem culto, suponho?"
    shp "Ah sim. O senhor Hougin, além de um profundo conhecimento em histórias fantasiosas, bem como reais, e até de caráter acadêmico"
    shp "Claro, tinha também pleno conhecimento de todas as notícias da atualidade."
    drc "Isso impactava diretamente nos negócios, imagino."
    shp "De fato. Ser culto é uma habilidade essencial para alguém como o senhor Hougin e o meio que comandava."
    drc "Bom, consigo prever algo com isso relacionado ao assassinato."
    shp "O senhor tem certeza?"
    drc "Toda."
    drc "Vamos voltar senhor Sheppard. Ainda há um cômodo que eu desejo investigar ainda hoje."
    shp "Como quiser, senhor Rightclue."

    if primeira_visita:
        $primeira_visita = False
        jump TRANSICAO1
    else:
        jump TRANSICAO2
