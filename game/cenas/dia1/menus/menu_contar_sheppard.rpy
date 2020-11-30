label MENU_CONTAR_SHEPPARD:
    menu:
        "O que fazer?"

        "Arriscar e contar":
            shp "Senhor Sheppard, está claro que foi um dos herdeiros!"
            shp "O que? O senhor está certo disso, detetive?"
            drc "Com toda certeza. É óbvio que seria um dos herdeiros. O último herdeiro, que por algum motivo, se perdeu a informação de quem era, desceu do quarto do senhor Hougin às duas e vinte nove."
            drc "O senhor Hougin deixou uma marca. A inscrição ao lado da cômoda tinha por significado, 231, duas e trinta e um, o horário em que foi apunhalado."
            drc "O assassino provavelmente apressou-se após o crime, e o senhor Hougin, em seu último suspiro, rabiscou traços para indicar o momento de sua morte. Realmente era um homem astuto e dotado de vontade e inteligências afiadíssimas."
            shp "As duas e trinta e um…"
            drc "Exato. Senhor Sheppard, precisamos ter extrema cautela. O assassino está aqui, dentro desta casa."
            shp "Senhor detetive, estou chocado. Não consigo entender, o porquê. Por que? Por que?"
            drc "Dinheiro, senhor Sheppard. Estou quase certo que é disso que se trata."
            shp "..."
            shp "Entendo."
            shp "Agradeço pelo empenho detetive. Vou me retirar por hoje. Tentar digerir tudo isso. Amanhã logo cedo investigaremos os herdeiros. Descobriremos quem é esse maldito traidor!"
            drc "Sim, senhor Sheppard. Descanse meu amigo. Amanhã começará a nossa caçada."
            shp "Obrigado, Rightclue. Tenho realmente que agradecer a presença do senhor, meu amigo."
            shp "Fico preocupado com você. E se alguém tentar alguma coisa."
            drc "Não acho que o assassino arriscaria me matar. O chefe envolveria toda a polícia no caso. E o assassino tem consciência disso."
            shp "O senhor está certo. Mas mesmo assim, tenha cuidado."
            drc "Certamente."
            shp "Bom, me despeço por aqui. Logo cedo baterei à porta."
            drc "Até mais, senhor Sheppard. Se mantenha de olhos abertos esta noite."
            shp "Com toda certeza."

        "Não contar ao Sheppard":
            drc "Senhor Sheppard. Não posso te contar exatamente quem seja. Me nego, por políticas pessoais, envolver o senhor neste risco. Mas saiba que pode ser mais que uma pessoa apenas. E está dentro dessa casa."
            shp "Compreendo, detetive.  Fico grato ao senhor, de toda a forma."
            shp "Qualquer coisa que precisar, estarei aqui para isso."
            shp "Precisamos pegar o culpado por tudo isso."
            drc "E pegaremos, senhor Sheppard."
            drc "Amanhã peço que se apronte logo cedo. Vamos entrar no encalço de algumas pessoas."
            shp "Certo. Estou de acordo!"
            shp "Vou regressar ao meu quarto imediatamente e acordar logo pela madrugada."
            drc "Pegaremos esse assassino, meu amigo."
            shp "Com toda a certeza!"
            shp "Obrigado, Rightclue. Tenho realmente que agradecer a presença do senhor, meu amigo."
            shp "Mas fico preocupado com você. E se alguém tentar alguma coisa."
            drc "Não acho que o assassino arriscaria me matar. O chefe envolveria toda a polícia no caso. E o assassino tem consciência disso."
            shp "O senhor está certo. Mas mesmo assim, tenha cuidado."
            drc "Certamente."
            shp "Agradeço por tudo, senhor Rightclue."

    stop music fadeout(5)
    scene quarto with dissolve
    with Fade(4, 4, 1)

    jump CENA21
