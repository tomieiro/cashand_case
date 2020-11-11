label DIALOGO_IND_C_CENA12:
    "*[ind_c_info[0]] se aproxima*"
    shp "Olá [ind_c_info[1]]."
    shp "Precisa de algo?"
    ind_c "Estava pensando sobre esse senhor..."
    shp "Algum problema?"
    ind_c "Me parece ser alguém envolvido com as autoridades..."

    if ind_c_info[1] == "Hugo":
        call DIALOGO_HUGO_12_C
    else:
        shp "Este é o nosso detetive contratado. Se apresente..."
        drc "Boa tarde, me..."
        ind_c "Perdão, senhor detetive, mas creio não ter assuntos a tratar por aqui."
        ind_c "O que acontece aqui é sigiloso e não queremos pessoas externas envolvidas."
        shp "Sinto muito [ind_c_info[1]], mas o detetive já está ciente de toda a situação."
        shp "Tenho ordens retroativas de seu [ind_c_info[2]] para cuidar desta família, e assim farei!"
        ind_c "Não concordo Sheppard, acho que você está atraindo uma atenção desnecessária. Mas faça como quiser."

    ind_c "Com licença, Sheppard."
    ind_c "Detetive..."
    ind_c "Espera, [ind_b_info[1]]. Vou com você..."
    "*[ind_b_info[0]] e [ind_c_info[0]] vão em direção ao portão*"
    return


label DIALOGO_HUGO_12_C:
    drc "Muito prazer, sou o detetive Rightclue. Estou aqui para ajudar no caso."
    hugo "Está a par de tudo, senhor Rightclue?"
    drc "Sim. Sheppard me instruiu. Tem minha palavra de sigilo."
    hugo "Certo. Não acho que sua presença seja bem vinda, principalmente por parte de minha prima, meu irmão e minha tia."
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
    ind_b "Hugo, você vai ficar brincando com o cachorro? não vai vir?"
    hugo "Já vou, já vou."
    return

label DIALOGO_JOE_12_C:
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

label DIALOGO_KAMIRA_12_C:
    return

label DIALOGO_CATHERINE_12_C:
    return
