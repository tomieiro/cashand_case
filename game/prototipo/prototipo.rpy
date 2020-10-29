init python:
    def character_beeps(event, interact=True, **kwargs):
        if not interact:
            return
        if event == "show_done":
            renpy.sound.play("audio/voices/voice_test.wav", loop="True", channel="sound")
        elif event == "slow_done" or event == "end":
            renpy.sound.stop(channel="sound")


define shp = Character("Sheppard", who_color="#c8ffc8", callback=character_beeps)
define kmr = Character("Kamira", who_color="#ffc8c8", callback=character_beeps)
define drc = Character("Rightclue", who_color="#c8c8ff", callback=character_beeps)

image img_bg = "images/teste/bg_test.png"
image img_bg2 = "images/teste/bg_test_2.png"

default per_role1 = shp
default per_role2 = kmr

transform kam_center:
    xalign 0.5
    yalign 2.0

label PROTOTIPO:

    #call screen slider_puzzle(3) with dissolve

    $quick_menu = True

    play music "audio/musicas/Tensao.ogg" fadeout 1

label ESCOLHA1:

    "Entendo... Estou na presença de duas pessoas. Vejamos..."
    scene img_bg2 with dissolve

    menu:
        "O que devo fazer?"

        "Diálogo A":
            "(Diálogos com roles)"
            $per_role1 = shp
            $per_role2 = kmr
            call DIALOGO_ROLE
            jump FIM_ESCOLHA1

        "Diálogo B":
            "(Diálogos com roles)"
            $per_role1 = kmr
            $per_role2 = shp
            call DIALOGO_ROLE
            jump FIM_ESCOLHA1

        "Investigar a sala":
            python:
                copo_selecionado = False
                cookie_selecionado = False
                itens_no_inventario = []
            #Chama a tela de point and click
            show screen point_and_click_test() with dissolve
            jump PUZZLE_TESTE

#Parte de diálogos específicos dos personagens
label FIM_ESCOLHA1:
    "(Diálogos sem roles)"
    show sheppard neutro at center
    shp "Eu sou Sheppard"
    hide sheppard neutro
    show kamira neutra at kam_center
    kmr "Eu sou Kamira"
    hide kamira neutra

    jump ESCOLHA1
    return


#Parte de diálogo para a role
label DIALOGO_ROLE:

    if per_role1 == shp:
        show sheppard neutro at center
    else:
        show kamira neutra at kam_center
    per_role1 "Eu sou a role 1"
    hide sheppard neutro
    hide kamira neutra

    if per_role2 == shp:
        show sheppard neutro at center
    else:
        show kamira neutra at kam_center
    per_role2 "Eu sou a role 2"
    hide sheppard neutro
    hide kamira neutra

    return

#Essa label existe para possibilitar uma tela point and click
#que ainda pode usar diálogos e até personagens, se necessário.
label PUZZLE_TESTE:
    #Esconde caixa de diálogo por enquanto
    window hide
    #Desativa o menu rápido durante toda a parte do point and click(evita algumas inconsistências)
    #PRECISA SER REPENSADO ISSO AQUI:
    #SÓ ESCONDE A DROGA DO MENU KKKK, O ROLLBACK AINDA PODE SER FEITO COM O MOUSE :(
    #$quick_menu = False
    $renpy.pause(hard=True)
