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

    if ind_a_info[1] == "Hugo":
        call DIALOGO_HUGO_12_B
    elif ind_a_info[1] == "Joe":
        call DIALOGO_JOE_12_B
    elif ind_a_info[1] == "Kamira":
        call DIALOGO_KAMIRA_12_B
    elif ind_a_info[1] == "Catherine":
        call DIALOGO_CATHERINE_12_B

    ind_b "Até mais."
    ind_b "Você vem, [ind_c_info[1]]?"
    ind_c "Pode ir que já te alcanço..."
    "*[ind_b_info[0]] se retira*"
    return


label DIALOGO_HUGO12_B:
    show sheppard neutro:
        xzoom 0.9 yzoom 0.9 xalign 0.2 yalign 0.99999
    show hugo neutro:
        xzoom 0.9 yzoom 0.9 xalign 0.7 yalign 0.99999
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
    show sheppard neutro:
        xzoom 0.9 yzoom 0.9 xalign 0.2 yalign 0.99999
    show joe neutro:
        xzoom 1.2 yzoom 1.2 xalign 0.7 yalign 0.99999
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

label DIALOGO_KAMIRA_12_B:
    show sheppard neutro:
        xzoom 0.9 yzoom 0.9 xalign 0.2 yalign 0.99999
    show kamira neutro:
        xzoom 1.2 yzoom 1.2 xalign 0.7 yalign 0.99999
    kmr "Quem seria o senhor?"
    drc "Prazer. Rightclue. Sou o detetive contratado."
    kmr "Espere um pouco Sheppard, o que significa isso?"
    shp "Está tudo certo Kamira, o detetive prometeu sigilo e nós ajudará."
    kmr "Não concordo com isso. De nenhuma forma, Sheppard. Isso só diz respeito a nós mesmos."
    shp "Confie em mim Kamira. Prometi ao seu tio que cuidaria de vocês. E assim cumprirei."
    kmr "..."
    return

label DIALOGO_CATHERINE_12_B:
    show sheppard neutro:
        xzoom 0.9 yzoom 0.9 xalign 0.2 yalign 0.99999
    show catherine neutro:
        xzoom 1.2 yzoom 1.2 xalign 0.7 yalign 0.99999
    cth "Quem seria o lindo rapaz?"
    shp "Este é detetive Rightclue. Está aqui para ajudar no caso."
    drc "Muito prazer."
    cth "Pois bem, meu anjo. Serei direta com você. Acho que você não tenha assuntos a tratar aqui."
    cth "Sheppard, já havia dito a você. Sem pessoas externas."
    shp "Com todo respeito, senhorita, prometi ao seu irmão cuidar de todos e assim farei."
    cth "Você nunca me escuta..."
    return
