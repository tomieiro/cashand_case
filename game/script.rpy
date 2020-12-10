#Dados persistentes:
define persistent.conquista_demitido = False
define persistent.conquista_sheppard1 = False
define persistent.conquista_sheppard2 = False
define persistent.conquista_biscoito = False
define persistent.rapido1 = False
define persistent.rapido2 = False
define persistent.rapido3 = False
define persistent.rapido4 = False
define persistent.rapido5 = False
define persistent.pac1 = False
define persistent.pac2 = False
define persistent.pac3 = False
define persistent.ganhou_tudo = False
define persistent.terminou_game = False

#O jogo começa aqui
label start:

    python:
        contou_ao_sheppard = False
        cluepoints = 0
        primeira_visita = True
        visCoz = False
        visBiblio = False
        visQuartoHougin = False
        visHall = False
        whoIs = 0
        flag_kamira = 0
        hardPause = True

    #Para de tocar música do menu inicial:
    stop music fadeout(4)

    jump CENA11

    return
