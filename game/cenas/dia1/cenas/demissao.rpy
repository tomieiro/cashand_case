label DEMISSAO:
    shp "Senhor Rightclue, não acho que o senhor esteja empenhado o bastante nesse caso. O senhor, me parece, investiga coisas irrelevantes ao meio do processo, e lhe falta a capacidade para ouvir."
    drc "Senhor Sheppard, o que quer dizer com isso?"
    shp "Quero dizer, senhor Rightclue, que o senhor não é a pessoa correta para este caso."
    shp "O senhor passará a noite aqui, uma vez que sou o contratante e não posso deixá-lo pela rua após todo esse dia, mas peço que se retire logo pela manhã."
    drc "Senhor Sheppard, eu realmente não entendo como o senhor conclui estes fatos."
    shp "Por favor, detetive. Não se oponha. Aqui está o valor pelo seu dia, e claro, não pagarei o planejado pelo caso completo."
    drc "Senhor Sheppard, mas eu..."
    shp "Espero que tenha sido claro, detetive. Tenho um compromisso com essa família e não posso me descuidar."
    shp "Bom, aproveite a noite e se retire pela manhã. Agradeço desde já. E uma boa noite."

    hide sheppard neutro with dissolve

    "*Sheppard fecha a porta*"
    drc "..."
    drc "Eu deveria ter pensado melhor sobre minhas escolhas..."

    window hide dissolve
    show ending bad
    with Dissolve(2, 4, 0.5)
