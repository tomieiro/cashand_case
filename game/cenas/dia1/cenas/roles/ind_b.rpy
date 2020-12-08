label DIALOGO_IND_B_CENA12:

    pause(1)

    shp "Boa tarde, [ind_b_info[1]]."
    ind_b "Olá, Sheppard."
    shp "Está bem? Precisa de algo?"
    ind_b "Tudo bem. Estava aqui, conversando com [ind_c_info[1]]."
    ind_b "Estamos tentando assimilar tudo ainda..."
    shp "Imagino..."

    if ind_b_info[1] == "Hugo":
        call DIALOGO_HUGO_12_B from _call_DIALOGO_HUGO_12_B
    elif ind_b_info[1] == "Joe":
        call DIALOGO_JOE_12_B from _call_DIALOGO_JOE_12_B
    elif ind_b_info[1] == "Kamira":
        call DIALOGO_KAMIRA_12_B from _call_DIALOGO_KAMIRA_12_B
    elif ind_b_info[1] == "Catherine":
        call DIALOGO_CATHERINE_12_B from _call_DIALOGO_CATHERINE_12_B

    ind_b "Até mais."
    ind_b "Você vem, [ind_c_info[1]]?"
    ind_c "Pode ir que já te alcanço..."

    hide joe with dissolve
    hide hugo with dissolve
    hide kamira with dissolve
    hide catherine with dissolve

    show sheppard neutro with moveinright:
        xalign 0.5 yalign 0.99999

    if ind_b_info[1] == "Catherine":
        shp "Parece que gostou de você."
        drc "Eu não teria essa opinião."
        shp "Acredite. Ela seria mais áspera."
        drc "..."

    return


label DIALOGO_HUGO_12_B:
    show sheppard neutro with moveinleft:
        xalign 0.2 yalign 0.99999

    show hugo neutro with dissolve:
        xalign 0.7 yalign 0.99999

    hugo "Quem é esse senhor?"
    drc "Muito prazer, sou o detetive Rightclue. Estou aqui para ajudar no caso."
    hugo "Acredito que você ja tenha sido instruído pelo senhor Sheppard, estou certo?"
    drc "Sim. Sheppard me instruiu bem. Tem minha palavra de sigilo."
    hugo "Certo. Não acho que sua presença seja bem vinda, principalmente por parte de minha familia."
    hugo "Mas, contanto que nos ajude a desvendar o que está acontecendo, estamos de acordo."
    drc "Entendo..."

    play sound "audio/sonoplastia/Thorn.mp3"
    $renpy.pause(3, hard=hardPause)

    drc "Olá, amigo."
    shp "É o Thorn, senhor detetive. Hugo o tem criado desde que este cão não era maior que dois palmos."
    hugo "É um bom rapaz."

    hide hugo with dissolve
    "*Hugo se agacha e faz carinho no Thorn*"

    hugo "Não é, Thorn?"
    "*Thorn lambe o rosto de Hugo em resposta*"
    "Parecem muito próximos... que cena bonita."

    show hugo neutro with dissolve:
        xalign 0.7 yalign 0.99999

    hugo "Bom, se me dão licença..."
    return

label DIALOGO_JOE_12_B:
    show sheppard neutro with moveinleft:
        xalign 0.2 yalign 0.99999
    show joe neutro with dissolve:
        xzoom 0.9 yzoom 0.9 xalign 0.7 yalign 0.99999
    joe "..."
    "*Joe encara Rightclue*"
    drc "..."
    joe "Ah..."
    joe "E quem seria esse, Sheppard? Acredito que não seja apropriado trazer desconhecidos para um enterro."
    shp "Perdão, Joe, este é o detetive Rightclue."
    shp "Ele está aqui para investigar o assassinato do senhor Hougin a meu pedido."
    joe "Entendo, um detetive..."
    joe "Sheppard... Insisto que não precisamos de ajuda externa. Ainda mais numa hora tão complicada."
    joe "Pense nos problemas que esse senhor pode trazer para a nossa família... e para você mesmo..."
    shp "Eu estou bem ciente disso, Joe."
    shp "Mas acredito que o senhor Rightclue vai pôr um fim nisso."
    shp "E claro, já garanti que ele se comprometesse e exigi total sigilo nessa investigação."
    joe "... Sinceramente, não estou com cabeça para continuar essa discussão com você."
    joe "Faça o que bem entender, contanto que esses ataques cessem."
    drc "Farei o meu melhor."
    joe "..."
    joe "Não me importo com o que você vai fazer, mas não piore as coisas..."
    joe "Todos aqui tem uma reputação a zelar..."
    return

label DIALOGO_KAMIRA_12_B:
    show sheppard neutro with moveinleft:
        xzoom 0.9 yzoom 0.9 xalign 0.2 yalign 0.99999
    show kamira neutra with dissolve:
        xzoom 0.9 yzoom 0.9 xalign 0.7 yalign 0.99999
    kmr "Quem seria o senhor?"
    drc "Prazer, Rightclue. Sou o detetive contratado."
    kmr "Espere um pouco, Sheppard. O que significa isso?"
    shp "Está tudo certo, Kamira, o detetive prometeu sigilo e nós ajudará."
    kmr "Não concordo com isso. De forma alguma, Sheppard. Isso só diz respeito a nós mesmos."
    shp "Confie em mim, Kamira. Prometi ao seu tio que cuidaria de vocês. Honrarei seu pedido."
    kmr "Não use o nome dele pra fazer o que bem entende."
    kmr "Não tenho razão para confiar nesse homem."
    kmr "Não me dê motivos para deixar de confiar em você também ..."
    shp "..."
    drc "Sei que a senhora e sua família estão passando por momentos difíceis, mas acredite, o senhor Sheppard está apenas querendo ajudar."
    kmr "..."
    drc "Eu darei o meu melhor para mostrar que a minha vinda não foi desnecessária."
    kmr "..."
    return

label DIALOGO_CATHERINE_12_B:
    show sheppard neutro with moveinleft:
        xzoom 0.9 yzoom 0.9 xalign 0.2 yalign 0.99999
    show catherine neutra with dissolve:
        xzoom 0.9 yzoom 0.9 xalign 0.7 yalign 0.99999
    cth "Quem seria esse rapaz, Sheppard?"
    shp "Este é detetive Rightclue. Está aqui para ajudar no caso."
    drc "Muito prazer."
    cth "Pois bem, meu anjo. Vou te dar uma pista."
    cth "Este caso não é para você. Não queremos mais pessoas aqui para piorar a situação."
    drc "..."
    cth "Sheppard, já havia dito a você. Sem pessoas externas."
    shp "Com todo respeito, senhorita, prometi ao seu irmão cuidar de todos e assim farei."
    cth "Você nunca me escuta..."
    cth "O que a minha família mais precisa agora é se unir, e não de um detetive."
    drc "Eu entendo que a senhora está de luto, e vou garantir que não tenha que lidar com mais problemas durante a minha estadia."
    cth "..."
    return
