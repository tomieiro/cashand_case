label CONCLUINDO_DIA1:

    "Mas preciso ter uma conclusão inicial para este caso."
    "O senhor Sheppard conta comigo."

    call INVENTARIO_DE_ESCOLHA_DIA01 from _call_INVENTARIO_DE_ESCOLHA_DIA01
    hide screen inventario_de_escolha with dissolve

    $pac1_itens_no_inventario.remove(pac1_item_relogio)
    $pac1_itens_no_inventario.remove(pac1_item_sangue)

    "Não queria acreditar nessa possibilidade..."
    "Mas as evidências levam a crer que o grupo no qual o envolvido no crime faz parte é:"

    call APP_DIA1 from _call_APP_DIA1

    "É isso. O assassino está entre os herdeiros..."
    "..."

    return
