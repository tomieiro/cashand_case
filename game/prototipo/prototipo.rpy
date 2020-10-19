define shp = Character("Sheppard")
define kmr = Character("Kamira")
image img_bg = "images/teste/bg_test.png"

default per_role = shp

label PROTOTIPO:

    play music "audio/musicas/Tensao.ogg" fadeout 1

    "Entendo... Estou na presença de duas pessoas. Vejamos..."
    scene img_bg

    menu:
        "Faça uma escolha:"

        "Diálogo A":
            $per_role = shp
            call DIALOGO_ROLE
            show sheppard neutro at center
            shp "Estou consciente!"
            hide sheppard neutro
            show kamira neutra at center
            kmr "Não acho conveniente sua chegada por aqui!"
            hide kamira neutra at center

        "Diálogo B":
            $per_role = kmr
            call DIALOGO_ROLE
            show sheppard neutro at center
            shp "Estou consciente!"
            hide sheppard neutro
            show kamira neutra at center
            kmr "Não acho conveniente sua chegada por aqui!"
            hide kamira neutra at center

        "Investigar a sala":
            show screen point_and_click_test() with dissolve
            jump PUZZLE_TESTE

    jump PROTOTIPO
    return



label DIALOGO_ROLE:
    if per_role == shp:
        show sheppard neutro at center
    else:
        show kamira neutra at center

    per_role "Me encarrego de te demitir..."
    per_role "Você realmente não se encaixa a este caso."
    hide sheppard neutro
    hide kamira neutra
    return

label PUZZLE_TESTE:
    window hide
    $renpy.pause(hard=True)
