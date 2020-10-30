label MENU_ESCOLHAS_DIA1:
    default visCoz = False
    default visBiblio = False
    default visQuartoHougin = False
    menu:
        "Locais para visitar:"

        "Biblioteca" if not visBiblio:
            shp "Senhor Rightclue, não entendo a razão de o senhor querer visitar a biblioteca."
            menu:
                shp "O senhor tem certeza?"
                "Ir para a biblioteca":
                    $visBiblio = True
                    jump BIBLIOTECA

                "Pensar melhor":
                    jump MENU_ESCOLHAS_DIA1

        "Cozinha" if not visCoz:
            shp "O senhor tem certeza?"
            "Ir para a cozinha":
                $visCoz = False
                jump COZINHA
            "Pensar melhor":
                jump MENU_ESCOLHAS_DIA1

        "Quarto de Hougin" if not visQuartoHougin:
            shp "O senhor tem certeza?"
            "Ir para o Quarto de Hougin":
                $visQuartoHougin = False
                jump QUARTO_HOUGIN
            "Pensar melhor":
                jump MENU_ESCOLHAS_DIA1

        "Perguntar sobre os Locais":
            jump MENU_ESCOLHAS_DIA1