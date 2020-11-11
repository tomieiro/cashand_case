label DIALOGO_IND_B_CENA12:
    "*Os dois seguem até a entrada*"
    "*Encontram [ind_b_info[0]] e [ind_c_info[0]] em vestes pretas, ao lado da porta*"

    "*[ind_b_info[1]] se aproxima*"
    shp "Boa tarde, [ind_b_info[1]]."
    ind_b "Olá Sheppard."
    shp "Está bem? precisa de algo?"
    ind_b "Tudo bem. Estava aqui, conversando com [ind_c_info[1]]."
    ind_b "Estamos tentando assimilar tudo ainda..."
    shp "Imagino..."

    if ind_b_info[1] == "Hugo":
        call DIALOGO_HUGO12_B
    else:
        ind_b "Quem é o cavalheiro?"
        drc "Boa tarde, sou o detetive Rightclue, estou aqui a pedido sigiloso do senhor Sheppard para resolver a situação."
        ind_b "..."
        shp "Algo a dizer, [ind_b_info[1]]?"
        ind_b "Espero que ele traga novos dias a essa casa, senhor Sheppard."


    ind_b "Até mais."
    ind_b "Você vem, [ind_c_info[1]]?"
    ind_c "Pode ir que já te alcanço..."
    "*[ind_b_info[0]] se retira*"
    return


label DIALOGO_HUGO12_B:
    hugo "Quem é esse senhor?"
    drc "Muito prazer, sou o detetive Rightclue. Estou aqui para ajudar no caso."
    hugo "Está a par de tudo, senhor Rightclue?"
    drc "Sim. Sheppard me instruiu. Tem minha palavra de sigilo."
    hugo "Certo. Não acho que sua presença seja bem vinda, principalmente por parte de meu irmão, tia e prima."
    hugo "Mas, contanto que nos ajude a desvendar o que está acontecendo, estamos de acordo."
    drc "Entendo..."
    "*Cão vem correndo e cheira a perna do detetive*"
    drc "Olá amigo."
    shp "É o Thorn, senhor detetive. Hugo tem o criado desde que este cão não era maior que dois palmos."
    hugo "É um bom rapaz."
    "*Hugo se agacha e faz carinho no Thorn*"
    hugo "Não é, Thorn?"
    "*Thorn lambe o rosto de Hugo em resposta*"
    "Parecem muito próximos... que cena bonita."
    hugo "Bom, se me dão licença..."
    return

label DIALOGO_JOE_12_B:
    joe "Me diga, Sheppard..."
    shp "...?"
    joe "Quem ordenou para que trouxesse esse indivíduo para dentro de nossa casa?"
    shp "Perdão Joe, este é o detetive Rightclue."
    shp "Está aqui para investigar o assassinato do senhor Hougin a meu pedido."
    joe "Sheppard, eu conversei com você. Insisto que não precisamos de ajuda externa, creio eu. Ainda mais numa hora tão complicada."
    shp "Mil perdões Joe, mas, como fiel companheiro de seu tão estimado pai, insisto que o senhor Rightclue ajude a família neste momento."
    shp "Claro, já garanti que ele se comprometesse e exigi total sigilo nessa investigação."
    joe "Sinceramente não estou com cabeça para continuar essa discussão com você."
    joe "Péssima tarde..."
    joe "Enfim, faça o que bem entender, contanto que esses ataques cessem."
    return
