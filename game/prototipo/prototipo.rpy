define sm = Character("Sheppard Magro")
define sg = Character("Sheppard Gordo")

default per_role = sm

label PROTOTIPO:

    "Executando protótipo..."

    menu:
        "Faça uma escolha:"

        "Diálogo A":
            $per_role = sm
            call DIALOGO_ROLE
            sm "Sou o Sheppard Magro"

        "Diálogo B":
            $per_role = sg
            call DIALOGO_ROLE
            sg "Sou o Sheppard Gordo"

        "Puzzle":
            show screen point_and_click_test() with dissolve
            jump PUZZLE_TESTE


    jump PROTOTIPO

    return



label DIALOGO_ROLE:
    per_role "bla bla bla"
    per_role "bla bla"
    per_role "bla bla bla bla"
    return

label PUZZLE_TESTE:
    window hide
    $renpy.pause(hard=True)
