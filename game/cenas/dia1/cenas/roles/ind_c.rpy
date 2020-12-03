label DIALOGO_IND_C_CENA12:
    shp "Olá [ind_c_info[1]]."
    shp "Precisa de algo?"
    ind_c "Estava pensando sobre esse senhor..."
    shp "Algum problema?"
    ind_c "Me parece ser alguém envolvido com as autoridades..."

    if ind_c_info[1] == "Hugo":
        call DIALOGO_HUGO_12_C
    elif ind_c_info[1] == "Joe":
        call DIALOGO_JOE_12_C
    elif ind_c_info[1] == "Kamira":
        call DIALOGO_KAMIRA_12_C
    elif ind_c_info[1] == "Catherine":
        call DIALOGO_CATHERINE_12_C

    ind_c "Com licença, Sheppard."
    ind_c "Detetive..."
    ind_c "Espera, [ind_b_info[1]]. Vou com você..."

    if ind_c_info[1] == "Catherine":
        shp "Parece que gostou de você."
        drc "Eu não teria essa opinião."
        shp "Acredite. Ela seria mais áspera."
        drc "..."

    hide joe with dissolve
    hide hugo with dissolve
    hide kamira with dissolve
    hide catherine with dissolve

    show sheppard neutro with moveinright:
        xalign 0.5 yalign 0.99999

    return


label DIALOGO_HUGO_12_C:
    show sheppard neutro with moveinleft:
        xalign 0.2 yalign 0.99999
    show hugo neutro with dissolve:
        xalign 0.7 yalign 0.99999
    drc "Muito prazer, sou o detetive Rightclue. Estou aqui para ajudar no caso."
    hugo "Está a par de tudo, senhor Rightclue?"
    drc "Sim. Sheppard me instruiu. Tem minha palavra de sigilo."
    hugo "Certo. Não acho que sua presença seja bem vinda, principalmente por parte de minha prima, meu irmão e minha tia."
    hugo "Mas, contanto que nos ajude a desvendar o que está acontecendo, estamos de acordo."
    drc "Entendo..."

    play sound "audio/sonoplastia/Thorn.mp3"
    $renpy.pause(3, hard=hardPause)

    drc "Olá amigo."
    shp "É o Thorn, senhor detetive. Hugo tem o criado desde que este cão não era maior que dois palmos."
    hugo "É um bom rapaz."
    "*Hugo se agacha e faz carinho no Thorn*"
    hugo "Não é, Thorn?"
    "*Thorn lambe o rosto de Hugo em resposta*"
    "Parecem muito próximos... que cena bonita."
    ind_b "Hugo, você vai ficar brincando com o cachorro? não vai vir?"
    hugo "Já vou, já vou."
    return

label DIALOGO_JOE_12_C:
    show sheppard neutro with moveinleft:
        xalign 0.2 yalign 0.99999
    show joe neutro with dissolve:
        xzoom 0.9 yzoom 0.9 xalign 0.7 yalign 0.99999
    drc "Sou o detetive Rightclue, foi contratado pelo senhor Sheppard para investigar o caso."
    joe "..."
    joe "Sheppard, eu conversei com você. Insisto que não precisamos de ajuda externa, creio eu. Ainda mais numa hora tão complicada."
    shp "Mil perdões Joe, mas, como fiel companheiro de seu tão estimado pai, insisto que o senhor Rightclue ajude a família neste momento."
    shp "Claro, já garanti que ele se comprometesse e exigi total sigilo nessa investigação."
    joe "Entedo o seu ponto de vista, mas lembre-se meu pai nem sempre estava certo, e não era digno de confiança."
    shp "..."
    joe "... Mas quem somos nos para falarmos dos mortos."
    joe "Enfim, faça o que bem entender, contanto que esses ataques cessem."
    drc "Eu farei e provarei que Sheppard não esta errado em me chamar."
    joe "..."
    "*Joe encara Rightclue*"
    return

label DIALOGO_KAMIRA_12_C:
    show sheppard neutro with moveinleft:
        xzoom 0.9 yzoom 0.9 xalign 0.2 yalign 0.99999
    show kamira neutra with dissolve:
        xzoom 0.9 yzoom 0.9 xalign 0.7 yalign 0.99999
    shp "Este é o nosso detetive contratado. Se apresente..."
    drc "Boa tarde, me..."
    kmr "Perdão, senhor detetive, mas creio não ter assuntos a tratar por aqui."
    kmr "O que acontece aqui é sigiloso e não queremos pessoas externas envolvidas."
    kmr "Então pode voltar para o lugar de onde veio."
    drc "..."
    shp "Sinto muito Kamira, mas o detetive já está ciente de toda a situação."
    shp "Tenho ordens retroativas de seu tio para cuidar desta família, e assim farei!"
    kmr "Você é muito atrevido de usar um homem morto como uma desculpa para fazer o que quer."
    kmr "Mas faça como quiser, você vai ter as consequencias de seus atos cedo ou tarde."
    shp "..."
    drc "Todos vamos não..."
    kmr "..."
    drc "Principalmente o responsavel por tudo isso quando for encontrado."
    return

label DIALOGO_CATHERINE_12_C:
    show sheppard neutro with moveinleft:
        xzoom 0.9 yzoom 0.9 xalign 0.2 yalign 0.99999
    show catherine neutra with dissolve:
        xzoom 0.9 yzoom 0.9 xalign 0.7 yalign 0.99999
    shp "Este é detetive Rightclue. Está aqui para ajudar no caso."
    drc "Muito prazer."
    cth "..."
    cth "Sheppard, já havia dito a você. Sem pessoas externas."
    shp "Com todo respeito, senhorita, prometi ao seu irmão cuidar de todos e assim farei."
    cth "Você nunca me escuta ..."
    shp "..."
    cth "Eu poderia ficar aqui discutindo com você opções melhores mas minha familia precisa de mim."
    cth "Espero que esse detetive seja util em nosso problema."
    drc "Acredite eu serei."
    cth "Veremos..."
    return
