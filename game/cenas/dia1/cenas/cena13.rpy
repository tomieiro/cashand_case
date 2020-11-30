label CENA13:

    shp "Aqui estamos. Senhor Rightclue, este é um ponto decisivo. É aqui que tudo começa pra você. As decisões que tomar a partir daqui, definirão se o senhor trará dias melhores para esta família."
    drc "Estou ciente, senhor Sheppard. Assumo esta responsabilidade."
    shp "Temos três lugares que podemos visitar agora, senhor Rightclue."
    shp "Bom por onde posso começar..."

label PENSAR_MELHOR_DIA1:
    if(not visQuartoHougin):
        shp "O quarto do senhor Hougin, foi onde ele foi encontrado, talvez haja algo interessante por lá."
        shp "Além dele temos os quartos dos demais residentes, mas acredito que nenhum deles queira ser perturbado no momento ..."
        "Realmente, dada a minha recente \"recepção\" não acho que eles tenham muito oque falar no momento"
    if(not visBiblio):
        shp "Temos também a velha biblioteca da mansão, faz anos que ninguém, fora o senhor Hougin, entrar nela, não vejo como pode haver alguma pista dentro dela."
    if(not visCoz):
        shp "E também temos a cozinha, acredito que a senhora Martha, a empregada da família, esteja por lá."
        shp "Ela pode saber de alguma coisa, já que ela está sempre atarefada indo de um lado ao outro da mansão."
    shp "Basicamente é isso..."

    jump MENU_ESCOLHAS_DIA1
