label MENU_ESCOLHAS_DIA1:
    default visCoz = False
    default visBiblio = False
    default visQuartoHougin = False
    menu:
        "Locais para visitar:"

        "Biblioteca" if not visBiblio:
            $visBiblio = True
            jump BIBLIOTECA

        "Cozinha" if not visCoz:
            $visCoz = False
            jump COZINHA

        "Quarto de Hougin" if not visQuartoHougin:
            $visQuartoHougin = False
            jump QUARTO_HOUGIN
