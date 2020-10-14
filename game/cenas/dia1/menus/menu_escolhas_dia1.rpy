label MENU_ESCOLHAS_DIA1:
    default visCoz = False
    default visBiblio = False
    default visQuartoHougin = False
    menu:
        "Locais para visitar:"

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
            $visCoz = False
            jump COZINHA

        "Quarto de Hougin" if not visQuartoHougin:
            $visQuartoHougin = False
            jump QUARTO_HOUGIN
