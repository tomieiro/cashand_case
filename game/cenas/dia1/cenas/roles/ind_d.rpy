label DIALOGO_IND_D_CENA12():

    ind_d "Olá, senhor Sheppard."
    shp "Olá, [ind_d_info[1]]."
    shp "Está tudo bem?"
    ind_d "Tudo bem. Só estava aqui me recordando dos velhos tempos..."
    ind_d "Tenho excelentes lembranças daqueles tempos..."
    shp "Entendo..."

    if ind_d_info[1] == "Hugo":
        call DIALOGO_HUGO_12_D from _call_DIALOGO_HUGO_12_D
    elif ind_d_info[1] == "Joe":
        call DIALOGO_JOE_12_D from _call_DIALOGO_JOE_12_D
    elif ind_d_info[1] == "Kamira":
        call DIALOGO_KAMIRA_12_D from _call_DIALOGO_KAMIRA_12_D
    elif ind_d_info[1] == "Catherine":
        call DIALOGO_CATHERINE_12_D from _call_DIALOGO_CATHERINE_12_D

    ind_d "Bom, se me dão licença, eu tenho que ir..."

    hide joe with dissolve
    hide hugo with dissolve
    hide kamira with dissolve
    hide catherine with dissolve

    show sheppard neutro with moveinright:
        xalign 0.5 yalign 0.99999

    if ind_d_info[1] == "Catherine":
        shp "Parece que gostou de você."
        drc "Eu não teria essa opinião."
        shp "Acredite. Ela seria mais áspera."
        drc "..."

    return


label DIALOGO_HUGO_12_D:
    show sheppard neutro with moveinleft:
        xalign 0.2 yalign 0.99999
    show hugo neutro with dissolve:
        xalign 0.7 yalign 0.99999
    hugo "Mesmo ficando mais tempo na minha Kombi..."
    shp "Não se sente solitário quando fica por lá tanto tempo?"
    hugo "Claro que não. Tenho meu amigão, Thorn."

    play sound "audio/sonoplastia/Thorn.mp3"
    $renpy.pause(3, hard=hardPause)

    hugo "Quem é esse senhor?"
    drc "Muito prazer, sou o detetive Rightclue. Estou aqui para ajudar no caso."
    hugo "Está a par de tudo, senhor Rightclue?"
    drc "Sim. Sheppard me instruiu. Tem minha palavra de sigilo."
    hugo "Certo. Não acho que sua presença seja bem vinda, principalmente por parte de meu irmão, tia e prima."
    hugo "Mas, contanto que nos ajude a desvendar o que está acontecendo, estamos de acordo."
    drc "Entendo..."
    drc "Esse aqui se chama Thorn?"
    hugo "Isso mesmo, tenho criado ele desde filhote."
    drc "Olá, amigo."
    hugo "É um bom garoto."
    drc "O que é isso que ele trouxe junto?"
    shp "Um saco de... biscoitos..."
    hugo "Boa Thorn, também estou com fome."
    "*Hugo morde um dos biscoitos*"
    shp "... caninos. Biscoitos caninos."
    hugo "Uma delícia."
    hugo "Toma Thorn, você merece."
    $renpy.notify("Conquista - Biscoitos Thorn!")
    $persistent.conquista_biscoito = True
    $conferir_todas_conquistas()
    "Parecem muito próximos... e o cachorro parece ser bem inteligente..."
    shp "Você nunca muda, Hugo."
    hugo "Hmm?"
    hugo "Quer um pouco, Sheppard? Detetive?"
    shp "Não, obrigado..."
    drc "Obrigado, estou sem fome..."
    return

label DIALOGO_JOE_12_D:
    show sheppard neutro with moveinleft:
        xalign 0.2 yalign 0.99999
    show joe neutro with dissolve:
        xzoom 0.9 yzoom 0.9 xalign 0.7 yalign 0.99999
    joe "E quem seria esse novo rosto?"
    shp "Este é o detetive Rightclue."
    shp "Está aqui para investigar o assassinato do senhor Hougin a meu pedido."
    joe "Sheppard, eu conversei com você. Insisto que não precisamos de ajuda externa, creio eu. Ainda mais numa hora tão complicada."
    shp "Mil perdões, Joe, mas como fiel companheiro de seu tão estimado pai, insisto que o senhor Rightclue ajude a família neste momento."
    shp "Claro, já garanti que ele se comprometesse e exigi total sigilo nessa investigação."
    joe "... Bom você sabe oque esta fazendo e sabe as consequencias que a presença desse sugeito pode trazer."
    shp "..."
    joe "Mas espero que esse homem mude a minha opnião e seja útil para a nossa situação."
    drc "Acredite, eu vou..."
    joe "Enfim, faça o que bem entender."
    return

label DIALOGO_KAMIRA_12_D:
    show sheppard neutro with moveinleft:
        xzoom 0.9 yzoom 0.9 xalign 0.2 yalign 0.99999
    show kamira neutra with dissolve:
        xzoom 0.9 yzoom 0.9 xalign 0.7 yalign 0.99999
    kmr "Quem seria o senhor?"
    kmr "Não tenho nenhuma lembrança dele."
    drc "Na verdade, ainda não nos conhecemos."
    drc "Prazer. Rightclue. Sou o detetive contratado."
    kmr "Errado! Você é problema."
    kmr "Sheppard, o que significa isso?"
    shp "Está tudo certo, Kamira. O detetive prometeu sigilo e nós ajudará."
    kmr "De forma alguma, Sheppard. Isso só diz respeito a nós mesmos."
    shp "Confie em mim, Kamira. Prometi ao seu tio que cuidaria de vocês. E assim cumprirei."
    kmr "Você já prometeu muitas coisas a ele..."
    shp "..."
    kmr "Duvido que seja a única que pense assim, mas você deveria sair daqui senhor detetive."
    drc "... E vou, mas apenas quando o caso estiver resolvido."
    kmr "..."
    return

label DIALOGO_CATHERINE_12_D:
    show sheppard neutro with moveinleft:
        xzoom 0.9 yzoom 0.9 xalign 0.2 yalign 0.99999
    show catherine neutra with dissolve:
        xzoom 0.9 yzoom 0.9 xalign 0.7 yalign 0.99999
    cth "Mas, com o passar do tempo, vemos novas pessoas. Não é, senhor ..."
    drc "Rightclue, sou um detetive. Muito prazer."
    cth "..."
    "*Catherine encara Sheppard*"
    shp "O senhor Rightclue está aqui para ajudar no caso. Ele me foi muito bem recomendado."
    cth "Serei direta com você. A última coisa que precisamos é de mais problemas."
    cth "Já havia dito ao Sheppard. Sem pessoas externas. Mas parece que ele se recusa a me escutar."
    shp "Com todo respeito, senhorita, prometi ao seu irmão cuidar de todos e assim farei."
    cth "Você está apenas fazendo o que bem entende."
    cth "Que seja... Espero que consiga nos dizer algo, detetive."
    drc "Acredite, eu vou surpreender você e sua família."
    drc "Vocês não vão se arrepender."
    cth "... Veremos."
    return
