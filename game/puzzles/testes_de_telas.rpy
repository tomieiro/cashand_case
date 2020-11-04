label TESTES_TELAS:
    "Coleta os itens aí, bro!"
    jump CHAMA_TELA_PAC_TESTE

label FIM_PAC_TESTE:
    "Prontooo, agora vamos escolhê-los"
    hide screen point_and_click_teste with dissolve
    scene cidade with dissolve
    "..."
    "Bom, tô com fome véi..."
    $print(renpy.get_return_stack())
    jump INVENTARIO_DE_ESCOLHA_TESTE


label FIM_IDE_TESTE:
    hide screen inventario_de_escolha with dissolve
    $print(renpy.get_return_stack())
    return
