#Essa label existe para possibilitar uma tela point and click
#que ainda pode usar diálogos e até personagens, se necessário.
label POINT_AND_CLICK:
    #Esconde caixa de diálogo por enquanto
    window hide
    #Desativa o menu rápido durante toda a parte do point and click(evita algumas inconsistências??? não sei)
    #PRECISA SER REPENSADO ISSO AQUI
    #$quick_menu = False #SÓ ESCONDE A DROGA DO MENU KKKK, O ROLLBACK AINDA PODE SER FEITO COM O MOUSE :(

    $ui.interact() # Esse é melhor?


label POINT_AND_CLICK_2:
    #Esconde caixa de diálogo por enquanto
    window hide
    #Desativa o menu rápido durante toda a parte do point and click(evita algumas inconsistências??? não sei)
    #PRECISA SER REPENSADO ISSO AQUI
    #$quick_menu = False #SÓ ESCONDE A DROGA DO MENU KKKK, O ROLLBACK AINDA PODE SER FEITO COM O MOUSE :(

    $renpy.choice_for_skipping() # PARA O SKIPPING PORRA
    $renpy.pause(hard=True) #Garante que o jogo fique parado esperando a tela de point and click
