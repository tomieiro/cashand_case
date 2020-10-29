label CENA12:

    "*Sheppard e Rightclue se dirigem para a mansão dos Cashand*"
    drc "É uma bela mansão."
    shp "Certamente senhor Rightclue. Este foi o castelo que sustentou Hougin ao longo de seus 36 anos de soberania."
    drc "Pois então, dois anos foram necessários para levantar um humilde jovem à senhor da máfia."
    shp "Precisamente. O senhor verá quando lhe digo que nada é por acaso. A genialidade deste homem era fascinante."
    drc "Se possível, não o exalte tanto em minha presença senhor Sheppard. Aceitei o caso por ordens superiores, mas não quero que o senhor pense que compactuo com a ideia do senhor Hougin."
    shp "De fato. Tentarei me segurar ao máximo."
    "*Entram pelo portão da mansão*"
    "*Encontram [ind_a_info[0]] em roupas fúnebres, junto à entrada, sobre o jardim*"
    shp "Boa tarde [ind_a_info[1]], como está."
    ind_a "Péssima tarde Sheppard. Quem ordenou para que trouxesse esse indivíduo para dentro de nossa casa?"
    shp "Perdão [ind_a_info[1]], este é o detetive Rightclue. Está aqui para investigar o assassinato do senhor Hougin a meu pedido."
    ind_a "Ultimamente tem se envolvido demais em nossa vida pessoal Sheppard. Não acha?"
    ind_a "Não precisamos de ajuda externa, creio eu. Ainda mais numa hora tão complicada."
    shp "Mil perdões [ind_a_info[1]], mas como fiel companheiro de seu tão estimado [ind_a_info[2]], insisto que o senhor Rightclue ajude a família neste momento."
    shp "Claro, já garanti que ele se comprometesse e exigi total sigilo nessa investigação."
    ind_a "Humph. Até depois Sheppard, não estou com ânimo para continuar essa discussão com você, faça o que bem entender, contanto que esses ataques cessem."
    "*[ind_a_info[0]] se afasta dos dois*"
    drc "Creio que serei considerado intruso em meio a esse imbróglio, senhor Sheppard."
    shp "Não se acanhe detetive, ainda há muitas outras saudações calorosas pela frente."
    "*Os dois seguem até a entrada*"
    "*Encontram [ind_b_info[0]] e [ind_c_info[0]] em vestes pretas, ao lado da porta*"
    shp "Boa tarde a vocês, [ind_b_info[1]] e [ind_c_info[1]]."
    ind_b "Olá Sheppard. Quem é o cavalheiro?"
    ind_c "Me parece ser alguém envolvido com as autoridades..."
    drc "Boa tarde, sou o detetive Rightclue, estou aqui a pedido sigiloso do senhor Sheppard para resolver a situação."
    ind_c "Perdão senhor detetive, mas creio não ter assuntos a tratar aqui. O que acontece aqui é sigiloso e não queremos pessoas externas envolvidas."
    shp "Sinto muito [ind_c_info[1]], mas o detetive já está ciente de toda a situação. Tenho ordem retroativas de seu [ind_c_info[2]] para cuidar desta família, e assim farei!"
    ind_c "Sempre te achei intrometido demais. Faça como quiser."
    shp "Não tem nada a dizer [ind_b_info[1]]?"
    ind_b "Espero que ele traga novos dias a essa casa, senhor Sheppard."
    "*[ind_b_info[0]] e [ind_c_info[0]] vão em direção ao portão*"
    drc "Estão realmente muito incomodados com minha presença senhor Sheppard, e parecem também desfazer um pouco do senhor."
    shp "Creio ser somente o momento. Acabam de perder dois familiares. As coisas se acalmarão, eu creio."
    drc "Tomara que sim."

    ## ROTEIRINHO DE EDICAO PARA O VINI
    # delicious vini
    # -> VOCE PRECISA CRIAR UMA CENA ABAIXO PRO IND_D
    # -> PRECISA COLOCAR UM IF LA NA CENA DO IND_A E AQUI ABAIXO NO IND_D, SE, CASO ELE FOR O HUGO,
    #CHAMA ESSE COMANDO: call FALA_DO_HUGO    ... CASO NAO SEJA, EXIBE O DIALOGO NORMAL(O DE CIMA JA TA LA)
    # E O DO IND_D VC CRIA ALGO, DE PREFERENCIA IGUALMENTE RUDE AO IND_A, JA QUE ELE SO PODERIA SER TROCADO DE LUGAR...
    # TENTE PUXAR ALGO MEIO ANOS 60 NA FALA, IGUAL EU VENHO TENTANDO, NA HORA DE ESCREVER;
    #JA ACRESCENTEI LA NO PERSONAGENS.RPY QUE O NEM O IND_B NEM O IND_C PODEM SER O HUGO NESSE PRIMEIRO DIA
    #VINI EDITE AQUI
    "*Entram na casa e encontram #INDIVIDUO FULANO AQUI VINI# em vestes escuras*"
    "..."
    "*#INDIVIDUO FULANO AQUI VINI# sai*"
    #VINI PARE AQUI
    shp "Vamos conhecer a casa, senhor Rightclue?"
    drc "Precisamente."

jump CENA13

label FALA_DO_HUGO:
    shp "Boa tarde Hugo!"
    hugo "Olá, boa tarde senhor Sheppard."
    hugo "Quem é o cavalheiro?"
    drc "Muito prazer, sou o detetive Rightclue. Estou aqui para ajudar no caso."
    hugo "Está a par de tudo senhor Rightclue?"
    drc "Sim. Sheppard me instruiu. Tem minha palavra de sigilo."
    hugo "Certo. Não acho que sua presença seja bem vinda, principalmente por parte de meu irmão, tia e prima. Mas contanto que nos ajude a desvendar o que está acontecendo. Estamos de acordo."
    "*Cão vem correndo e cheira a perna do detetive*"
    drc "Olá amigo."
    shp "É o Thorn, senhor detetive. Hugo tem o criado desde que este cão não era maior que dois palmos."
    hugo "É um bom rapaz."
    hugo "Bom, se me dão licença...."
    return
