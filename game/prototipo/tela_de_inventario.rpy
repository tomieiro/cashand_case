default itens_no_inventario = []
default item_mostrado = ""

transform bot_inv_tr:
    maxsize (140, 140)
    xalign 0.5
    yalign 0.5

screen tela_de_inventario():
    modal True

    hbox:
        frame:
            xalign 0.0
            yalign 0.0
            xsize 200
            ysize 720
            background "#000"
            vbox:
                xsize 1.0
                ysize 1.0
                for item in itens_no_inventario:
                    frame:
                        background "#fff"
                        xsize 180
                        ysize 180
                        margin (10, 20)
                        imagebutton:
                            idle item
                            action [SetVariable("item_mostrado", item), Jump("MOSTRA_ITEM_DO_INVENTARIO")]
                            at bot_inv_tr
        imagebutton:
            idle "images/teste/exit_but.png"
            action Jump("FECHAR_TELA_INVENTARIO")


label FECHAR_TELA_INVENTARIO:
    hide screen tela_de_inventario
    jump PUZZLE_TESTE

label MOSTRA_ITEM_DO_INVENTARIO:
    show screen mostra_item(item_mostrado) with dissolve
    pause 1.0
    hide screen mostra_item with dissolve
    jump PUZZLE_TESTE
