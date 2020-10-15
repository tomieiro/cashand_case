label TRANSICAO2:
    "*Os dois voltam à sala*"
    shp "Bom, peço que aguarde um momento detetive."
    drc "Tudo bem, senhor Sheppard."
    "*Sheppard sai (pensei em mencionar algo entre 20 minutos)*"
    "*Sheppard volta*"
    shp "Detetive, estou garantindo que o senhor possa passar a noite por aqui, e evitar despesas extras. Já conversei com os Cashand e te dou essa oportunidade."
    drc "Agradeço senhor Sheppard, mas acho que minha presença não é bem vinda."
    shp "Eu insisto detetive. Passarei esta noite aqui também, no quarto ao lado do seu."
    drc "Bom, se o senhor insiste, creio que seja prudente já que posso começar meu trabalho logo pela manhã."
    shp "De fato. Fico feliz em ouvir isso."
    shp "Então vamos. Um bom banho e um descanso serão benéficos antes de continuarmos."
    shp "Gostaria de conversar com o senhor tem a dizer após o jantar, que claro, providenciarei para que Martha leve ao seu quarto."
    drc "Agradeço senhor Sheppard, e claro, terei algo a dizer sobre toda essa situação."
    shp "Certo. Seu quarto é o segundo quarto desse primeiro andar. Logo ali."
    shp "Nos encontramos mais tarde então, senhor Rightclue."
    drc "Tudo bem, até mais, senhor Sheppard."
    "*Esvai a tela preta. Mostra quarto do detetive*"
    "Foi um excelente banho. Também já estou satisfeito com o jantar."

    if cluepoints >= 2:
        call CONCLUINDO_DIA1 from _call_CONCLUINDO_DIA1

    jump CENA14
