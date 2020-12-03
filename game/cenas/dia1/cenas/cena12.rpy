#Ver de trocar a apresentacao pra hora que eles se encontrarem

label CENA12:
    scene jardim
    with Fade(2, 2, 0.5)
    play music "audio/musicas/Onde.mp3"

    drc "É uma bela mansão."

    show sheppard neutro with dissolve:
        xzoom 0.9 yzoom 0.9 xalign 0.5 yalign 0.99999

    shp "Certamente senhor Rightclue. Este foi o castelo que sustentou Hougin ao longo dos ultimos 30 anos."
    drc "Pois então, oito anos foram necessários para elevar um humilde jovem à posição de senhor desse imperio."
    shp "Precisamente. O senhor verá quando lhe digo que nada é por acaso. A genialidade deste homem para era fascinante."
    drc "Se possível, não o exalte tanto em minha presença senhor Sheppard. Aceitei o caso por ordens superiores, mas não quero que o senhor pense que compactuo com a ideia do senhor Hougin."
    shp "De fato. Tentarei me segurar ao máximo."

    call DIALOGO_IND_A_CENA12 from _call_DIALOGO_IND_A_CENA12
    call INTRODUCAO_PERSONAGEM_CENA12(ind_a_info) from _call_INTRODUCAO_PERSONAGEM_CENA12

    $renpy.pause(2, hard=hardPause)

    call DIALOGO_IND_B_CENA12 from _call_DIALOGO_IND_B_CENA12
    call INTRODUCAO_PERSONAGEM_CENA12(ind_b_info) from _call_INTRODUCAO_PERSONAGEM_CENA12_1

    $renpy.pause(2, hard=hardPause)

    call DIALOGO_IND_C_CENA12 from _call_DIALOGO_IND_C_CENA12
    call INTRODUCAO_PERSONAGEM_CENA12(ind_c_info) from _call_INTRODUCAO_PERSONAGEM_CENA12_2

    $renpy.pause(1, hard=hardPause)

    drc "Estão, realmente, muito incomodados com minha presença senhor Sheppard, e parecem também desfazer um pouco do senhor."
    shp "Creio ser somente o momento. Acabam de perder dois familiares. As coisas se acalmarão, eu creio."
    drc "Tomara que sim."

    $renpy.pause(2, hard=hardPause)

    call DIALOGO_IND_D_CENA12 from _call_DIALOGO_IND_D_CENA12
    call INTRODUCAO_PERSONAGEM_CENA12(ind_d_info) from _call_INTRODUCAO_PERSONAGEM_CENA12_3

    shp "Bom, acho que você já viu todos os herdeiros..."
    drc "Espere um segundo, Sheppard. Não eram cinco? Onde está o último?"
    shp "O último herdeiro era Lostie Annou Cashand, segundo irmão mais novo do senhor Hougin Cashand, que fora assassinado esta noite."
    drc "Intrigante... Podemos afirmar que os assassinatos ocorreram pelo interesse nos bens do senhor Hougin, creio eu. Talvez alguém interessado em lesar a família e ficar com o dinheiro?"
    shp "De fato. Acredito ser totalmente coerente com a situação, visto que o senhor Hougin andava ruim de saúde."
    shp "Todavia, ele não morreu devido à sua doença. Foi encontrado no terceiro quarto do segundo andar da mansão dos Cashand, apunhalado no peito."
    drc "E o senhor Lostie?"
    shp "Com o pescoço quebrado, próximo ao jardim da mansão."
    shp "..."
    drc "..."
    shp "Vamos conhecer o restante da casa, senhor Rightclue?"
    drc "Precisamente."
    play sound "audio/sonoplastia/AbrindoPorta.mp3"
    $renpy.pause(2, hard=hardPause)
    jump CENA13
