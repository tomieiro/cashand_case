label CENA25:

    scene quarto
    with Fade(3, 5, 0.5)
    play sound "audio/sonoplastia/SentandoNaCama.mp3"
    $renpy.pause(2, hard=hardPause)

    "..."
    "..."
    "..."
    "O que foi tudo isso?"
    "Qual o sentido desses eventos?"
    "Quem é o culpado?"
    "..."
    "Estão preparando o velório de Kamira."

    "Assim como Sheppard, ela será enterrada amanhã de manhã."
    "Preciso pensar..."

    call INVENTARIO_DE_ESCOLHA_DIA02 from _call_INVENTARIO_DE_ESCOLHA_DIA02

    "Talvez se eu..."

    call SLIDER_PUZZLE_3X3_DIA02 from _call_SLIDER_PUZZLE_3X3_DIA02

    $pac1_itens_no_inventario.remove(pac2_item_papel)
    $renpy.pause(2, hard=hardPause)
    show screen mostra_item("images/engler/itens/bilhete.png") with dissolve
    "Gravador cômoda senha culpado"
    hide screen mostra_item with dissolve
    "Espere um pouco... É isso..."
    "..."

    play sound "audio/sonoplastia/Passos.mp3"
    scene fundo preto
    with Fade(1,2,0.5)
    play sound "audio/sonoplastia/AbrindoPorta.mp3"
    $renpy.pause(1, hard=hardPause)
    scene corredor hall
    with Fade(2,1,0.5)
    play sound "audio/sonoplastia/FechandoPorta.mp3"
    $renpy.pause(2, hard=hardPause)
    play sound "audio/sonoplastia/Passos.mp3"
    $renpy.pause(3, hard=hardPause)
    play sound "audio/sonoplastia/AbrindoPorta.mp3"
    $renpy.pause(2, hard=hardPause)
    scene quarto hougin
    with Fade(1, 1, 0.5)
    play sound "audio/sonoplastia/FechandoPorta.mp3"
    $renpy.pause(2, hard=hardPause)

    "Se eu não estiver enganado..."

    call CHAMA_TELA_PAC_DIA2 from _call_CHAMA_TELA_PAC_DIA2

    "Analisando os fatos..."

    call INVENTARIO_DE_ESCOLHA_DIA02_2 from _call_INVENTARIO_DE_ESCOLHA_DIA02_2

    "Bom, vamos tentar..."

    call SLIDER_PUZZLE_3X3_DIA02_2 from _call_SLIDER_PUZZLE_3X3_DIA02_2

    play sound "audio/sonoplastia/Destravando.mp3"
    $renpy.pause(2, hard=hardPause)

    "Excelente. Agora a tampa pode ser fechada."

    show screen mostra_item("images/engler/itens/gravador desligado fechado.png") with dissolve

    "Ligo o gravador na tomada e..."
    "Hmmm..."
    "Basta setar o modo de reprodução e..."
    "..."
    "..."
    drc "Mas que droga!"
    "..."
    drc "Quebrado. Claro."
    "..."
    "..."
    "Hmm?"
    "..."
    drc "O senhor era mesmo um homem astuto, senhor Hougin."
    drc "Quem diria possuir um artefato dessa complexidade."
    "Há um segundo sistema. Dessa vez parece algum tipo de ativação elétrica."
    "Isso é tecnologia de ponta. Realmente fascinante."
    hide screen mostra_item with dissolve
    "Bom, vamos à tentativa..."

    call LIGHTS_OUT_PUZZLE_4X4_DIA02 from _call_LIGHTS_OUT_PUZZLE_4X4_DIA02

    play music "audio/musicas/Onde.mp3" fadein 4.0

    show screen mostra_item("images/engler/itens/gravador ligado fechado.png") with dissolve
    "Excelente!"
    "Agora.... Escutemos..."
    "..."
    "..z....sh.....zh.....sh.....z..."
    kmr "hzGora.... zhsh.... im.... Está po...shz... cionado."
    kmr "Pronto. Tio, isto monitorará o senhor mais esta noite."
    hgin "Não preciso destas tranqueiras."
    kmr "Será benéfico ao senhor. Podemos mostrar suas tosses e faltas de ar ao médico."
    kmr "Tenho certeza que no futuro isso será muito usado."
    hgin "Ora, vamos. Como se eu fosse um velho prestes a morrer..."
    kmr "..."
    kmr "Me sinto na obrigação de repetir..."
    kmr "O senhor deveria parar, tio."
    kmr "O senhor está doente. Estas bebidas, cigarros, noites boêmias..."
    kmr "Estas coisas não se encaixam mais à sua saúde."
    hgin "Ha ha ha. De fato."
    hgin "Mas sabe, minha querida, não sentarei esperando a morte."
    hgin "Se tiver que morrer, morrerei em pé."
    kmr "..."
    kmr "Por quê? Por que o senhor não entende?"
    kmr "Já te pedi muitas e muitas vezes. Mas o senhor não me ouve."
    kmr "O senhor vai morrer! Sua saúde já não suporta mais isso."
    kmr "Quando você me escutará? Quando? Quando?"
    hgin "Já faz muito tempo que deixei de escutar a todos."
    hgin "Aproveitarei até meu último momento."
    kmr "O senhor não entende?"
    kmr "O senhor não entende que você fará muita falta? Principalmente para mim."
    kmr "Por que o senhor não me escuta?"
    hgin "..."
    hgin "Realmente me desculpe. Mas eu não posso."
    hgin "Prefiro mil vezes morrer de corpo, do que de espírito."
    "*Kamira começa a chorar*"
    kmr "..."
    kmr "Bom, se o senhor quer assim. Então que assim seja!"

    play sound "audio/sonoplastia/AbrindoPorta.mp3"
    $renpy.pause(1, hard=hardPause)
    play sound "audio/sonoplastia/FechandoPorta.mp3"
    $renpy.pause(2, hard=hardPause)

    "..."
    "..z....sh.....zh.....sh.....z..."
    drc "Então era isso..."
    drc "..."
    drc "Não acredito."
    drc "Ela estava preocupada com ele."
    drc "Com sua saúde inclusive."
    drc "Acho que..."

    "..z....sh.....zh.....sh.....z..."

    play sound "audio/sonoplastia/AbrindoPorta.mp3"
    $renpy.pause(2, hard=hardPause)

    hgin "Então você voltou."
    hgin "..."
    hgin "Escondeu-se de Kamira? Pois bem... Achei muito estranho. Você nunca foi sequer dócil comigo." #rigato: a fala de ind_a na cena 23 dá a entender que não visitou Hougin, o que seria uma contradicao no caso de Hugo. Mas, sendo ele o assassino, acho que faz sentido ele mentir sobre isso.
    hgin "Acha que va..."

    play sound "audio/sonoplastia/Esfaqueando.mp3"
    $renpy.pause(2, hard=hardPause)

    hgin "Argh.... Aaah.....A...... Arhc...."
    hgin "Cloh....... argh...... clogh..."
    hgin "..."
    hgin "..."

    play sound "audio/sonoplastia/FechandoPorta.mp3"
    $renpy.pause(2, hard=hardPause)

    "..."
    hide screen mostra_item with dissolve

    drc "..."
    drc "Meu Deus..."
    drc "Foi o momento exato."
    "Ele não conseguiu dizer quem era."
    "Era disso que Kamira dizia mais cedo."
    "Então, com isso, posso afirmar que..."

    call APP_DIA2 from _call_APP_DIA2

    "Meu Deus. Ela era inocente."
    "Por minha incompetência e falta de tato, ela se foi."
    "..."
    "Não. Não é hora disso. Preciso salvar os demais. Pense. Pense."
    "Sobraram três indivíduos. Joe, Hugo e Catherine."
    "O culpado está aqui. Dentro dessa casa. Quem será a próxima vítima?"
    "..."
    "Não... não arriscaria... Só tem uma chance de se safar agora."
    "Assumo que conheça o trato com o senhor Venchinni. Aquele barulho, naquela noite, prova isso."
    "Todavia não sabe da fúria do senhor Venchinni, após a morte do senhor Sheppard, eu assumo."
    "Tenho o controle da situação."
    "Por hoje descansarei. Tenho profunda certeza que o culpado não arriscaria matar outro membro da família."
    "Pela manhã, após o velório, será minha cartada final."
    "É tudo ou nada."
    "É só uma questão de tempo..."
    stop music fadeout(3)
    "..."
    jump CENA31
