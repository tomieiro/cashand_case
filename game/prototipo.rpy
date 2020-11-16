image prot_img_cid = "images/cenarios/cidade.png"
image prot_img_esc = "images/cenarios/escritorio.png"

image side sheppard = "/images/engler/personagens/sheppard/sheppard neutro.png"

default prot_role1 = shp
default prot_role2 = kmr


transform kam_center:
    xalign 0.5
    yalign 2.0

label PROTOTIPO:

    #$quick_menu = True
    play music "audio/musicas/Ambiente.mp3" fadeout 1

label ESCOLHA1:

    "Entendo... Estou na presença de duas pessoas. Vejamos..."
    scene prot_img_cid with dissolve

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
            jump CHAMA_TELA_PAC_PROTOTIPO


#Parte de diálogos específicos dos personagens
label FIM_ESCOLHA1:
    "(Diálogos sem roles)"
    show sheppard neutro at center
    shp "Eu sou Sheppard."
    hide sheppard neutro
    show kamira neutra at kam_center
    kmr "Eu sou Kamira."
    hide kamira neutra

    jump ESCOLHA1
    return


#Parte de diálogo para a role
label DIALOGO_ROLE:

    if per_role1 == shp:
        show sheppard neutro at center
    else:
        show kamira neutra at kam_center
    per_role1 "Eu sou a role 1."
    hide sheppard neutro
    hide kamira neutra

    if per_role2 == shp:
        show sheppard neutro at center
    else:
        show kamira neutra at kam_center
    per_role2 "Eu sou a role 2."
    hide sheppard neutro
    hide kamira neutra

    return


#Essa label existe para possibilitar uma tela point and click
#que ainda pode usar diálogos e até personagens, se necessário.
label PUZZLE_TESTE:
    #Esconde caixa de diálogo por enquanto
    window hide
    #Desativa o menu rápido durante toda a parte do point and click(evita algumas inconsistências??? não sei)
    #PRECISA SER REPENSADO ISSO AQUI
    #$quick_menu = False #SÓ ESCONDE A DROGA DO MENU KKKK, O ROLLBACK AINDA PODE SER FEITO COM O MOUSE :(

    $renpy.pause(hard=True) #Garante que o jogo fique parado esperando a tela de point and click
