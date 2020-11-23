label DIALOGO_IND_A_CENA12():
    "*Encontram [ind_a_info[0]] em roupas fúnebres, junto à entrada, sobre o jardim*"

    shp "Boa tarde [ind_a_info[1]], como está?"
    ind_a "Boa tarde, Sheppard."
    shp "O que faz aqui no jardim?"
    ind_a "Estava tentando me distrair"
    ind_a "Respirar um pouco de ar fresco..."
    shp "Entendo..."

    if ind_a_info[1] == "Hugo":
        call DIALOGO_HUGO_12_A
    elif ind_a_info[1] == "Joe":
        call DIALOGO_JOE_12_A
    elif ind_a_info[1] == "Kamira":
        call DIALOGO_KAMIRA_12_A
    elif ind_a_info[1] == "Catherine":
        call DIALOGO_CATHERINE_12_A

    ind_a "Até depois, Sheppard"
    "*[ind_a_info[0]] se afasta dos dois*"
    drc "Creio que serei considerado intruso em meio a esse imbróglio, senhor Sheppard."
    shp "Não se acanhe detetive, ainda há muitas outras saudações calorosas pela frente."

    return


label DIALOGO_HUGO12_A:
    show sheppard neutro:
        xalign 0.2 yalign 0.99999
    show hugo neutro:
        xalign 0.7 yalign 0.99999
    hugo "Estava aqui pensando em levar o Thorn pra passear um pouco também."
    shp "Olha lá, por falar nele..."
    "*Cão vem correndo e cheira a perna do detetive*"
    hugo "Verdade Thorn, nem tinha percebido esse senhor."
    hugo "Quem é ele, Sheppard?"
    shp "Por favor, detetive, se apresente."
    drc "Muito prazer, sou o detetive Rightclue. Estou aqui para ajudar no caso."
    hugo "Está a par de tudo, senhor Rightclue?"
    drc "Sim. Sheppard me instruiu. Tem minha palavra de sigilo."
    hugo "Certo. Não acho que sua presença seja bem vinda, principalmente por parte de minha tia, minha prima e meu irmão."
    hugo "Mas, contanto que nos ajude a desvendar o que está acontecendo, estamos de acordo."
    drc "Entendo..."
    drc "Esse aqui se chama Thorn?"
    hugo "Isso mesmo, tenho criado ele desde filhote."
    drc "Olá, amigo."
    hugo "É um bom garoto"
    hugo "Ei thorn, quer passear?"
    "*Thorn começa a balançar o rabo alegremente*"
    hugo "Muito bom, garoto. Vamos lá, vou colocar sua coleira."
    hugo "Pronto."
    hugo "Calma, calma, já vamos..."
    "*Hugo é arrastado pelo Thorn até a saída*"
    "Parecem muito próximos... e o cachorro é muito inteligente."
    shp "Tenha cuidado, Hugo!"
    drc "Esse está bem animado."
    shp "Ele sempre foi assim."
    return


label DIALOGO_JOE_12_A:
    show sheppard neutro:
        xalign 0.2 yalign 0.99999
    show joe neutro:
        xzoom 0.9 yzoom 0.9 xalign 0.7 yalign 0.99999
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


label DIALOGO_KAMIRA_12_A:
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

label DIALOGO_CATHERINE_12_A:
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
