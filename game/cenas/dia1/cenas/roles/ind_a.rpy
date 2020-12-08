label DIALOGO_IND_A_CENA12():
    "*Encontram [ind_a_info[0]], junto à entrada, sobre o jardim*"

    shp "Boa tarde, [ind_a_info[1]], como está?"
    ind_a "Boa tarde, Sheppard."
    shp "O que faz aqui no jardim?"
    ind_a "Estava tentando me distrair"
    ind_a "Respirar um pouco de ar fresco..."
    shp "Entendo..."

    if ind_a_info[1] == "Hugo":
        call DIALOGO_HUGO_12_A from _call_DIALOGO_HUGO_12_A
    elif ind_a_info[1] == "Joe":
        call DIALOGO_JOE_12_A from _call_DIALOGO_JOE_12_A
    elif ind_a_info[1] == "Kamira":
        call DIALOGO_KAMIRA_12_A from _call_DIALOGO_KAMIRA_12_A
    elif ind_a_info[1] == "Catherine":
        call DIALOGO_CATHERINE_12_A from _call_DIALOGO_CATHERINE_12_A

    ind_a "Até depois, Sheppard"

    hide joe with dissolve
    hide hugo with dissolve
    hide kamira with dissolve
    hide catherine with dissolve

    show sheppard neutro with moveinright:
        xalign 0.5 yalign 0.99999

    if ind_a_info[1] == "Catherine":
        shp "Parece que gostou de você."
        drc "Eu não teria essa opinião."
        shp "Acredite. Ela seria mais áspera."
        drc "..."

    drc "Creio que serei considerado intruso em meio a esse imbróglio, senhor Sheppard."
    shp "Não se acanhe, detetive, ainda há muitas outras saudações calorosas pela frente."

    return


label DIALOGO_HUGO_12_A:
    show sheppard neutro with moveinleft:
        xalign 0.2 yalign 0.99999
    show hugo neutro with dissolve:
        xalign 0.7 yalign 0.99999
    hugo "Estava aqui pensando em levar o Thorn pra passear um pouco também."
    shp "Olha lá, por falar nele..."

    play sound "audio/sonoplastia/Thorn.mp3"
    $renpy.pause(3, hard=hardPause)

    hugo "Verdade, Thorn, nem tinha percebido esse senhor."
    hugo "Quem é ele, Sheppard?"
    shp "Por favor, detetive, se apresente."
    drc "Muito prazer, sou o detetive Rightclue. Estou aqui para ajudar no caso."
    hugo "Está a par de tudo, senhor Rightclue?"
    drc "Sim. Sheppard me instruiu bem. Tem minha palavra de sigilo."
    hugo "Certo. Não acho que sua presença seja bem vinda, principalmente por parte de minha tia... minha prima... e meu irmão..."
    hugo "Mas... contanto que nos ajude a desvendar o que está acontecendo, estamos de acordo."
    drc "Entendo..."
    "Ele não parece muito bem."
    "Talvez eu deva me preparar para mais pessoas como ele."
    drc "Esse aqui se chama Thorn?"
    hugo "Isso mesmo, tenho criado ele desde filhote."
    drc "Olá, amigo."
    hugo "É um bom garoto."
    hugo "Ei, Thorn, quer passear?"
    "..."
    hugo "Muito bom, garoto. Vamos lá, vou colocar sua coleira."
    hugo "Pronto."
    hugo "Calma, calma, já vamos..."
    "Parecem muito próximos... e o cachorro é muito inteligente."
    shp "Tenha cuidado, Hugo!"
    "Este rapaz me parece bem, dada a situação."
    shp "Você nunca muda, Hugo."
    shp "Mas não guarde tudo para si."
    hugo "Agradeço, Sheppard. Mas estou bem."
    return


label DIALOGO_JOE_12_A:
    show sheppard neutro with moveinleft:
        xalign 0.2 yalign 0.99999
    show joe neutro with dissolve:
        xzoom 0.9 yzoom 0.9 xalign 0.7 yalign 0.99999
    joe "Me diga, Sheppard..."
    shp "...?"
    joe "Quem ordenou para que trouxesse esse indivíduo para dentro de nossa casa?"
    shp "Perdão, Joe, este é o detetive Rightclue."
    shp "Está aqui para investigar o assassinato do senhor Hougin a meu pedido."
    joe "Sheppard, eu conversei com você. Insisto que não precisamos de ajuda externa, creio eu. Ainda mais numa hora tão complicada."
    joe "Incluir pessoas de fora só vai piorar a situação"
    shp "Mil perdões Joe, mas, como fiel companheiro de seu tão estimado pai, insisto que o senhor Rightclue ajude a família neste momento."
    shp "Claro, já garanti que ele se comprometesse e exigi total sigilo nessa investigação."
    joe "Sinceramente não estou com cabeça para continuar essa discussão com você."
    joe "É um péssimo dia..."
    joe "Sinceramente espero que não tenhamos mais problemas por conta disso."
    joe "Ei, você!"
    drc "..."
    joe "Tente não destruir a reputação do senhor Sheppard com a nossa família."
    drc "Não vou..."
    drc "Tenho confiança em minha habilidades."
    joe "..."
    joe "Enfim, faça o que bem entender, contanto que esses ataques cessem."

    return


label DIALOGO_KAMIRA_12_A:
    show sheppard neutro with moveinleft:
        xzoom 0.9 yzoom 0.9 xalign 0.2 yalign 0.99999
    show kamira neutra with dissolve:
        xzoom 0.9 yzoom 0.9 xalign 0.7 yalign 0.99999
    kmr "Quem seria o senhor?"
    drc "Prazer. Rightclue. Sou o detetive contratado."
    kmr "Espere um pouco, Sheppard. O que significa isso?"
    shp "Está tudo certo, Kamira, o detetive prometeu sigilo e nos ajudará."
    kmr "Não concordo com isso. De forma alguma, Sheppard. Isso só diz respeito a nós mesmos."
    kmr "Você não tem o direito de trazer mais problemas para a nossa casa."
    shp "Confie em mim, Kamira. Prometi ao seu tio que cuidaria de vocês. Honrarei seu pedido."
    drc "Acredite nas palavras do senhor Sheppard senhorita."
    drc "Nós vamos resolver o seu problema."
    kmr "Isso nós vamos descobrir..."
    kmr "Só tente não estragar tudo..."
    return

label DIALOGO_CATHERINE_12_A:
    show sheppard neutro with moveinleft:
        xzoom 0.9 yzoom 0.9 xalign 0.2 yalign 0.99999
    show catherine neutra with dissolve:
        xzoom 0.9 yzoom 0.9 xalign 0.7 yalign 0.99999
    cth "Quem seria o lindo rapaz?"
    shp "Este é detetive Rightclue. Está aqui para ajudar no caso."
    drc "Muito prazer."
    cth "Pois bem, meu anjo. Serei direta com você. Creio que não tenha assuntos a tratar aqui."
    cth "Sheppard, já havia lhe dito. Sem pessoas externas."
    shp "Com todo respeito, senhorita, prometi ao seu irmão cuidar de todos e assim farei."
    cth "Você nunca me escuta..."
    cth "Bom, se esse rapaz se mostrar capaz de fazer algo, vamos sair no lucro."
    drc "Acredite, vou surpreender você e sua família."
    cth "Veremos..."
    return
