label DIALOGO_IND_D_CENA12():

    "*Entram na casa e encontram [ind_d_info[0]]*"

    ind_d "Olá, senhor Sheppard."
    shp "Olá, [ind_d_info[1]]."
    shp "Está tudo bem?"
    ind_d "Tudo bem. Só estava aqui me recordando dos velhos tempos..."
    ind_d "Tenho algumas lembranças boas daqui..."
    shp "Sei..."

    if ind_d_info[1] == "Hugo":
        call DIALOGO_HUGO12_D
    else:
        ind_d "Quem é este senhor ao seu lado?"
        drc "Muito prazer, sou o detetive Rightclue. Estou aqui para ajudar no caso."
        ind_d "imagino que o isso seja coisa sua, senhor Sheppard."
        shp "Estou apenas fazendo o meu trabalho, [ind_d_info[1]]"
        shp "O senhor Rightclue já está a par de toda a nossa situação."
        ind_d "Certo. Não concordo com a sua presença aqui, mas espero que consigo nos ajudar com o nosso problema."

    ind_d "Bom, se me dão licença, eu tenho que ir..."
    "*[ind_d_info[0]] sai*"

    return


label DIALOGO_HUGO12_D:
    show sheppard neutro:
        xzoom 0.9 yzoom 0.9 xalign 0.2 yalign 0.99999
    show hugo neutro:
        xzoom 0.9 yzoom 0.9 xalign 0.7 yalign 0.99999
    hugo "Mesmo ficando mais tempo na minha Kombi..."
    shp "Não se sente solitário quando fica por lá tanto tempo?"
    hugo "Claro que não. Tenho meu amigão, Thorn."
    "*Cão vem correndo e cheira a perna do detetive*"
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
    hugo "É um bom garoto"
    drc "O que é isso que ele trouxe junto?"
    shp "Um saco de... biscoitos..."
    hugo "Boa Thorn, também estou com fome."
    "*Hugo morde um dos biscoitos*"
    shp "... caninos. Biscoitos caninos."
    hugo "Uma delícia."
    hugo "Toma Thorn, você merece."
    "Parecem muito próximos... e o cachorro parece ser bem inteligente..."
    shp "Você nunca muda, Hugo."
    hugo "Hum?"
    hugo "Quer um pouco, Sheppard? detetive?"
    shp "Não, obrigado..."
    drc "Obrigado, estou sem fome..."
    return

label DIALOGO_JOE_12_D:
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
