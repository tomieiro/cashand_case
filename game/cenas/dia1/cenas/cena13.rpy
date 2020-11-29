label CENA13:
    scene hall
    with Fade(2, 1, 0.5)

    show sheppard neutro with dissolve:
        xzoom 0.9 yzoom 0.9 xalign 0.5 yalign 0.99999

    shp "Aqui estamos. Senhor Rightclue, este é um ponto decisivo. É aqui que tudo começa pra você. As decisões que tomar a partir daqui, definirão se o senhor trará dias melhores para esta família."
    drc "Estou ciente, senhor Sheppard. Assumo esta responsabilidade."
    shp "Onde gostaria de investigar primeiro senhor Rightclue?"

jump MENU_ESCOLHAS_DIA1
