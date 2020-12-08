label CENA13:
    play sound "audio/sonoplastia/Passos.mp3"
    stop music fadeout(3)
    scene hall
    with Fade(2, 1, 0.5)

    show sheppard neutro with dissolve:
        xzoom 0.9 yzoom 0.9 xalign 0.5 yalign 0.99999

    #$renpy.music.set_volume(0.5, delay=0, channel='music')
    play music "audio/musicas/Pistas.mp3" fadein 3.0

    shp "Aqui estamos. Senhor Rightclue, este é um ponto decisivo. É aqui que tudo começa para você. As decisões que tomar a partir daqui definirão se o senhor trará dias melhores para esta família."
    drc "Estou ciente, senhor Sheppard. Assumo esta responsabilidade."
    shp "Temos três lugares que podemos visitar agora, senhor Rightclue."
    shp "Bom, por onde posso começar..."

label PENSAR_MELHOR_DIA1:
    if(not visQuartoHougin):
        shp "O quarto do senhor Hougin foi onde ele foi encontrado, talvez haja algo interessante por lá."
        shp "Além dele temos os quartos dos demais residentes, mas acredito que nenhum deles queira ser perturbado no momento..."
        "Realmente, dada a minha recente \"recepção\" não acho que eles tenham muito o que falar no momento."
    if(not visBiblio):
        shp "Temos também a velha biblioteca da mansão. Faz anos que ninguém, fora o senhor Hougin, entra nela. Não vejo como pode haver alguma pista dentro dela."
    if(not visCoz):
        shp "Também temos a cozinha, acredito que a senhora Martha, a empregada da família, esteja por lá."
        shp "Ela pode saber de alguma coisa, já que ela está sempre atarefada indo de um lado ao outro da mansão."
    shp "Basicamente é isso..."

    jump MENU_ESCOLHAS_DIA1
