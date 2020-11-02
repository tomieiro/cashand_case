label MENU_ESCOLHAS_DIA1:
    shp "Bom por onde posso começar..."
    shp "O quarto do senhor Hougin, foi onde ele foi encontrado, talvez haja algo interessante por lá."
    shp "Além dele temos os quartos dos demais residentes, mas acredito que nenhum deles queira ser perturbado no momento ..."
    "Realmente, dada a minha recente \"recepção\" não acho que eles tenham muito oque falar no momento"
    shp "Temos também a velha biblioteca da mansão, faz anos que ninguém, fora o senhor Hougin, entrar nela, não vejo como pode haver alguma pista dentro dela."
    shp "Por fim temos a cozinha, acredito que a senhora Martha, a empregada da família, esteja por lá."
    shp "Ela pode saber de alguma coisa, já que ela está sempre atarefada indo de um lado ao outro da mansão."
    shp "Basicamente é isso..."
    menu:
        "Locais para visitar"

        "Biblioteca" if not visBiblio:
            shp "Senhor Rightclue, não entendo a razão de o senhor querer visitar a biblioteca..."
            shp "Pelo que me lembro, o senhor Hougin não visitava a biblioteca há pelo menos uma semana."
            menu:
                shp "O senhor tem certeza?"
                "Ir para a biblioteca":
                    drc "Acredite em mim Sheppard, as pequenas pistas importam!"
                    $visBiblio = True
                    jump BIBLIOTECA
                "Pensar melhor":
                    drc "Realmente, senhor Sheppard. Deixe-me pensar melhor..."
                    jump MENU_ESCOLHAS_DIA1
        "Cozinha" if not visCoz:
            menu:
                shp "O senhor tem certeza?"
                "Ir para a cozinha":
                    $visCoz = True
                    jump COZINHA
                "Pensar melhor":
                    jump MENU_ESCOLHAS_DIA1
        "Quarto de Hougin" if not visQuartoHougin:
            menu:
                shp "O senhor tem certeza?"
                "Ir para o Quarto de Hougin":
                    $visQuartoHougin = True
                    jump QUARTO_HOUGIN
                "Pensar melhor":
                    jump MENU_ESCOLHAS_DIA1
        "O senhor poderia repetir?":
            jump MENU_ESCOLHAS_DIA1
