label MENU_ESCOLHAS_DIA1:
    menu:
        "Locais para visitar"

        "Biblioteca" if not visBiblio:
            shp "Senhor Rightclue, não entendo a razão de o senhor querer visitar a biblioteca..."
            shp "Pelo que me lembro, o senhor Hougin não visitava a biblioteca há pelo menos uma semana."
            menu:
                shp "O senhor tem certeza?"
                "Ir para a biblioteca":
                    drc "Acredite em mim, Sheppard, as pequenas pistas importam!"
                    $visBiblio = True
                    play sound "audio/sonoplastia/Passos.mp3"
                    jump BIBLIOTECA
                "Pensar melhor":
                    drc "Realmente, senhor Sheppard. Deixe-me pensar melhor..."
                    jump MENU_ESCOLHAS_DIA1
        "Cozinha" if not visCoz:
            menu:
                shp "O senhor tem certeza?"
                "Ir para a cozinha":
                    $visCoz = True
                    play sound "audio/sonoplastia/Passos.mp3"
                    jump COZINHA
                "Pensar melhor":
                    jump MENU_ESCOLHAS_DIA1
        "Quarto de Hougin" if not visQuartoHougin:
            menu:
                shp "O senhor tem certeza?"
                "Ir para o Quarto de Hougin":
                    $visQuartoHougin = True
                    play sound "audio/sonoplastia/Passos.mp3"
                    jump QUARTO_HOUGIN
                "Pensar melhor":
                    jump MENU_ESCOLHAS_DIA1
        "O senhor poderia repetir?":
            jump PENSAR_MELHOR_DIA1
